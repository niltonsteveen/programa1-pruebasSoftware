from flask import Flask, request
app=Flask(__name__)

@app.route('/', methods=['POST','GET'])
def upload():
	if request.method == 'POST':
		fileUpload=request.files['file']
	return render_template('template.html')

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)