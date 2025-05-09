from flask import Flask, render_template, request, jsonify
from chatbot import build_bot

app = Flask(__name__)
bot = build_bot("Colombian_Law_Overview.pdf")  # Replace with your PDF file

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    question = request.json.get("question", "")
    answer = bot.invoke(question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)