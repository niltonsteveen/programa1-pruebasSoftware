from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
	return 'Hola mundo'

@app.route('/saludo')
def index1():
	return 'ejemplo'

app.run()