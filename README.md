# Reemplazo de páginas con bit de referencia (segunda oportunidad)

Simulador del algoritmo FIFO mejorado (segunda oportunidad).
- Backend: Python + Flask (`app.py`, `algoritmo.py`)
- Frontend: HTML (`templates/index.html`) y CSS (`static/style.css`)

## Cómo ejecutarlo
```
pip install -r requirements.txt
python app.py
```
Abre http://127.0.0.1:5000 en el navegador.

## Cómo funciona
Cada marco guarda una página y su bit de referencia. Un puntero circular señala la página más antigua.
- Acierto: el bit de la página pasa a 1.
- Fallo con marco libre: la página entra con bit 1.
- Fallo sin marcos libres: si la página del puntero tiene bit 1, se pone en 0 y el puntero avanza (segunda oportunidad). Si tiene bit 0, se reemplaza.
