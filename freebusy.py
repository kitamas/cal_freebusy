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

    dt_parameter1 = "2022,10,01,0,0"
    #dt_parameter2 = "2022,10,30,24,0"

    dt_str_date1 = datetime.datetime.strptime(dt_parameter1, '%Y,%m,%d,%H,%M')
    #dt_str_date2 = datetime.datetime.strptime(dt_parameter2, '%Y,%m,%d,%H,%M')

    start_parameter = dt_str_date1

    #start = start_parameter.isoformat("T", "seconds")
    start = start_parameter.isoformat() + 'Z'

    #end = (start_parameter + datetime.timedelta(hours=24)).isoformat("T", "seconds")
    end = (start_parameter + datetime.timedelta(days=24)).isoformat() + 'Z'

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