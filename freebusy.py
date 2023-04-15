# ChatGPT + Dialogflow CX + Heroku 
# https://www.youtube.com/watch?v=TrDFd4o9Kxg

import openai
import flask
import json
import os
from flask import send_from_directory, request, jsonify
import datetime
# from dotenv import load_dotenv


# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = "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"

# Flask app should start in global layout
app = flask.Flask(__name__)

app = flask(__name__)

@app.route('/dialogflow/cx/receiveMessage',methods=['POST'])

def cxReceiveMessage():

    try:

        data = request.get_json()
        # Use this tag property to choose the action
        # tag = data['fulfillmentInfo']['tag']

        query_text = data['text']

        print(query_text)

        result = text_completion(query_text)

        print(result)
        print(result['response'])

        if result['status'] == 1:
            return jsonify(
                {
                    'fulfillment_response': {
                        'messages': [
                            {
                                'text': {
                                    'text': [result['response']],
                                    'redactedText': [result['response']]
                                },
                            'responseType': 'HANDLER_PROMPT',
                             'source': 'VIRTUAL_AGENT'
                            }
                        ]
                    }
                }
            )

    except Exception as e:
            print(e)

            pass
#44

#61

def text_completion(prompt: str) -> dict:
    try:
        response = openai.Completion.create(
            model = 'text-davinci-003',
            prompt = f'Human: {prompt}\nAI: ',
            temperature = 0.8,
            max_tokens = 150,
            top_p = 1,
            frequency_penalty = 0,
            stop = ['Human:','AI:']
        )
        return {
            'status': 1,
            'response': response['choices'][0]['text']
        }
# 86
    except Exception as e:
        pass
# 92

if __name__ == '__main__':
    app.run(debug=True)


