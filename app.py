from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)
GPT_API_URL = os.environ.get("GPT_API_URL")
GPT_API_KEY = os.environ.get("GPT_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message')
    if not message:
        return jsonify({'error': 'Missing message'}), 400

    headers = {'Authorization': f'Bearer {GPT_API_KEY}'}
    payload = {'message': message}
    gpt_response = requests.post(GPT_API_URL, json=payload, headers=headers)
    if gpt_response.status_code != 200:
        return jsonify({'error': 'GPT API error'}), gpt_response.status_code

    reply = gpt_response.json().get('reply')
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(port=5000)
