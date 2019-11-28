from models.base_model import BaseModel
import peewee as pw
from flask_login import UserMixin
from playhouse.postgres_ext import HStoreField
<<<<<<< HEAD

=======
>>>>>>> master


class Survey(UserMixin,BaseModel):
    topic=pw.CharField()
<<<<<<< HEAD
    question_answer = HStoreField(null=True)
    
=======
    question_answer = HStoreField()

>>>>>>> master
