from flask import Flask
from flask import render_template
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/api/cats/')
def catFacts():
  resp = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1')
  return json.loads(resp.text)