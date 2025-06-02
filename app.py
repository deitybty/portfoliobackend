from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_URL = "https://api.mistral.ai/v1/chat/completions"
API_KEY = "fmHSF8MVirIksFQG1CBwkymLxwKR0Btp" 

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistral-medium",  # Or mistral-small
        "messages": [{"role": "user", "content": user_msg}]
    }
    response = requests.post(API_URL, json=payload, headers=headers)
    result = response.json()
    return jsonify({"reply": result["choices"][0]["message"]["content"]})
