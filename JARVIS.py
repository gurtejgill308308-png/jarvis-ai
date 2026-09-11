import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

# API Key Render de Environment chon lavega
API_KEY = os.environ.get("GEMINI_API_KEY") 
if not API_KEY:
    API_KEY = "TEMPERORY_KEY_PASTE_HERE_IF_NEEDED" # ithe apni key paa de je env ch nahi

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "JARVIS JAGDA HAI"

@app.route('/ping')
def ping():
    return "JAGDA HAI"

@app.route('/ask')
def ask():
    q = request.args.get('q','')
    if not q:
        return jsonify({"reply": "Ki puchna?"})
    try:
        response = model.generate_content(q)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": f"Error: {e}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
