from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
	page = open("./Template/template.html")
	return page

@app.route('/saludo')
def index1():
	return 'ejemplo'

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)