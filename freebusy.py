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


@app.route('/authentication')

def authentication():
    creds = google_oauth2_service_account.Credentials.from_service_account_info(
    {
  "type": "service_account",
  "project_id": "my-project-90818-learn-hun",
  "private_key_id": "cf8bd4105633c3cac528d1c8c4c66cc3b825e837",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCeQrDkS5Rq/khX\nNoU01bLEbZHj/JjzwlcozMB0uRP+H9NYJytYrl4+vqhi3+EApY+bKpU/iB/A9tPC\nVIYjhXeACCXtNq6sz8hQDN6y+cKW5K4i2yd1xpeIlAXjo4M/uRIarlffgEi3MOAX\nRtTDskXvECuu2rXsIbgQEBzpCwJQhaVWnOHk4ONTJnEKSjvtuHXRZUc6GrabLrLU\nb4h1nDYh8+IVoUxpcZg0sW9XWpXw2O3kh8o6ADy4aH2KB9Sv4yktLLNcVWrqisei\nekA93NnWji5pG2DKuqjrmaZGA9SwOA5gT34EfrbL8zVFaEGgV7yp5ytrTg5vmtaw\nP36j58iJAgMBAAECggEAG5iV900NjYWXECwX2LFtuW5AuwBEHHc2Ew12/rN6Hr0m\ncW/tEUrgcLD2tD0FI0N7UcuAWGJwZQm1PaTW+hEvGAJzuJQpK8WUkI7Z81v1WDH6\ngmX0EMenC0ACceIEhCNNmpztgjHAnD73yF9HwPMQWkIX1+bXw5vSmGxy2hkbF3ac\nKehAlVB584QC8L191WtWPpx27pdNy2ncnlW6Xaail8NtGlCELLGrmicQUjgxZhsU\ngEZh/ZrTYm4ion5mWCYtbSvuXN++9Zy6kIdpYiFOroQuEr48L6l0KLmVvNsuZ1D0\nk4xdXJxtx0kacGr0tyg1VV3vut14vcSlDqbeDUy7DQKBgQC/5LuQVTJT3FiJ13sb\nCyJIuFVQAX2p1+TXsiKJh9Copaua0tvXygJtbGFEVmYKS3VwiC8OyESQQhATFORE\nYZYpek0UwhNggekg+asiMMSnPc/hHkxQdsxmT34sfmuooSeDvqrVPw6BW3i7Hb6Q\nB7lfydH+v6VejPKWm2q7sm6UpQKBgQDTIZJ/rdgknqnIENgcHwRJoKS3j2RcCvnK\nu0pXoumA9xq1/JFOCuGmRnscyga0d17fYGpER3iR5NL2YAksMSUEDyj+yFupHyfS\nTZzVVaeYNW3OKjDXwUDGYh2D3JkF7P6zeC9LLBkvwuhllvwC1URewWARBpreVGpH\nuZGRo6CLFQKBgHnO9yTif+TtzSIKr3F2OtgQcs8rcxpaGkC1KelFVjWHnIvV54lu\nCOZu0rtvYKyOQ8kgGUb351XvKYcDTvb9PzWrFbzkiSpMrLCq62/zpxFGUmvjMKwv\nDQaw1TXnNe3ABnZBlO1yboG8j8GvWuTQkmJ0mSFtg8qmC+OAWls1I66lAoGAZCvL\njBR5Nnao6ylCv6Tfrecv/39jCGCUv2E5FndO/kc/PxUEA9kZ0oAiLTiVEc6JDsZ5\n5MdcJyxAA3DxKSxv+YsP0kJRat5DUH5OaNFo4MiIvoY6AkPIbddjVYq2d59IAPKG\nzc2wbX62MG0ASH/THnn1EF7n35CBlGIw9L6DjzkCgYEAu0LhdTHuuM6DOAfh4ohw\n0oj2770Dyw0vQImp+4qbdocLqXIVOZYEIywGfi+OLuSxrSYsw2BuTAPAtIEmkuHx\n4cvV/XxcWWPY30B4Z2irOBIsIXJjfAO/DyCyDaX7Cmoy+NgoCwRSRzDeOiQ7ysw8\nhwrS/OoTx3BhHYJt+NO6qIM=\n-----END PRIVATE KEY-----\n",
  "client_email": "appointment-scheduler@my-project-90818-learn-hun.iam.gserviceaccount.com",
  "client_id": "115405775326578876255",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/appointment-scheduler%40my-project-90818-learn-hun.iam.gserviceaccount.com"
    },
    scopes=['https://www.googleapis.com/auth/calendar'],
    subject='appointment-scheduler@my-project-90818-learn-hun.iam.gserviceaccount.com'
    )
    return creds

