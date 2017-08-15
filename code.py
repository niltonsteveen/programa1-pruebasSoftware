from flask import Flask, render_template
app=Flask(__name__, static_url_path='/Templates')

@app.route('/')
def index():
	return render_template('template.html')

@app.route('/saludo')
def index1():
	return 'ejemplo'

if __name__ == '__main__':
	app.run()