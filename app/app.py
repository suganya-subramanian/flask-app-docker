from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
	return "Hi this is suganya-Devops engineer"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)