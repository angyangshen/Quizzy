from models.base_model import BaseModel
import peewee as pw
from flask_login import UserMixin
from playhouse.postgres_ext import JSONField


class Survey(UserMixin,BaseModel):
    topic=pw.CharField(null=True)
    question_answer = JSONField(null=True)
    
