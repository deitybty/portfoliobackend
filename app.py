# from flask import Flask, request, jsonify
# from mistralai import Mistral
# import os

# app = Flask(__name__)


# model = "mistral-large-latest"


# client = Mistral(api_key="fmHSF8MVirIksFQG1CBwkymLxwKR0Btp")

# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.get_json()
#     user_message = data.get("message", "")
    
#     if not user_message:
#         return jsonify({"reply": "No message provided"}), 400

#     response = client.chat(
#         model=model,
#         messages=[
#             ChatMessage(role="user", content=user_message)
#         ]
#     )
    
#     reply = response.choices[0].message.content
#     return jsonify({"reply": reply})




from flask import Flask, request, jsonify
from mistralai import Mistral

app = Flask(__name__)

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
