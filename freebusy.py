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
              "messages": [
      {
        "text": {
          "text": [
            "Üdvözlöm Vanda vagyok! Miben segíthetek?"
          ]
        },
        "platform": "FACEBOOK"
      },
      {
        "card": {
          "title": "card title",
          "subtitle": "subtitle",
          "imageUri": "https://dev.da.tsmcloud.hu/images/robot_icon.png",
          "buttons": [
            {
              "text": "button title"
            }
          ]
        },
        "platform": "FACEBOOK"
      },
      {
        "quickReplies": {
          "title": "quick 1"
        },
        "platform": "FACEBOOK"
      },
{
 "facebook":{
  "attachment":{
     "type":"template",
     "payload":{
        "template_type":"generic",
        "elements":[
           {
              "title":"Welcome!",
              "image_url":"https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png",
              "subtitle":"We have the right hat for everyone.",
              "default_action":{
                 "type":"web_url",
                 "url":"https://www.google.com/",
                 "webview_height_ratio":"tall"
              },
              "buttons":[
                 {
                    "type":"web_url",
                    "url":"https://www.google.com/",
                    "title":"View Website"
                 },
                 {
                    "type":"postback",
                    "title":"Start Chatting",
                    "payload":"DEVELOPER_DEFINED_PAYLOAD"
                 }
              ]
           },
               {
              "title":"Welcome!",
              "image_url":"https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png",
              "subtitle":"We have the right hat for everyone.",
              "default_action":{
                 "type":"web_url",
                 "url":"https://www.google.com/",
                 "webview_height_ratio":"tall"
              },
              "buttons":[
                 {
                    "type":"web_url",
                    "url":"https://www.google.com/",
                    "title":"View Website"
                 },
                 {
                    "type":"postback",
                    "title":"Start Chatting",
                    "payload":"DEVELOPER_DEFINED_PAYLOAD"
                 }
              ]
           },
               {
              "title":"Welcome!",
              "image_url":"https://upload.wikimedia.org/wikipedia/commons/7/70/Example.png",
              "subtitle":"We have the right hat for everyone.",
              "default_action":{
                 "type":"web_url",
                 "url":"https://www.google.com/",
                 "webview_height_ratio":"tall"
              },
              "buttons":[
                 {
                    "type":"web_url",
                    "url":"https://www.google.com/",
                    "title":"View Website"
                 },
                 {
                    "type":"postback",
                    "title":"Start Chatting",
                    "payload":"DEVELOPER_DEFINED_PAYLOAD"
                 }
              ]
           }
        ]
     }
     }
     }
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
    },
        "platform": "FACEBOOK"
    }
    ]
       }
    }
    return res

    app.run()
 