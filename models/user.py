from models.base_model import BaseModel
import peewee as pw
from flask_login import UserMixin



class User_(UserMixin,BaseModel):
    username = pw.CharField(unique=False)
    password = pw.CharField()
    email = pw.CharField()