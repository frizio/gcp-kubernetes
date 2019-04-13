from flask import Flask
import pymongo
import time

# dbname = ""
# found = False
# while found:
#     try:
#         with open("/mongo-cfg/database", "r") as f:
#             if f.mode == 'r':
#                 dbname = f.read()
#                 found = True
#     except:
#         time.sleep(0.5)

mongo_client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mongo_db = mongo_client["mydatabase"]
mongo_coll = mongo_db["customers"]

app = Flask(__name__)


@app.route('/user/<name>')
def user(name):
    user_object = mongo_coll.find_one({"username": name})
    return user_object


@app.route('/shared-data')
def shared():
    with open("/mongo-cfg/database", "r") as f:
        if f.mode == 'r':
            return f.read()
    return "Can't read it"


if __name__ == '__main__':
    app.run()
