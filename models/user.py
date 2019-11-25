from models.base_model import BaseModel
import peewee as pw
from flask_login import UserMixin
from enum import Enum


class User_(UserMixin,BaseModel,Enum):
    username = pw.CharField(unique=False)
    password = pw.CharField()
    email = pw.CharField()
    teacher = 1
    student = 2


    