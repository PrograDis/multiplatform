from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>¡Pagina en Digital Ocean!</h1>
    <h2>¡Hola Mundo!</h2>
    <p>Yo queria seguir artes xd.</p>  
    <button onclick="location.href='https://pagina-heroku.com'">Ir a Heroku</button>
    <button onclick="location.href='https://pagina-digitalocean.com'">Ir a DigitalOcean</button>
    <button onclick="location.href='https://multiplatform-production.up.railway.app'">Ir a Railway</button>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
