from flask import Flask, request, jsonify
from flask_cors import CORS
from mistralai import Mistral

app = Flask(__name__)
CORS(app, origins=["https://deitybty.github.io"])  # 👈 allow requests from your frontend origin

client = Mistral(api_key="fmHSF8MVirIksFQG1CBwkymLxwKR0Btp")
model = "mistral-large-latest"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"reply": "No message provided"}), 400

    response = client.chat.complete(
        model=model,
        messages=[{
            "role": "user",
            "content": user_message
        }]
    )

    reply = response.choices[0].message.content
    return jsonify({"reply": reply})
