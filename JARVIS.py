from flask import Flask, request, jsonify
from google import genai

API_KEY = "TERI_GEMINI_API_KEY"
client = genai.Client(api_key=API_KEY)
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>JARVIS AI - India da Best AI Assistant by Gurtej</title>
        <meta name="description" content="JARVIS AI by Gurtej Gill. India da apna AI assistant. Koi vi sawal pucho.">
        <meta name="google-site-verification" content="MIY2hPLifmIRB2jc_COPY_WALA_PURA_CODE">
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body style="font-family:Arial; text-align:center; padding:50px;">
        <h1>JARVIS Online ✅</h1>
        <p>India da Best AI - Gurtej Gill dwara banaya</p>
        <a href="#" style="background:black; color:white; padding:12px 20px; text-decoration:none; border-radius:8px;">Chat with JARVIS</a>
        <p style="margin-top:20px;">Google te search karo: JARVIS AI Gurtej</p>
    </body>
    </html>
    """

@app.route('/google81207f9f266a8db9.html')
def google_verify():
    return "google-site-verification: google81207f9f266a8db9.html"

@app.route('/chat', methods=['POST'])
def chat():
    try:
        m=request.json.get('message')
        r=client.models.generate_content(model='gemini-2.0-flash',contents=m)
        return jsonify({"reply": r.text})
    except Exception as e: return jsonify({"reply": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
