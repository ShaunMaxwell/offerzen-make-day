import logging
from phone import Phone
from flask import Flask, json, request

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route("/", methods=['POST'])
def hello():
    function = request.get_json().get("result").get("action").lower()
    if "brand" in function:
        return get_brands()
    elif "model" in function:
        return get_models()
    elif "pdp" in function:
        return get_plid()
    else:
        response = app.response_class(
        response=json.dumps("hello world"),
        status=200,
        mimetype='application/json')
        return response


@app.route("/make_name", methods=['POST'])
def make_name():
    parameters = request.get_json().get("result").get("parameters")
    number = parameters.get("number")
    color = parameters.get("color")
    name = "Alright, your silly name is {} {}! I hope you like it. See you next time.".format(color.capitalize(),
                                                                                              number)
    result = {'speech': name,
              'displayText': name}

    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/get_brands", methods=['POST'])
def get_brands():
    """
    gets list of phones from root API
    :return: list of supported phone models
    """
    phone = Phone()
    brands = phone.get_brands()
    text = "Sure! Here are the available brands:\n " \
           "{0}\n" \
           "What do you want?".format(brands)


    result = {'speech': text, 'displayText': text}
    # print result

    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/get_models", methods=['POST'])
def get_models():
    parameters = request.get_json().get("result").get("parameters")
    brand = parameters.get('brand')
    # print brand
    phone = Phone()
    models = phone.get_models_by_brand(brand)
    text = "Here are the available models for {0}:\n{1}".format(brand,models)
    result = {'speech': text, 'displayText': text}
    # print result
    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route("/get_plid", methods=['POST'])
def get_plid():
    p = Phone()
    parameters = request.get_json().get("result").get("parameters")
    print request.get_json().get("result").get('contexts')
    try:
        brand = request.get_json().get("result").get('contexts')[3].get("parameters").get("brand")
    except:
        brand = "Samsung"

    print "selected brand = {0}".format(brand)
    model_number = parameters.get('number', 0)
    if type(model_number) != int :
        model_number = int(parameters.get('number', 0).encode('ascii'))

    models = p.get_models_by_brand(brand)

    selected = models[model_number]
    print selected
    plid = p.get_plid(brand, selected)
    print plid
    result = {'speech': plid, 'displayText': plid}
    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    return response


def serve():
    app.run(host='0.0.0.0')
