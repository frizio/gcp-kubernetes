import locale
from flask import Flask
from datetime import datetime
import socket


locale.setlocale(locale.LC_ALL, 'it_IT')
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello GCP World!</h1>\n'


@app.route('/hello/<name>')
def hello(name):
    return '<h1>Hello %s!</h1>\n' % name


@app.route('/version')
def version():
    s = '<h1>GCP Developer Enablement Program</h1>\n'
    s += '<p>Questa è la demo di Docker, versione 1.0<p>\n'
    s += '<p>Pagina servita da ' + socket.gethostname() + '<p>\n'
    s += '<p>' + datetime.time(datetime.now()).strftime('%A, %d %B %Y alle %H:%M:%S') + '<p>\n'
    return s


if __name__ == '__main__':
    app.run()
