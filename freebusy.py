# FLASK = = = = = = = = = = = 
import flask
import json
import os
from flask import send_from_directory, request
import datetime
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

# https://cloud.google.com/dialogflow/cx/docs/concept/agents-prebuilt#financial-services

# Flask app should start in global layout
app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')


@ app.route('/webhook', methods = ['GET', 'POST'])
def webhook():

    text = " *bold*  \n **mdw** _italic_ [link](https://facebook.com) "

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
                "in_hours" : 'true',
                "card_verified" = 'true'
            }
        }
    }

    return res

    app.run()

""" 
def cxPrebuiltAgentsFinServ(request):
    print('Cloud Function:', 'Invoked cloud function from Dialogflow')
    req_data = request.get_json()
    tag = req_data['fulfillmentInfo']['tag']

    if tag:
        # BEGIN validateAccount
        if tag == 'validateAccount':
            print(tag + ' was triggered.')
            card_last_four = req_data['sessionInfo']['parameters']['card_last_four']

            # card validation only fails if card number is 0000
            if card_last_four == '0000':
                card_verified = 'false'
            else:
                card_verified = 'true'

            return json.dumps(
                {"sessionInfo": {"parameters": {"card_verified": card_verified}}}), 200

        # BEGIN checkInHours
        elif tag == 'checkInHours':
            print(tag + ' was triggered.')

            # check if we are currently in hours
            current_date = datetime.now()
            print('current time is ' + str(current_date))

            current_hour = current_date.hour
            print('current hour is ' + str(current_hour))
            if current_hour >= 8 and current_hour <= 20:
                in_hours = 'true'
                print('currently in hours')
            else:
                in_hours = 'false'
                print('currently out of hours')

            return json.dumps(
                {"sessionInfo": {"parameters": {"in_hours": in_hours}}}), 200

    return 'OK', 200
"""