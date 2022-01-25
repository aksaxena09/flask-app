import sqlite3
from db import db

class StoreModel(db.Model):

    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    catogory = db.Column(db.String(80))

    items = db.relationship('itemModel', lazy='dynamic') #only when json is called it will look into db otherwise no. 

    def __init__(self, name, catogory):
        self.name = name
        self.catogory = catogory
        

    def json(self):
        return {'name':self.name, 'catogory':self.catogory, 'items':[item.json() for item in self.items.all()]}
    
    @classmethod
    def find_by_name(cls, name):
        
        return cls.query.filter_by(name=name).first() #SELECT * FROM {table} WHERE name=name

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()