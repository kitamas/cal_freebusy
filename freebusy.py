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

    text = "*1 mdw*, **2 mdw**,  \n _3mdw_"

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
                   "text":"Pick a color:",
                   "quick_replies":[
                      {
                         "content_type":"text",
                         "title":"Red",
                         "payload":"Red color",
                         "image_url":" https://www.creativefabrica.com/wp-content/uploads/2019/05/Robot-icon-by-ahlangraphic-580x386.jpg"
                      },
                      {
                         "content_type":"text",
                         "title":"Green",
                         "payload":"Green color"
                      }
                   ]
                }
             }
          ]
       }
    } 



    """
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
                         }
                      ],
                      [
                         {
                            "type":"info",
                            "title":"Info item title, card clickable tts.mp3",
                            "subtitle":"Info item subtitle, robot.mp3",
                            "image":{
                               "src":{
                                  "rawUrl":"https://dev.da.tsmcloud.hu/images/robot_icon.png"
                               }
                            },
                            "actionLink":"https://dev.da.tsmcloud.hu/mp3/tts.mp3"
                         }
                      ],
                      [
                         {
                            "type":"description",
                            "title":"Description title",
                            "text":[
                               "This is text line 1",
                               "This is text line 2"
                            ]
                         }
                      ],
                      [
                         {
                            "type":"image",
                            "accessibilityText":"image",
                            "rawUrl":"https://www.creativefabrica.com/wp-content/uploads/2019/05/Robot-icon-by-ahlangraphic-580x386.jpg"
                         }
                      ],
                      [
                         {
                            "type":"button",
                            "icon":{
                               "type":"chevron_right",
                               "color":"#FF9800"
                            },
                            "text":"Button text",
                            "link":"https://example.com",
                            "event":{
                               "name":""
                            }
                         }
                      ],
                      [
                         {
                            "type":"chips",
                            "options":[
                               {
                                  "text":"robot",
                                  "image":{
                                     "src":{
                                        "rawUrl":"https://dev.da.tsmcloud.hu/images/robot_icon.png"
                                     }
                                  },
                                  "link":"https://dev.da.tsmcloud.hu/mp3/robot.mp3"
                               },
                               {
                                  "text":"yes",
                                  "image":{
                                     "src":{
                                        "rawUrl":"https://dev.da.tsmcloud.hu/images/yes.png"
                                     }
                                  },
                                  "link":"https://cloud.google.com/dialogflow/case-studies"
                               },
                               {
                                  "text":"no",
                                  "image":{
                                     "src":{
                                        "rawUrl":"https://dev.da.tsmcloud.hu/images/no.png"
                                     }
                                  },
                                  "link":"https://cloud.google.com/dialogflow/docs"
                               }
                            ]
                         }
                      ],
                      [
                         {
                            "type":"list",
                            "title":"List item 1 title",
                            "subtitle":"List item 1 subtitle",
                            "event":{
                               "name":""
                            }
                         },
                         {
                            "type":"divider"
                         },
                         {
                            "type":"list",
                            "title":"List item 2 title",
                            "subtitle":"List item 2 subtitle",
                            "event":{
                               "name":""
                            }
                         }
                      ],
                      [
                         {
                            "type":"accordion",
                            "title":"accordion title",
                            "subtitle":"accordion subtitle",
                            "text":"Lorem <img src=\"https://www.creativefabrica.com/wp-content/uploads/2019/05/Robot-icon-by-ahlangraphic-580x386.jpg\" width=\"38\"><a target=\"_blank\" href=\"https://dev.da.tsmcloud.hu/apisandbox.html\">DEV link</a> ipsum dolor sit amet.",
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
    } 
    """

    

    return res

    app.run()
 