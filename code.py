from flask import Flask, request, render_template
from flask import jsonify
from werkzeug import secure_filename
import os
app=Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'


def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/' , methods=['POST', 'GET'])
def upload():
	if request.method == 'POST':
		f=request.files['file']
		print type(f)
		f.save(secure_filename(f.filename))	
		"""num=[1,2,3,4,5,7]
		media=11
		desviacion=34.5
		return jsonify(numeros=num, media=media, desviacion=desviacion)"""
		return 'file uploaded successfully'
	else :
		return render_template('template.html')

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)