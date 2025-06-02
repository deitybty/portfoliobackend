from flask import Flask, request, jsonify
from flask_cors import CORS
from mistralai import Mistral

app = Flask(__name__)
CORS(app, origins=["https://deitybty.github.io"])

client = Mistral(api_key="fmHSF8MVirIksFQG1CBwkymLxwKR0Btp")
model = "mistral-large-latest"

deity_bio = """
Deity Basumatary is a Physics researcher and educator from Assam, India. 
She holds an M.Sc. in Physics from Cotton University, specializing in Condensed Matter Physics, Thin Film Physics, and Nano Materials. 
Her research focuses on energy storage materials, particularly graphitic carbon nitride-polypyrrole nanocomposites. 
Deity is currently a Lecturer at Sijou Academy, where she teaches Physics to senior secondary students.

She is also skilled in Python and C++, and actively participates in extracurricular activities such as yoga, dance, anchoring, and scientific talks. 
She is fluent in English, Hindi, Assamese, and Bodo. Deity has presented talks on energy storage and virtual reality, and has participated in workshops including an IoT session at IIT Kharagpur.
"""




@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"reply": "No message provided"}), 400

    response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "system",
                "content": f"You are a helpful assistant. You have general world knowledge, and you also know specific details about Deity Basumatary:\n{deity_bio}\nUse this info when asked about her, otherwise answer generally."
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    reply = response.choices[0].message.content
    return jsonify({"reply": reply})
