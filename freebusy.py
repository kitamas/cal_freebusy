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
                      "text"
                   ]
                }
             },
             {
                "payload":{
                   "richContent":[
                      [
                         {
                            "title":"Description title",
                            "type":"description",
                            "text":[
                               "This is text line 1",
                               "This is text line 2"
                            ]
                         },
						 {
                            "title":"Description title",
                            "type":"description",
                            "text":[
                               "This is text line 1",
                               "This is text line 2"
                            ]
                         },
						 {
                            "type":"chips",
                            "options":[
                               {
                                  "text":"AI csapat",
                                  "image":{
                                     "src":{
                                        "rawUrl":"https://dev.da.tsmcloud.hu/images/icon1.png"
                                     }
                                  },
                                  "link":"https://dev.da.tsmcloud.hu/"
                               },
                               {
                                  "text":"Telekom",
                                  "image":{
                                     "src":{
                                        "rawUrl":"https://dev.da.tsmcloud.hu/images/icon2.png"
                                     }
                                  },
                                  "link":"https://www.telekom.hu/"
                               }
                            ]
                         },
						 {
    "facebook": {
    "attachment": {
      "type": "template",
      "payload": {
        "elements": [
          {
            "title": "More",
            "buttons": [
              {
                "title": "more",
                "payload": "more",
                "type": "postback"
              }
            ],
            "subtitle": "",
            "image_url": "https://i.imgur.com/sI1VUsV.jpg"
          }
        ],
        "template_type": "generic"
      }
    }
    }
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
 