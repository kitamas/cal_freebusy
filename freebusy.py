import flask
import json
import os
import openai

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
    # temp = req.get('sessionInfo').get('parameters').get('temp')
    # temp_str = str(temp)

    # print("TEMP PARAMETER STR = ",temp_str)

    cookies = {
    'secret': '',
    }
    # 'secret': 'contemporary',

    headers = {
    'Content-Type': 'application/json',
    }

    OPENAI_API_KEY = "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"
    COMPLETIONS_MODEL = "text-davinci-002"

    openai.api_key = os.getenv("OPENAI_API_KEY")

    """
    openai.Completion.create(
        model=COMPLETIONS_MODEL,
        prompt="Hello world",
        max_tokens=6,
        temperature=0.3,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )["choices"][0]["text"].strip(" \n")
    """
    completion = openai.Completion.create(engine="text-davinci-002", prompt="Hello world")

    # print the completion
    print(completion.choices[0].text)

        # prompt=prompt,
        # model="text-davinci-002",

    #data = '{"data":"' + gpt3 + '","topk:":"0","temp":"' + temp_str + '"}'
    #data = data.encode('utf-8')

    #response = requests.post('https://polka.nytud.hu/tcom/gpt3/', headers=headers, cookies=cookies, data=data)

    text = response.json()['text']
    print("TEXT = ",text)

    return text

    app.run()




