from application.controllers.home import home
from application.controllers.user_login import login_route
from flask import Flask
import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://tyler:tyler@cluster0-zd1wk.mongodb.net/test?retryWrites=true&w=majority")

db = cluster['DiGift']
collection = db['email']
user_email = {}


app = Flask("digift", template_folder='application/templates',
            static_folder='application/static',
            instance_relative_config=True)

app.register_blueprint(home)
app.register_blueprint(login_route)

class Email():
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_email(self):
        if email is None:
            user_email.append(self.name, self.email)
            collection.insert_one(user_email)

            return self.email

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)
