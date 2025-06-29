from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# 🔑 API key directly set ki gayi hai (hardcoded for now)
openai.api_key = "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"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an intelligent assistant named 'Udaan AI', helpful, friendly and motivational."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.8,
            max_tokens=500
        )
        reply = response.choices[0].message["content"].strip()
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"⚠️ Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
