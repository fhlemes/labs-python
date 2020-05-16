import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class Development(object):
  DEBUG = True
  TESTING = False

app_config = {
  "development": Development
}