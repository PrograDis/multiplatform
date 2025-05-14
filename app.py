from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>¡Página en Railway!</h1>
    <button onclick="location.href='https://heroku-deployment-0de4ea1c85ec.herokuapp.com'">Ir a Heroku</button>
    <button onclick="location.href='hhttps://shark-app-az7mh.ondigitalocean.app'">Ir a DigitalOcean</button>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
