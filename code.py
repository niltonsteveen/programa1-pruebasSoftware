from flask import Flask, request, render_template
from flask import jsonify
from werkzeug import secure_filename
app=Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/' , methods=['POST', 'GET'])
def upload():
	if request.method == 'POST':
		file = request.files['file']
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			num=[1,2,3,4,5,7]
			media=11
			desviacion=34.5
		return jsonify(numeros=num, media=media, desviacion=desviacion)
	else :
		return render_template('template.html')

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)