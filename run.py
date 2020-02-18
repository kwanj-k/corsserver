import json
import os
import requests
from flask import Flask, request
from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello  World!"


@app.route('/location/')
@cross_origin()
def get_location():
    url = request.args.get('url') +'&key=' + os.getenv('GOOGLE_API_KEY')
    response = json.loads(requests.get(url).content)
    return response

@app.route('/weather/')
@cross_origin()
def get_weather():
    url = request.args.get('url')
    response = json.loads(requests.get(url).content)
    return response

if __name__ == '__main__':
    app.run()
