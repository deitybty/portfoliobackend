# from flask import Flask, request, jsonify
# import requests

# app = Flask(__name__)

# API_URL = "https://api.mistral.ai/v1/chat/completions"
# API_KEY = "fmHSF8MVirIksFQG1CBwkymLxwKR0Btp" 

# @app.route("/chat", methods=["POST"])
# def chat():
#     user_msg = request.json.get("message")
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "model": "mistral-medium",  # Or mistral-small
#         "messages": [{"role": "user", "content": user_msg}]
#     }
#     response = requests.post(API_URL, json=payload, headers=headers)
#     result = response.json()
#     return jsonify({"reply": result["choices"][0]["message"]["content"]})



from flask import Flask, request, jsonify
from mistralai.client import Mistral
from mistralai.models.chat_completion import ChatMessage
import os

app = Flask(__name__)

# Set your API key here or from Render's environment variables
# API_KEY = os.environ.get("fmHSF8MVirIksFQG1CBwkymLxwKR0Btp", "your-api-key")  # Replace with your key for local testing
MODEL = "mistral-medium"  # Or use "mistral-large-latest"

client = Mistral(api_key="fmHSF8MVirIksFQG1CBwkymLxwKR0Btp")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    
    if not user_message:
        return jsonify({"reply": "No message provided"}), 400

    response = client.chat(
        model=MODEL,
        messages=[
            ChatMessage(role="user", content=user_message)
        ]
    )
    
    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

