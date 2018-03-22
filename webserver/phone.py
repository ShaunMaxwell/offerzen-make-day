import requests
from config import PhonealotConfig

class Phone():

    def __init__(self):
        self.apikey = PhonealotConfig.DF_API_KEY
        # self.tal_qry = "https://api.takealot.com/rest/v-1-6-0/productlines/search?sort=Default%20Descending&rows=1&start=0&detail=mlisting&qsearch={0}&filter=Available:true"
        self.tal_qry = "https://api.takealot.com/rest/v-1-6-0/productlines/search?sort=Default%20Descending&rows=10&start=0&detail=mlisting&qsearch={0}&filter=Type:16&Available:true"

    def get_all_models(self):
        return requests.get('https://sandbox.root.co.za/v1/insurance/modules/root_gadgets/models',
                                auth=(self.apikey, ''))

    def get_brands(self):
        all_models = self.get_all_models().json()
        brands = set([phone['make'].encode('ascii') for phone in all_models])
        return list(brands)

    def get_models_by_brand(self, brand=None):
        all_models = self.get_all_models().json()
        if brand:
            models = list(set([phone['name'].encode('ascii') for phone in all_models if brand.lower() in phone['make'].lower()]))
        else:
            models = None
        return_dict = {}
        for (idx, model) in enumerate(models):
            return_dict[idx] = model
        return return_dict

    def get_plid(self, brand, phone):
        search = self.tal_qry.format(brand + "%20" + phone)
        print search
        result = requests.get(search).json().get('results')
        return "https://www.takealot.com/title/{0}".format(result.get('productlines')[0].get('id'))


