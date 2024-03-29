from flask import Blueprint, render_template,request,redirect,url_for,flash 
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_required,login_user,logout_user,current_user
from models.user_survey import *

students_blueprint = Blueprint('students',
                            __name__,
                            template_folder='templates')


@students_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('')

@students_blueprint.route('/new', methods=['POST'])
def create():
    confidence = request.form["rating"]
    User_survey(confidence_level=confidence).save()
    return render_template('students/new.html')

@students_blueprint.route('/survey', methods=['GET'])
def survey():
    return render_template('students/survey.html')

