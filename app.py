from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "mensagem": "Flask funcionando!",
        "status": "OK"
    })


@app.route("/teste")
def teste():
    return jsonify({
        "teste": "CI/CD funcionando!"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
