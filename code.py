
import os
from flask import Flask, request, render_template
from werkzeug import secure_filename

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
		filename=f.filename
		linea1 = f.readline()
		return linea1

		"""print 'entro por aca'
		f=request.files['file']
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], f))"""
		"""num=[1,2,3,4,5,7]
		media=11
		desviacion=34.5
		return jsonify(numeros=num, media=media, desviacion=desviacion)"""

if __name__ == '__main__':
	app.run()