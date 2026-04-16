# Astera Support Desk

Astera Support Desk is a customer service chatbot web app for ecommerce-style support flows. It combines a Flask backend, simple NLP-style intent detection, and a polished responsive frontend to answer common customer questions such as order tracking, delayed delivery, refunds, address changes, payments, coupon issues, account access, and support escalation.

## Features

- Rule-based chatbot with broader support coverage
- Fuzzy intent detection using keyword overlap and text similarity
- Realistic support-desk UI with agent profile styling
- REST API endpoint for chatbot interaction
- Quick action suggestions for common customer issues
- Clean project structure suitable for GitHub portfolios and demos

## Project Structure

```text
Astera Support Desk/
|-- app.py
|-- chatbot_engine.py
|-- requirements.txt
|-- README.md
|-- static/
|   |-- style.css
|   `-- script.js
|-- templates/
    `-- index.html
```

## How It Works

1. The user sends a message from the frontend.
2. Flask receives the message through the `/chat` API route.
3. The chatbot engine normalizes the message and compares it with predefined intent patterns.
4. It uses keyword overlap and fuzzy text matching to choose the best intent.
5. The system returns a response, detected intent, confidence score, and suggested follow-up questions.

## Supported Intents

- Greeting
- Order tracking
- Shipping information
- Delivery delays
- Refund policy
- Return process
- Order cancellation
- Payment methods
- Payment failures
- Account help
- Address change
- Product availability
- Promo code issues
- Store hours
- Contact support
- Goodbye

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Run The Project

```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## Sample Questions

- Where is my order?
- My delivery is delayed.
- Can I change my shipping address?
- My payment failed but money was deducted.
- My coupon code is not working.
- I forgot my password.

## Future Improvements

- Add a database for chat or ticket history
- Connect to live order and courier APIs
- Add authentication and customer profiles
- Upgrade to ML-based intent classification
- Deploy on Render, Railway, or PythonAnywhere

## License

This project is open for educational and portfolio use.
