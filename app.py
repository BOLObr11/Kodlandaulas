from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/secret")
def secret():
    resultado = random.choice(["Cara 🪙", "Coroa 🪙"])
    return render_template("secret.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)
