import flask
import json
import os
# import openai

from flask import send_from_directory, request

import requests

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
    print("REQ JSON DUMP")
    print(json.dumps(req, indent=4))

    gpt3 = req.get('sessionInfo').get('parameters').get('gpt3')
    print("GPT3 PARAMETER  = ",gpt3)
    # question = gpt3
    # temp = req.get('sessionInfo').get('parameters').get('temp')
    # temp_str = str(temp)

    # print("TEMP PARAMETER STR = ",temp_str)

    headers = {
    # 'Content-Type': 'application/json',
    'Authorization': 'Bearer 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'
    }

    json_data = {
    'model': 'text-davinci-002',
    'prompt': 'Say this is a test',
    'max_tokens': 6,
    'temperature': 0.3,
    'top_p':1,
    'frequency_penalty':0,
    'presence_penalty':0.3,
    'stop':["\n"],
    }


    response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=json_data)
    print("RESPONSE = ",type(response))
    #text = response.json()['text']

    text = response.json()
    print("TEXT = ",text)
    return text

    app.run()




