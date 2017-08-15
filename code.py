
import os
from flask import Flask, request, render_template
from flask import jsonify
from werkzeug import secure_filename
from Code.camilaCode import ReadFile, myExc
from Code.niltonCode import CodeDeviation

app=Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
#app=Flask(__name__, static_url_path='/Templates')

@app.route("/")
def index():
	return render_template("template.html")

@app.route('/upload' , methods=['POST'])
def upload():
	if request.method == 'POST':
		f = request.files['file']
		cd = CodeDeviation()		
		readFile = ReadFile()
		readFile.readFile(f)
		numeros=readFile.muestra
		media=45
		desviacion=cd.calcularDesviacion(cd.calcularNumerador(numeros), len(numeros))
		salida=jsonify(numeros=numeros, media=media, desviacion=desviacion)
		return salida

if __name__ == '__main__':
	app.run()