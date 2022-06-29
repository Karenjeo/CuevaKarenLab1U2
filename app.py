# importar os
import os 
# importar la libreria flask
from flask import Flask, render_template
 # Instancia de la clase Flask y la respectiva clase
app = Flask(__name__)
app.secret_key = "s3cr3t" 
app.debug = False 
app._static_folder = os.path.abspath("templates/static/") 


@app.route('/')
def principal():
    """
    Esta función esta encarga de abrir la página principal
    desde donde se ejecutara el html y las funciones que hemos
    programado en javascript

    Returns:
        Retorna la página principal, denomindad blockhopper.html
    """
    #ruta de la página principal
    return render_template('layouts/index.html') 

#main
if __name__ == '__main__':
    app.run(debug=True)