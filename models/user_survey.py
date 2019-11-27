from models.base_model import BaseModel
from .survey import Survey
from .user import User_
import peewee as pw
from flask_login import UserMixin



class User_survey(UserMixin,BaseModel):
    question = pw.CharField(unique=False)
    answer = pw.CharField(default='')
    response = pw.CharField()
    survey_id = pw.ForeignKeyField(Survey,backref='surveys')
    user_id = pw.ForeignKeyField(User_,backref='users_')
    