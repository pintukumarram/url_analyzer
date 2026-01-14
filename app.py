from flask import Flask, request, jsonify, render_template
from utils.url_parser import parse_url_details

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze-url", methods=["POST"])
def analyze_url():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    return jsonify(parse_url_details(url))

if __name__ == "__main__":
    app.run(debug=True)
