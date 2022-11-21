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

    text = ask()

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


def ask(question,chat_log=None):

    req = request.get_json(force=True)
    print("REQ JSON DUMP")
    print(json.dumps(req, indent=4))

    gpt3 = req.get('sessionInfo').get('parameters').get('gpt3')
    print("GPT3 PARAMETER  = ",gpt3)
    question = gpt3
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


    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine = davinci,
        prompt = prompt_text,
        max_tokens=45,
        temperature=0.3,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3,
        stop=["\n"],
    )
    story = response["choices"][0]["text"].strip(" \n")
    return str(story)

    print("STORY = ",story)

    #data = '{"data":"' + gpt3 + '","topk:":"0","temp":"' + temp_str + '"}'
    #data = data.encode('utf-8')
    #response = requests.post('https://polka.nytud.hu/tcom/gpt3/', headers=headers, cookies=cookies, data=data)
    # text = response.json()['text']
    # print("TEXT = ",text)

def append_interaction_t_chat_log(question,answer,chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'

    app.run()




