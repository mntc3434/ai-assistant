from flask import Flask, jsonify, request
from flask_cors import CORS  # Import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes (or specify origins if needed)

# Replace with your Geminai API key
GEMINAI_API_KEY = "AIzaSyAmKtLwOMfaNeEGz6jbMdE65epmoKNq3LE"
genai.configure(api_key=GEMINAI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


@app.route("/api/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Generate content using Geminai API
        response = model.generate_content(user_message)

        bot_reply = response.text  # Assuming the response has the 'text' attribute

        return jsonify({"reply": bot_reply})

    except Exception as e:
        return jsonify({"error": f"Request failed: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
