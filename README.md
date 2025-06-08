# GITBRIDGE_STARTER

This starter package provides a minimal Flask-based bridge between a personal GPT API and a local client.

## Setup

1. Install dependencies:

```bash
pip install flask requests
```

2. Create a `.env` file from `.env.example` and set your API credentials.

3. Run the server:

```bash
python app.py
```

4. Send a test message:

```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
```

## UID Tagging

This repo will be connected to AUTO+NETA reflex calls via UID anchors.
