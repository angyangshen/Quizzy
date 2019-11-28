from models.base_model import BaseModel
from .survey import Survey
from .user import User_
import peewee as pw
from flask_login import UserMixin
from playhouse.postgres_ext import HStoreField



class User_survey(UserMixin,BaseModel):
    question_response = HStoreField(null=True)
    survey_id = pw.ForeignKeyField(Survey,backref='surveys', null=True)
    user_id = pw.ForeignKeyField(User_,backref='users_')
    