
import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'cookbook_manager'
app.config["MONGO_URI"] = 'mongodb+srv://<username>:<password>@myfirstcluster-eimbl.mongodb.net/test?retryWrites=true&w=majority'


@app.route('/')
def hello():
    return 'Hello World ...again'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '127.0.0.1'),
            port=int(os.environ.get('PORT', '8080')),
            debug=True)