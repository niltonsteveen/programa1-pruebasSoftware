import os
from flask import Flask, request, render_template
from werkzeug import secure_filename

app=Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
	return render_template("template.html")


@app.route('/upload' , methods=['POST'])
def upload():
	if request.method == 'POST':
		"""target = os.path.join(APP_ROOT, 'images/')
		if not os.path.isdir(target):
			os.mkdir(target)"""
		f = request.files['file']
		filename=f.filename
		"""for file in request.files.getlist('file'):
			filename=file.filename"""
			#destination='/'.join([target,filename])
			#file.save(destination)
		return filename

		"""print 'entro por aca'
		f=request.files['file']
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], f))"""
		"""num=[1,2,3,4,5,7]
		media=11
		desviacion=34.5
		return jsonify(numeros=num, media=media, desviacion=desviacion)"""
	else :
		return render_template('template.html')

if __name__ == '__main__':
	app.run()