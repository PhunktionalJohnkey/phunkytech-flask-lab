# This is the Product class

# Imports db to gain access to SQLAlchemy
from db import db

# Creates a new class named Product that extends db.Model
class Product(db.Model):
    __tablename__ = 'products' # defines the table name

    # Creates 2 additional fields - id and name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    # Initializes the class to accept and id and a name
    def __init__(self, id, name):
        self.id = id
        self.name = name

    # Defines persistence and query methods
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.get(_id)

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def json(self):
        return {
            "id": self.id,
            "name": self.name
        }

