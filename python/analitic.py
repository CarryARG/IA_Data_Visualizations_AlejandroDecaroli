from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calcular-suma", methods=["POST"])
def calcular_suma():
    try:
        data = request.get_json()
        num1 = data["num1"]
        num2 = data["num2"]
        resultado = num1 + num2
        return jsonify({"result": resultado})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
