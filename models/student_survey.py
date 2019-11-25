from models.base_model import BaseModel
import peewee as pw
from flask_login import UserMixin



class Student_survey(UserMixin,BaseModel):
    question = pw.CharField(unique=False)
    answer = pw.CharField(default='')
    response = pw.CharField()
    survey_id = pw.ForeignKeyField(Survey,backref='survey')
    