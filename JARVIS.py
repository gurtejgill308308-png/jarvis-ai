from flask import Flask, request, jsonify
from google import genai

API_KEY = "TERI_GEMINI_API_KEY"
client = genai.Client(api_key=API_KEY)
app = Flask(__name__)

@app.route('/')
def home(): return "JARVIS Online ✅"
@app.route('/chat', methods=['POST'])
def chat():
    try:
        m=request.json.get('message')
        r=client.models.generate_content(model='gemini-2.0-flash',contents=m)
        return jsonify({"reply": r.text})
    except Exception as e: return jsonify({"reply": str(e)})

if __name__ == '__main__': app.run(host='0.0.0.0', port=10000)
