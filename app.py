from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    print("Current directory content:", os.listdir())
    print("Templates content:", os.listdir("templates"))
    return render_template("index.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)