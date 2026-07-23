from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/hello")
def hello():
    return jsonify({
        "message": "🎉 Flask is running successfully on Vercel!"
    })

@app.route("/api/time")
def current_time():
    return jsonify({
        "current_time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })

@app.route("/about")
def about():
    return """
    <h1>About</h1>
    <p>This is a Flask application deployed on Vercel.</p>
    <a href="/">Go Home</a>
    """

# Required for Vercel
if __name__ == "__main__":
    app.run(debug=True)