from flask import Flask, request, render_template, jsonify

app = Flask(__name__, template_folder="../templates", static_folder="../static")  # Especifica la carpeta de plantillas

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/analizar_datos")
def analizar_datos():
    return render_template("analitic.html")

@app.route("/donacion")
def donacion():
    return render_template("donacion.html")

@app.route("/ia")
def ia():
    return render_template("ia.html")

@app.route("/tutoriales")
def tutoriales():
    return render_template("tutorial.html")


@app.route("/calcular-suma", methods=["POST"])
def calcular_suma():
    try:
        data = request.get_json()  # Obtener datos JSON
        num1 = data["num1"]
        num2 = data["num2"]
        resultado = num1 + num2
        return jsonify({"result": resultado})  # Devuelve el resultado como JSON
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
