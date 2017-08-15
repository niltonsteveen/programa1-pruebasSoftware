from flask import Flask, request, render_template
app=Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route('/' , methods=['POST', 'GET'])

def upload():
	if request.method == 'POST':
		file = request.files['file']
		data={
			'numeros': [1,2,3,4,5,7],
			'media': 11,
			'desviacion': 34.5
		}
		return file
	else :
		return render_template('template.html')

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)