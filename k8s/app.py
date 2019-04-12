from flask import Flask
import pymongo
import time

host = ""
found = False
while found:
    try:
        with open("/mongo-cfg/hostname", "r") as f:
            if f.mode == 'r':
                host = f.read()
                found = True
    except:
        time.sleep(0.5)

mongo_client = pymongo.MongoClient("mongodb://%s:27017/" % host)
mongo_db = mongo_client["mydatabase"]
mongo_coll = mongo_db["customers"]

app = Flask(__name__)


@app.route('/user/<name>')
def user(name):
    user_object = mongo_coll.find_one({"username": name})
    return user_object


if __name__ == '__main__':
    app.run()
