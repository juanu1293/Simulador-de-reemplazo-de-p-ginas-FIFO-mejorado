from flask import Flask, render_template, request

from algoritmo import fifo_fallos, segunda_oportunidad

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    datos = {"refs": "7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1", "marcos": "3"}
    resultado, error = None, None

    if request.method == "POST":
        datos["refs"] = request.form.get("refs", "").strip()
        datos["marcos"] = request.form.get("marcos", "").strip()
        try:
            refs = [int(x) for x in datos["refs"].replace(",", " ").split()]
            n_marcos = int(datos["marcos"])
            if not refs:
                raise ValueError("Escribe al menos una página en la cadena.")
            if n_marcos < 1:
                raise ValueError("El número de marcos debe ser 1 o más.")
            pasos, fallos = segunda_oportunidad(refs, n_marcos)
            resultado = {
                "pasos": pasos,
                "n_marcos": n_marcos,
                "total": len(refs),
                "fallos": fallos,
                "aciertos": len(refs) - fallos,
                "fallos_fifo": fifo_fallos(refs, n_marcos),
            }
        except ValueError as e:
            error = str(e) if "marcos" in str(e) or "página" in str(e) else \
                "Usa solo números enteros separados por espacios."

    return render_template("index.html", datos=datos, resultado=resultado, error=error)


if __name__ == "__main__":
    app.run(debug=True)
