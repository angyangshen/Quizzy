from models.base_model import BaseModel
from .survey import Survey
from .user import User_
import peewee as pw
from flask_login import UserMixin
from playhouse.postgres_ext import JSONField



class User_survey(UserMixin,BaseModel):
    question_response = JSONField(null=True)
    student_survey_id = pw.IntegerField(null=True)
    user_id = pw.ForeignKeyField(User_, backref="user", null = True)
    
    