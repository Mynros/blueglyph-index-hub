# blueglyph-index-hub

This repository contains example resources for building a small portal that connects to a personal GPT API. The following guide explains how to set up a simple Flask server that accepts user messages and forwards them to a GPT model.

## Flask Example

Below is a minimal Flask application (`app.py`) that exposes an endpoint to relay messages to your GPT service. It assumes you have a personal GPT API that accepts a JSON payload with a `message` field and returns a JSON response with a `reply` field.

```python
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
```

Save this file as `app.py` in your project directory.

## Setup Steps

1. **Install dependencies**

   Ensure you have Python 3 installed. Then run:

   ```bash
   pip install flask requests
   ```

2. **Configure API keys**

   Set the following environment variables so the server can communicate with your GPT service:

   - `GPT_API_URL` – the endpoint for your personal GPT API
   - `GPT_API_KEY` – your API key for authentication

   For example, you can create an `.env` file or export them in your shell:

   ```bash
   export GPT_API_URL="https://your-gpt-service/chat"
   export GPT_API_KEY="your-api-key"
   ```

3. **Run the server**

   Start the Flask app with:

   ```bash
   python app.py
   ```

   The server will listen on `http://localhost:5000/chat`.

## Sending Messages

Send a POST request with a JSON payload containing `message` to the `/chat` endpoint:

```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
```

The server relays the message to your GPT API and returns the model's reply.

