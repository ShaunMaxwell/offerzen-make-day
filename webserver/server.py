import logging

from flask import Flask, json, request

app = Flask(__name__)
logger = logging.getLogger(__name__)


@app.route("/")
def hello():
    return "Hello World!"


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


def serve():
    app.run(host='0.0.0.0')
