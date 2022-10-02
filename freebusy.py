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

@app.route('/')
@app.route('/home')
def home():
    return "Hello World"

@app.route('/authentication')

def authentication():
    creds = google_oauth2_service_account.Credentials.from_service_account_info(
    {
  "type": "service_account",
  "project_id": "my-project-90818-learn-hun",
  "private_key_id": "5af4d0f2630d0c5701bbd094a4245c4d336396a7",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDk76CnM/T/6sGI\n0S1UaK/mE0mSiVeZIY+KKsCn01mrdcVttTcyJPkgy8bBv9idWITlQbRGaAOgLudy\nTVbqHb0ma99koIBf2HI67z6fzMPJOw4q1VqG550Bj933v/GON8exdM2zr9HvaLXJ\nmTCloOwbV91O0O57X1uVBVz9oAZCLrJhPaHRKq2zr7asH5VgyX3eX772d1MCA3pS\ntyXbMVMXDdKji06FjV2ctRUVszr2zE2lcqtV4GVXlrUAKy9IOBbdRGkeVBW82qXz\nNCRXXkuLsRjd7JLawhHsKgpjAJLQBTKkvgfWggYtSV4VynsEDG8a3321SGphTgI0\ns4lgiiGpAgMBAAECggEAAuH+lqRpmSBiY//oT3gLAP1sr37xvrCkv1Nm/iYD6swO\nmqFNyuCaz34paE6rYl3XPJDNfZZ5Nzbn/LE7HzMVKurwUvLPcwWFeLcDBZ2dOIc5\nGDJ8E5dOi5K9c41z8/vBVLt5DKJx5Q8fPOTkLy2902FRnNi2LBEJFPEOmPX/Ji2s\nwQD9qhRmEDMOQBiEWTTE0gPoISYp062QcIc30SHItdNdo0iNuz3SK1yq7Fq2vDMS\nUYK0YuSTmxu2NGw5kSFY9mKCbRwCDnTvc74PLvmqIxm0DTkiySNVCx1lAs5h3Gaz\n2Qw4osX3CIotoKAaMf6FuFgR/f+elF0uBZ+JCt1HNQKBgQD7D1/NwUFOuB0N6pq3\n+NNy0seqZmpibBr5Pjerzqf9ZrBk6VCR2VA/cjmzk28npd0bzaTZZ709ncbpidXG\n1+Yfy6y4j24pSULKcXHeS6up0OZzaJgyghbhOQ0RE5d/NhvS2quSXM/YaIaVzQdN\nBdh1ZZNKrmtwe5Cd2JWmFWwUTQKBgQDpcM+9PWpLy/8Xw4esjnfbfsQpo7xK+7DJ\nBRf+FuWrvOejWOtlfXVe8WBhvBPPaEKOzXt91VUFi6WqErNnjZV7/6/KHRJjHg46\n/wCSMPhQ/jvnKvnymj3JB1qqnCSLy/2dmTFYZR0HOUGbIdZkBFb2ajbsWvkGnwJf\nEeGn62VgzQKBgQDJd2Hq7A0rTWXLWBtGTL/p4almXX87cgMHRd1I2rJGD9S3dd84\n2wmhkFkreMF3MIvJlvGVoMDkpCsOF5TcVz6M/1WgWUEOkoKtj/HPcCvWPxPfQuz3\ngxs3KyAINw+YfuQ/BUkvT5le0SpHJduY/HriYlubT3JaNl4rvLUCLSio9QKBgQCj\nM8Vorhk0aKgs+vxNfUT6ZYPLALfRTGlqAG+nqmZjTKw9HRtlVvLJr8MMUSsgY+m0\nYKAndw/70oe9gVl/2hJaIIXLrct/FDIquMCzdB0Gstc6ZGdeXss3Ujbm9EbwnWrv\n1XwUKozC0hq11FBImGgb2mIPmAJlyKElyiCS/xVfOQKBgH+Djwz8TPUIibKIK/cZ\nLgQWi7OmU5q7waRlYFEXa86qx1XhfNZI0hdDKQGFm6/E7xvlYfsvaxy3mWt2H7aP\nT395BTGaOvd1iMJc+KKG7/0dwsF9TNe2bLayukYn1pv/sax/CDMe9nWAWz47LyuH\ni5DwBThM9ioEUpec0sYCjl8B\n-----END PRIVATE KEY-----\n",
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

    text = main()

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

    return res

def main():

    creds = authentication()
    service = build("calendar", "v3", credentials=creds)

    req = request.get_json(force=True)
    print("REQ")
    print(json.dumps(req, indent=4))

    #d = datetime.datetime.now().date()
    #today = datetime.datetime(d.year, d.month, d.day, 10)+datetime.timedelta(hours=1)
    #2022-09-25 11:00:00
    #start = today.isoformat("T", "seconds")

    dt_parameter1 = "2022,9,30,0,0"
    #dt_parameter2 = "2022,9,30,24,0"

    dt_str_date1 = datetime.datetime.strptime(dt_parameter1, '%Y,%m,%d,%H,%M')
    #dt_str_date2 = datetime.datetime.strptime(dt_parameter2, '%Y,%m,%d,%H,%M')

    start_parameter = dt_str_date1

    #start = start_parameter.isoformat("T", "seconds")
    start = start_parameter.isoformat() + 'Z'

    #end = (start_parameter + datetime.timedelta(hours=24)).isoformat("T", "seconds")
    end = (start_parameter + datetime.timedelta(hours=24)).isoformat() + 'Z'

    #datetime1 = datetime.datetime(2022, 09, 29, 0, 0).isoformat("T", "seconds")
    #datetime2 = datetime.datetime(2022, 09, 29, 24, 0).isoformat("T", "seconds")

    body = {
            "timeMin": start,
            "timeMax": end,
            "timeZone": 'Europe/Budapest',
            "items": [{"id": '61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com'}]
           }

    event_result = service.freebusy().query(body=body).execute()

    print("EVENT RESULT")
    print(json.dumps(event_result, indent=4))

    text = str(event_result['calendars']['61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com']['busy'])

    return text

    app.run()

"""
{
  "kind": "calendar#freeBusy",
  "timeMin": "2022-09-29T00:00:00.000Z",
  "timeMax": "2022-09-30T00:00:00.000Z",
  "calendars": {
    "61u5i3fkss34a4t50vr1j5l7e4@group.calendar.google.com": {
      "busy": [
        {
          "start": "2022-09-29T16:00:00+02:00",
          "end": "2022-09-29T17:00:00+02:00"
        },
        {
          "start": "2022-09-29T18:00:00+02:00",
          "end": "2022-09-29T19:00:00+02:00"
        }
      ]
    }
  }
}
"""