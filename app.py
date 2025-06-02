from flask import Flask, request, jsonify
from flask_cors import CORS
from mistralai import Mistral

app = Flask(__name__)
CORS(app, origins=["https://deitybty.github.io"])  # 👈 allow requests from your frontend origin

client = Mistral(api_key="fmHSF8MVirIksFQG1CBwkymLxwKR0Btp")
model = "mistral-large-latest"

# @app.route('/chat', methods=['POST'])
# def chat():
#     data = request.get_json()
#     user_message = data.get("message", "")

#     if not user_message:
#         return jsonify({"reply": "No message provided"}), 400

#     response = client.chat.complete(
#         model=model,
#         messages=[{
#             "role": "user",
#             "content": user_message
#         }]
#     )

#     reply = response.choices[0].message.content
#     return jsonify({"reply": reply})

user_bio = """
Deity Basumatary is a passionate Physics researcher and educator from Assam, India. She holds a Master's degree in Physics from Cotton University with a specialization in Condensed Matter Physics, Thin Film Physics, and Nano Materials. Her master's thesis focused on synthesizing and analyzing the electrochemical properties of graphitic carbon nitride-polypyrrole nanocomposites for energy storage applications.
Deity is currently a Lecturer at Sijou Academy, where she teaches Physics to higher secondary students, fostering critical thinking and a strong scientific foundation. She also has prior experience running private tutoring classes and is known for her engaging teaching style and effective mentorship.
In addition to her academic and teaching pursuits, Deity has skills in programming (Python, C++), communication, and public speaking. She is also actively involved in extracurricular activities such as yoga, dance, and anchoring. She has participated in national-level workshops, including an IoT workshop at IIT Kharagpur.
Deity is fluent in English, Hindi, Assamese, and is a native Bodo speaker. She is deeply interested in the advancement of energy storage technologies and enjoys sharing her knowledge through talks and presentations on science and technology topics.
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
                "content": f"You are a helpful AI assistant who knows the following about the user:\n{user_bio}"
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

