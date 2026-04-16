from flask import Flask, jsonify, render_template, request

from chatbot_engine import CustomerServiceChatbot


app = Flask(__name__)
chatbot = CustomerServiceChatbot()


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/chat")
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()

    if not message:
        return jsonify(
            {
                "reply": "Please enter a question so I can help you.",
                "intent": "empty_input",
                "confidence": 0.0,
                "suggestions": ["Track my order", "Refund policy", "Contact support"],
            }
        )

    response = chatbot.get_response(message)
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
