from flask import Flask, render_template_string, request, jsonify
from google import genai
import os

API_KEY = "AQ.Ab8RN6KE5wNXsievxmBsYQGGfQM8sYjVoezrqIwa1svRMOj3gg"
client = genai.Client(api_key=API_KEY)
app = Flask(__name__)

HTML = """<html><head><title>JARVIS</title><meta name="viewport" content="width=device-width, initial-scale=1"><style>body{background:#0a1931;color:white;font-family:Arial;margin:0;padding:20px;}#chat{max-width:700px;margin:auto;padding-bottom:100px;} .msg{padding:12px 18px;border-radius:20px;margin:10px;max-width:80%;display:inline-block;} .user{background:#0084ff;float:right;clear:both;} .bot{background:#2a2a4a;float:left;clear:both;} #box{position:fixed;bottom:20px;left:0;width:100%;text-align:center;background:#0a1931;padding:15px 0;} input{width:65%;padding:14px;border-radius:25px;border:none;} button{padding:14px 22px;border-radius:25px;border:none;background:#0084ff;color:white;margin-left:8px;}</style></head><body><div id="chat"><div><div class='msg bot'>Ssa! Main JARVIS aa 🚀</div></div></div><div id="box"><input id="inp" placeholder="Kujh pucho..."><button onclick="send()">Send</button></div><script>async function send(){let t=document.getElementById('inp').value; if(!t) return; let c=document.getElementById('chat'); c.innerHTML+=`<div style='text-align:right'><div class='msg user'>`+t+`</div></div>`; document.getElementById('inp').value=''; let r=await fetch('/chat',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:t})}); let d=await r.json(); c.innerHTML+=`<div><div class='msg bot'>`+d.reply+`</div></div>`;}</script></body></html>"""
@app.route('/')
def home(): return render_template_string(HTML)
@app.route('/chat', methods=['POST'])
def chat():
 try:
  m=request.json.get('message')
  res=client.models.generate_content(model='gemini-2.0-flash',contents=m)
  return jsonify({"reply": res.text})
 except Exception as e: return jsonify({"reply": f"Error: {e}"})
if __name__ == '__main__': app.run(host='0.0.0.0', port=10000)