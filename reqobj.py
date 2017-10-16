from flask import request
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    browser = request.headers.get('User-Agent')
    return '<p> Your browser is {}</p>'.format(browser)

if __name__ == '__main__':
    app.run(debug=True)

