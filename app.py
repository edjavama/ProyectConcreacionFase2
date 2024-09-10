from flask import Flask, render_template
import pandas as pd
import csv

app=Flask(__name__)

# Función para cargar los datos desde un archivo CSV
def leer_datos_csv(archivo):
    cards = []
    with open(archivo, newline='', encoding='utf-8') as archivocsv:
        reader = csv.DictReader(archivocsv)
        for row in reader:
            cards.append({
                'nombre_pais': row['nombre_pais'],  # Nombre de las columnas en tu CSV
                'nombre': row['nombre'],
                'item1': row['item1'],
                'valor1': row['valor1'],
                'item2': row['item2'],
                'valor2': row['valor2']
            })
    return cards

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/index.html')
def index_2():
    return render_template('index.html')
@app.route('/mapas.html')
def mapas():
    return render_template('mapas.html')
@app.route('/boyaca.html')
def boyaca():
    return render_template('boyaca.html')
@app.route('/cundinamarca.html')
def cundinamarca():
    return render_template('cundinamarca.html')
@app.route('/dashboard.html')
def dashboard():
    # Cargar los datos de dos conjuntos de tarjetas
    cards_1 = leer_datos_csv('filtroextraidos.csv')  #primer archivo
    cards_2 = leer_datos_csv('filtro_cundinamarca.csv') #segundo archivo
    return render_template('dashboard.html', cards_1=cards_1, cards_2=cards_2)
@app.route('/contactenos.html')
def contactenos():
    return render_template('contactenos.html')
@app.route('/suscribirse.html')
def suscribirse():
    return render_template('suscribirse.html')
@app.route('/pqrs.html')
def pqrs():
    return render_template('pqrs.html')

if __name__=='__main__':
    app.run(debug=True)