@app.route('/webhook', methods=['GET','POST'])
def webhook():

    text = "*1 markdown text*, **2 markdown text**, 3 markdown text  \n"

    res = {
       "fulfillmentText":"dfmessenger fulfillmentText",
       "fulfillmentMessages":[
          {
             "text":{
                "text":[
                   "dfmessenger fulfillmentMessages"
                ]
             }
          },
          {
             "payload":{
                "richContent":[
                   [
                      {
                         "type":"info",
                         "title":"Info item title, card clickable tts.mp3",
                         "subtitle":"Info item subtitle, robot.mp3",
                         "image":{
                            "src":{
                               "rawUrl":"https://elearning.dev.unideb.hu/moodle37/webservice/moodlebot/robot_icon.png"
                            }
                         },
                         "actionLink":"https://elearning.dev.unideb.hu/moodle37/webservice/moodlebot/tts.mp3"
                      }
                   ]
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
                      }
                   ]
                ]
             }
          },
          {
             "payload":{
                "richContent":[
                   [
                      {
                         "type":"image",
                         "accessibilityText":"image",
                         "rawUrl":"https://www.creativefabrica.com/wp-content/uploads/2019/05/Robot-icon-by-ahlangraphic-580x386.jpg"
                      }
                   ]
                ]
             }
          },
          {
             "payload":{
                "richContent":[
                   [
                      {
                         "link":"https://elearning.dev.unideb.hu/moodle37/webservice/moodlebot/robot.mp3",
                         "text":"BUTTON link /robot.mp3",
                         "icon":{
                            "type":"link",
                            "color":"#FF9800"
                         },
                         "type":"button"
                      }
                   ]
                ]
             }
          },
          {
             "payload":{
                "richContent":[
                   [
                      {
                         "type":"button",
                         "icon":{
                            "type":"chevron_right",
                            "color":"#FF9800"
                         },
                         "text":"Button event, parameter",
                         "link":"https://",
                         "event":{
                            "name":"",
                            "languageCode":"",
                            "parameters":{
                               "param1":"1"
                            }
                         }
                      }
                   ]
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
                               "text":"robot",
                               "image":{
                                  "src":{
                                     "rawUrl":"https://elearning.dev.unideb.hu/moodle37/webservice/moodlebot/robot_icon.png"
                                  }
                               },
                               "link":"https://elearning.dev.unideb.hu/moodle37/webservice/moodlebot/robot.mp3"
                            },
                            {
                               "text":"yes",
                               "image":{
                                  "src":{
                                     "rawUrl":"https://elearning.dev.unideb.hu/moodle37/webservice/moodlebot/yes.png"
                                  }
                               },
                               "link":"https://cloud.google.com/dialogflow/case-studies"
                            },
                            {
                               "text":"no",
                               "image":{
                                  "src":{
                                     "rawUrl":"https://elearning.dev.unideb.hu/moodle37/webservice/moodlebot/no.png"
                                  }
                               },
                               "link":"https://cloud.google.com/dialogflow/docs"
                            }
                         ]
                      }
                   ]
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
                "richContent":[
                   [
                      {
                         "subtitle":"list item 1 subtitle",
                         "title":"list item 1 title",
                         "type":"list",
                         "event":{
                            "parameters":{
                               "param2":"prm2"
                            },
                            "name":"WELCOME",
                            "languageCode":"en"
                         }
                      },
                      {
                         "type":"divider"
                      },
                      {
                         "subtitle":"list item 2 subtitle",
                         "title":"list item 2 title",
                         "type":"list",
                         "event":{
                            "parameters":{
                               
                            },
                            "name":"PARALELL",
                            "languageCode":"en"
                         }
                      }
                   ]
                ]
             }
          },
          {
             "payload":{
                "richContent":[
                   [
                      {
                         "subtitle":"accordion subtitle",
                         "type":"accordion",
                         "title":"accordion title",
                         "text":"Lorem <img src=\"https://www.creativefabrica.com/wp-content/uploads/2019/05/Robot-icon-by-ahlangraphic-580x386.jpg\" width=\"38\"><a target=\"_blank\" href=\"https://moodle.org\">Moodle link</a> ipsum dolor sit amet.",
                         "image":{
                            "src":{
                               "rawUrl":"https://www.creativefabrica.com/wp-content/uploads/2019/05/Robot-icon-by-ahlangraphic-580x386.jpg"
                            }
                         }
                      }
                   ]
                ]
             }
          }
       ]
    }

	
"""
    res = {
        "fulfillment_response": {
            "messages": [
                {
                    "text": {
                        "text": [
                            text
                        ]
                    }
                }
            ]
        },
        "session_info": {
            "session" : "session_name",
            "parameters": {
                "event_id" : "event_id"
            }
        }
    }
"""

    return res

# app.run()