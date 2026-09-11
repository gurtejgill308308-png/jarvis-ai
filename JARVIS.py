import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Apni API Key ethe paa
genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "AIzaSy...TeriKey..."))

model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
    return "JARVIS IS LIVE"

@app.route('/ping')
def ping():
    return "JAGDA HAI"

@app.route('/ask')
def ask():
    q = request.args.get('q', '')
    if not q:
        return jsonify({"reply": "Bolo veere ki chahida?"})
    try:
        response = model.generate_content(q)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
