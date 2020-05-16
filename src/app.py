  
#src/app.py
import requests
from flask import Flask

from .config import app_config
from flask import request, json, Response, Blueprint, g

from datetime import date

def create_app(env_name):
  
  # app initiliazation
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])
  
  # Route default
  @app.route('/', methods=['GET'])
  def index():

    # date today - 
    data = date.today()

    # format date default BR - d/m/YYYY
    data_pt = "{}/{}/{}".format(data.day, data.month, data.year)

    # format date with strftime
    data_pt1 = data.strftime("%d/%m/%Y")

    # request 
    digital = requests.get("https://api.digitalocean.com/v2/")

    result = [{
      "dataDefault": data,
      "dataBR": data_pt,
      "dataFormatada": data_pt1,
      "do": digital.json()
    }]

    message = {'success': 'Welcome phyton api', "data": result}
    return custom_response(message, 200)

  # Verify age
  @app.route('/<int:idade>', methods=['GET'])
  def getAge(idade):
    permitted = 18
    user = idade

    if permitted >= user :
      message = {'error': 'Minor age'}
      return custom_response(message, 403)
    else :
      message = {'success': 'Major age'}
      return custom_response(message, 200)

  return app

def custom_response(res, status_code):

  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )