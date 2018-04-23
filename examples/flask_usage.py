

from flask import Flask 
import cookie

app = Flask(__name__)

@app.route('/')
def home_page ():
	return "Hello, world!"

@cookie.cookie
def run (port=None):
	port = int(port)
	app.run(debug=True, port=port)

if __name__ == "__main__":
	run() 

