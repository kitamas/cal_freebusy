import flask
import json
import os
from flask import send_from_directory, request

import requests
import locale

# Flask app should start in global layout
app = flask.Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/favicon.png')

@app.route('/')


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

    req = request.get_json(force=True)
    print(json.dumps(req, indent=4))

    gpt3_latin1 = req.get('sessionInfo').get('parameters').get('gpt3')
    #gpt3_utf = gpt3_latin1.decode('iso-8859-1').encode('utf8')
    #print("gpt3 parameter UTF = ",gpt3_utf)
    gpt3 = gpt3_latin1

    temp = req.get('sessionInfo').get('parameters').get('temp')
    temp_str = str(temp)
    print("temp parameter str = ",temp_str)

    cookies = {
    'secret': 'contemporary',
    }

    headers = {
    'Content-Type': 'application/json',
    }

    # data = '{"data":"Ki nyer ma","topk:":"0","temp":".1"}'
    # data = '{"data":"' + gpt3 + '","topk:":"0","temp":".1"}'
    data = '{"data":"' + gpt3 + '","topk:":"0","temp":"' + temp_str + '"}'

    print("data =",data)
    #response = requests.post('https://polka.nytud.hu/tcom/gpt3/', headers=headers, cookies=cookies, data=data)
    response = requests.post('https://polka.nytud.hu/tcom/gpt3/', headers=headers, cookies=cookies, data=data.encode('utf-8'))
    print(response.json())

    text = response.json()['text']
    print("text = ",text)

    return text

    app.run()






