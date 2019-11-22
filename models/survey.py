from models.base_model import BaseModel
import peewee as pw
from flask_login import UserMixin



class Survey(UserMixin,BaseModel):
    topic=pw.CharField()
    