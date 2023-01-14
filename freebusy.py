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
                        "Response facebook"
                    ]
                },
                "platform": "FACEBOOK"
            },
             {
                "payload":{
                   "richContent":[
                      [
                         {
                            "type":"chips",
                            "options":[
                               {
                                  "text":"Start over"
                               }
                            ]
                         }
                      ]
                   ]
                }
             },
             {
                "payload":{
    {
    "facebook": {
    "attachment": {
      "type":"template",
      "payload":{
        "template_type":"generic",
        "elements":[
           {
            "title":"Your first payload",
            "image_url":"https://i.imgur.com/MgSrTnB.gif",
            "subtitle":"you are welcome.",
            "default_action": {
              "type": "web_url",
              "url": "https://www.google.com"
            },
            "buttons":[
              {
                "type":"web_url",
                "url":"https://telegram.org/",
                "title":"button 1"
              },{
                "type":"web_url",
                "url":"https://medium.com",
              "title":"button 2"
              },{
                "type":"web_url",
                "url":"https://emojipedia.org",
                "title":"button 3"
              }              
            ]      
          }
        ]
      }
    }
    }
    }
                }
             }	 
          ]
       }
    }

    return res

    app.run()
 