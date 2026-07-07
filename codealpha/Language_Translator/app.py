from flask import Flask, render_template, request, jsonify
from translator import translate_text

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()

    text = data["text"]
    source = data["source"]
    target = data["target"]

    translated = translate_text(
        text,
        source,
        target
    )

    return jsonify({
        "translated": translated
    })

if __name__ == "__main__":
    app.run(debug=True)