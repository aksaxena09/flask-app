from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.store import StoreModel

class Store(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('catogory',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'store not found'}, 404


    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "An store with name '{}' already exists.".format(name)}

        data = Store.parser.parse_args()
        

        store = StoreModel(name, data['catogory'])
      
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred inserting the store."}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)

        if store:
            store.delete_from_db()
            return {'message': 'store deleted'}
        


class StoreList(Resource):
    def get(self):

        return {'stores': list(map(lambda x: x.json(), StoreModel.query.all()))}
