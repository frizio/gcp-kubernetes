import locale
from flask import Flask
from datetime import datetime
import socket
import requests

locale.setlocale(locale.LC_ALL, 'it_IT')
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello GCP World!</h1>\n'


@app.route('/hello/<name>')
def hello(name):
    r = requests.get('http://127.0.0.1:5003/user/%s' % name)
    if r.status_code == 200:
        user = r.json()
        return '<h1>Hello %s %s!</h1>\n' % (user['firstname'], user['lastname'])
    else:
        return '<h1>Error: %d!</h1>\n' % r.status_code


@app.route('/version')
def version():
    s = '<h1>GCP Developer Enablement Program</h1>\n'
    s += '<p>Questa è la demo di Docker, versione 1.0<p>\n'
    s += '<p>Pagina servita da ' + socket.gethostname() + '<p>\n'
    s += '<p>' + datetime.now().strftime('%A, %d %B %Y alle %H:%M:%S') + '<p>\n'
    return s


@app.route('/last')
def last():
    try:
        with open("/api-cfg/last-greeting", "r") as f:
            return f.read()
    except:
        return "<error>"


if __name__ == '__main__':
    app.run()
