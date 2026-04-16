<p align="center">
  <img src="assets/banner.svg" alt="Astera Support Desk banner" width="100%">
</p>

# Astera Support Desk

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-233746?style=for-the-badge&logo=python&logoColor=white" alt="Python badge">
  <img src="https://img.shields.io/badge/Flask-Web%20App-5F8D76?style=for-the-badge&logo=flask&logoColor=white" alt="Flask badge">
  <img src="https://img.shields.io/badge/NLP-Intent%20Matching-D96C3D?style=for-the-badge" alt="NLP badge">
  <img src="https://img.shields.io/badge/Status-Portfolio%20Ready-2D4454?style=for-the-badge" alt="Status badge">
</p>

Astera Support Desk is a customer-service chatbot for ecommerce support teams. It is designed to handle common customer queries such as order tracking, delivery delays, refunds, payment issues, address changes, and account-access problems through a polished web interface and a lightweight NLP-style intent engine.

This project was built to demonstrate practical product thinking, backend API design, frontend execution, and applied NLP fundamentals in a way that feels closer to a real support tool than a classroom prototype.

## Portfolio Summary

Astera Support Desk is a polished full-stack chatbot project that demonstrates:

- applied NLP fundamentals through intent detection and fuzzy matching
- backend API design with Flask
- frontend product thinking through a branded, responsive support interface
- realistic business use cases in ecommerce customer support

This is the kind of project that is easy to discuss in interviews because it combines technical implementation with clear product value.

## Live Repository Preview

<p align="center">
  <img src="assets/chat-preview.svg" alt="Astera Support Desk interface preview" width="100%">
</p>

## Why This Project Stands Out

- Solves a real business problem by reducing repetitive customer-support workload
- Combines backend logic, UI design, and conversational experience in one project
- Uses explainable intent detection instead of a black-box model, making it easy to discuss in interviews
- Presents the chatbot as a believable product with clean branding and realistic support flows
- Shows readiness for future scaling into live APIs, CRM systems, and ML-based classification

## Product Overview

Astera Support Desk acts as a first-line digital support associate. A customer can open the chat interface, ask a natural question, and receive immediate guidance for common support cases.

Examples:

- "Where is my order?"
- "My payment failed but money was deducted."
- "Can I change my delivery address?"
- "My coupon is not working."
- "I forgot my password."

The chatbot identifies the most likely user intent, returns a relevant answer, and suggests useful follow-up questions to keep the conversation moving.

## Core Features

- Rule-based chatbot with fuzzy intent matching
- Responsive support-desk style frontend
- Flask backend with a dedicated `/chat` API endpoint
- Intent detection using keyword overlap and string similarity
- Support for realistic ecommerce issues such as refunds, payment failures, delayed delivery, and account help
- Quick action suggestions for smoother user interaction
- Graceful fallback responses for unsupported questions

## Supported Customer Intents

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

## Tech Stack

- Python
- Flask
- HTML
- CSS
- JavaScript
- `difflib.SequenceMatcher` for lightweight fuzzy matching

## Architecture Snapshot

<p align="center">
  <img src="assets/architecture.svg" alt="Astera Support Desk architecture diagram" width="100%">
</p>

## System Design

### 1. Frontend

The frontend provides a modern support-chat experience with:

- branded hero section
- conversational chat layout
- avatar-based message styling
- quick-action suggestion chips
- responsive design for desktop and mobile

### 2. Backend

The Flask server:

- serves the main UI
- accepts chat messages through a JSON API
- routes user messages to the chatbot engine
- returns structured responses with reply text, detected intent, confidence score, and follow-up suggestions

### 3. Chatbot Engine

The chatbot engine:

- normalizes user input
- compares it against predefined intent patterns
- scores matches using keyword overlap and fuzzy similarity
- selects the best intent above a confidence threshold
- falls back gracefully when no strong match is found

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

## What Recruiters Can Look At

### Product Thinking

- The chatbot is framed as a usable support experience, not just a technical demo
- The interface and conversation design were shaped around realistic customer needs

### Engineering Skills

- Clean separation between UI, API, and chatbot logic
- Structured JSON responses between frontend and backend
- Intent matching logic that is simple, explainable, and extensible

### UX and Frontend Execution

- Visually polished interface
- Smooth chat interaction with suggestions and typing feedback
- Mobile-friendly responsive layout

### Extensibility

- Easy to connect to order databases or courier APIs
- Easy to replace the rule-based engine with an ML or LLM-based classifier later

## GitHub About Section

If you want to use a short description in the GitHub repository "About" field, use:

```text
Polished Flask-based customer support chatbot with rule-based NLP, fuzzy intent matching, and a responsive ecommerce help desk UI.
```

## Local Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the environment

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

```text
http://127.0.0.1:5000
```

## Free Deployment Option

As of April 17, 2026, the easiest free option for this Flask project is PythonAnywhere.

Why this is the best fit:

- PythonAnywhere still offers a free `Beginner` account
- it supports Flask directly
- it is simpler for this project than converting the app to serverless hosting
- it does not require the `gunicorn` startup flow used by platforms like Render

Important free-plan limits:

- 1 web app
- 1 web worker
- 512 MiB disk space
- 2 consoles
- 1 month expiry on the free web app

Official sources:

- PythonAnywhere free account features: https://help.pythonanywhere.com/pages/FreeAccountsFeatures
- PythonAnywhere pricing: https://www.pythonanywhere.com/pricing/
- Flask setup guide: https://help.pythonanywhere.com/pages/Flask

### Deploy To PythonAnywhere

1. Create a free PythonAnywhere account.
2. Open the `Web` tab.
3. Click `Add a new web app`.
4. Choose `Manual configuration` and select Python 3.
5. Upload or clone this GitHub repo into your PythonAnywhere home folder.
6. Open the WSGI configuration file from the `Web` tab.
7. Replace its contents with the code from `pythonanywhere_wsgi.py`, but change:

```python
project_home = Path("/home/yourusername/Chatbot")
```

to your real PythonAnywhere username and folder path.

8. Reload the web app from the `Web` tab.

### Notes

- On PythonAnywhere, your Flask app is loaded through the WSGI file, not by running `python app.py`.
- The `if __name__ == "__main__":` block in `app.py` is fine and will not run during PythonAnywhere import.
- If you want, I can next simplify the repo for PythonAnywhere specifically and remove the Render-only files.

## Example Questions To Test

- Where is my order?
- My order is delayed.
- I want a refund.
- My payment failed but money was deducted.
- Can I change my delivery address?
- My coupon code is not working.
- I forgot my password.
- How can I contact support?

## Future Improvements

- Add real order-tracking integration
- Add customer authentication and profile history
- Store chat logs or support tickets in a database
- Add analytics for common support issues
- Upgrade intent detection with machine learning or LLM-based routing
- Deploy the app to Render, Railway, or another cloud platform

## Interview Talking Points

- Why a rule-based NLP system can be a strong first version for support automation
- How fuzzy matching improves intent detection over exact keyword matching
- Why support-chat UX matters as much as backend accuracy
- How this architecture can evolve into a production-ready support assistant

## License

This project is open for educational and portfolio use.
