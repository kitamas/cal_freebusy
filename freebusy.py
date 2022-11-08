import requests

cookies = {
    'secret ': ' contemporary',
}

headers = {
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    # 'Cookie': 'secret = contemporary',
}

json_data = {
    'data': 'Ki nyer ma',
    'topk:': '0',
    'temp': '.1',
}

response = requests.post('https://polka.nytud.hu/tcom/gpt3/', cookies=cookies, headers=headers, json=json_data)