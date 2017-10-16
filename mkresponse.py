from flask import Flask
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
    response = make_response('<h1>this is an example of make response</h1>',900)
    response.set_cookie('answer','42')
    return response

if __name__ == '__main__':
    app.run(debug=True)

