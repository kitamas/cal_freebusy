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
                "text":{
                   "text":[
                      text
                   ]
                }
             },
             {
                "payload":{
                   "richContent":[
                      [
                         {
                            "type":"chips",
                            "options":[
                               {
                                  "text":"Chips 1",
                                  "image":{
                                     "src":{
                                        "rawUrl":"https://example.com/images/logo.png"
                                     }
                                  },
                                  "link":"https://example.com"
                               },
                               {
                                  "text":"Chips 2",
                                  "image":{
                                     "src":{
                                        "rawUrl":"https://example.com/images/logo.png"
                                     }
                                  },
                                  "link":"https://example.com"
                               }
                            ]
                         }
                      ]
                   ]
                }
             }
          ]
       }
    }

    return res

    app.run()
 