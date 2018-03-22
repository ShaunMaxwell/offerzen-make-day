import requests
from config import PhonealotConfig

class Phone():

    def __init__(self):
        self.apikey = PhonealotConfig.DF_API_KEY

    def get_brands(self):
        response = requests.get('https://sandbox.root.co.za/v1/insurance/modules/root_gadgets/models',
                                auth=(self.apikey, ''))
        models = response.json()
        brands = set([phone['make'] for phone in models])
        return list(brands)
