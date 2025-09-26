# -*- coding: utf-8 -*-
from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- Inventario de sistemas vidriados ---
inventario = {
    "ventana corrediza": {"precio": 350000, "descuento": 5},
    "puerta vidrio templado": {"precio": 1200000, "descuento": 10},
    "fachada estructural": {"precio": 5800000, "descuento": 0},
    "baranda en aluminio y vidrio": {"precio": 950000, "descuento": 8},
    "ventana batiente": {"precio": 420000, "descuento": 0},
}

def consultar_producto(nombre_producto):
    nombre_producto = nombre_producto.lower()
    if nombre_producto in inventario:
        producto = inventario[nombre_producto]
        precio = producto["precio"]
        descuento = producto["descuento"]
        if descuento > 0:
            precio_final = precio - (precio * descuento / 100)
            return f"✅ El sistema **{nombre_producto}** tiene un valor de {precio:,.0f} pesos, con {descuento}% de descuento aplicado. Precio final: {precio_final:,.0f} pesos."
        else:
            return f"✅ El sistema **{nombre_producto}** tiene un valor de {precio:,.0f} pesos (sin descuento actualmente)."
    else:
        return f"❌ El producto **{nombre_producto}** no está registrado en nuestro portafolio. Contáctanos para una cotización personalizada."

# --- Plantilla HTML ---
html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>ChatBot Ventanería</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f6f9; display:flex; justify-content:center; align-items:center; height:100vh; }
        .chatbox { background:white; padding:20px; border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1); width:420px; }
        h2 { color:#007BFF; }
        input, button { padding:10px; width:100%; margin-top:10px; border-radius:8px; border:1px solid #ccc; }
        button { background:#007BFF; color:white; border:none; cursor:pointer; }
        button:hover { background:#0056b3; }
        .respuesta { margin-top:15px; padding:10px; background:#eaf4ff; border-radius:8px; }
    </style>
</head>
<body>
    <div class="chatbox">
        <h2>🏢 Ventanería Ingeniería y Diseño</h2>
        <p>Consulte precios de nuestros sistemas vidriados:</p>
        <form method="POST">
            <input type="text" name="producto" placeholder="Ej: ventana corrediza" required>
            <button type="submit">Consultar</button>
        </form>
        {% if respuesta %}
        <div class="respuesta">{{ respuesta|safe }}</div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    respuesta = ""
    if request.method == "POST":
        producto = request.form["producto"]
        respuesta = consultar_producto(producto)
    return render_template_string(html, respuesta=respuesta)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


