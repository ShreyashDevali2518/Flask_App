from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/hello")
def hello():
    return jsonify(message="Hello from Flask!")


if __name__ == "__main__":
    # debug=True is fine for local dev; turn off before deploying
    app.run(debug=True, host="0.0.0.0", port=5000)
