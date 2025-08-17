from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import requests
from datetime import timedelta

# Replace this with your actual Together API key
TOGETHER_API_KEY = "tgp_v1_irCLU1AW7N9Vj8CpZH18a8Ixdp5NsNhSVNjC-V48TLU"

app = Flask(__name__)
app.secret_key = "chatbot_secret_123"  # Needed for session management
app.permanent_session_lifetime = timedelta(hours=1)

@app.route("/")
def index():
    if "history" not in session:
        session["history"] = []
    return render_template("index.html", history=session["history"])

@app.route("/api", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant with world knowledge."},
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7,
        "top_p": 0.9
    }

    response = requests.post("https://api.together.xyz/v1/chat/completions", headers=headers, json=payload)
    try:
        reply = response.json()["choices"][0]["message"]["content"]
    except Exception:
        reply = "Sorry, something went wrong."

    # Save messages in session history
    history = session.get("history", [])
    history.append({"user": user_message, "bot": reply})
    session["history"] = history

    return jsonify({"reply": reply})

@app.route("/clear")
def clear():
    session.pop("history", None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
