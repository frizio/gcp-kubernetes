import locale
from flask import Flask
from datetime import datetime


locale.setlocale(locale.LC_ALL, 'it_IT')
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello GCP World!</h1>'


@app.route('/version')
def version():
    s = '<h1>GCP Developer Enablement Program</h1>'
    s += '<p>Questa è la demo di Docker, versione 1.0<p>'
    s += '<p>' + datetime.time(datetime.now()).strftime('%A, %d %B %Y alle %H:%M:%S') + '<p>'
    return s


if __name__ == '__main__':
    app.run()
