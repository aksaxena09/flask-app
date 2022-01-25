from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

#when we import a file in python it run the file. 
from security import authenticate, identity
from resources.user import userRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db
    
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #every change istracked which is turne off
app.secret_key = 'Akarsh'
api = Api(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) # /auth new endpoint

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(userRegister, '/register')

if __name__ == '__main__': #because if we import app file anywhere it will not get run.
    
    app.run(port=8000, debug=True) #debug opens html page during errors to show good error message and reruns app after saved changes
 
