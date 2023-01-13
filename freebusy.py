# FLASK = = = = = = = = = = = 
import flask
import json
import os
from flask import send_from_directory, request
# FLASK = = = = = = = = = = = 

# CRED = = = = = = = = = = =
import googleapiclient.discovery
from google.oauth2 import service_account as google_oauth2_service_account
# CRED = = = = = = = = = = =

# QUICKSTART = = = = = = = = = = =
import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# QUICKSTART = = = = = = = = = = =

# Flask app should start in global layout
app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')


@ app.route('/webhook', methods = ['GET', 'POST'])
def webhook():

    text = "*1 markdown text*, **2 markdown text**, 3 markdown text  \n"

    res = {
       "fulfillment_response":{
          "messages":[
      {
        "text": {
          "text": [
            " *1 markdown text*, **2 markdown text**, 3 markdown text  \n Üdvözlöm Vanda vagyok! Miben segíthetek?"
          ]
        }
      },
	               {
                "payload":{    
	  "facebook": {
    "text": "Welcome to my agent!",
    "quick_replies": [
      {
        "title": "reply 1",
        "content_type": "text",
        "payload": "reply1"
      }
    ]
    }
	}
             }
          ]
    }
    }

    return res

    app.run()
 