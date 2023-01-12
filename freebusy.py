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
                            "type":"chips",
                            "options":[
                               {
                                  "text":"AI csapat",
                                  "image":{
                                     "src":{
                                        "rawUrl":"https://dev.da.tsmcloud.hu/var/www/images/icon1.png"
                                     }
                                  },
                                  "link":"https://dev.da.tsmcloud.hu/"
                               },
                               {
                                  "text":"Telekom",
                                  "image":{
                                     "src":{
                                        "rawUrl":"https://dev.da.tsmcloud.hu/var/www/images/icon2.png"
                                     }
                                  },
                                  "link":"https://www.telekom.hu/"
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
    }

    return res

    app.run()
 