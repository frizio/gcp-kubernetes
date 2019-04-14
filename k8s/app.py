from flask import Flask
import pymongo
from bson.json_util import dumps
import socket

mongo_client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mongo_db = mongo_client["mydatabase"]
mongo_coll = mongo_db["users"]

app = Flask(__name__)


@app.route('/user/<name>')
def user(name):
    try:
        with open("/web-cfg/last-greeting", "w") as f:
            f.write("Searched %s by %s" % (name, socket.gethostname()))
    except:
        pass
    user_object = mongo_coll.find_one({"username": name})
    if user_object is None:
        return "Could not find"
    return dumps(user_object)


if __name__ == '__main__':
    app.run()
