from flask import Blueprint, render_template,request,redirect,url_for,flash
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_required,login_user,logout_user,current_user
from models.survey import Survey

surveys_blueprint = Blueprint('surveys',
                            __name__,
                            template_folder='templates')


@surveys_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('surveys/new.html')

@surveys_blueprint.route('/create', methods=['POST'])
def create():
    create_survey = Survey(topic=request.json['topic'], question_answer=request.json['survey'])
    create_survey.save()
    survey = Survey.select().order_by(Survey.id.desc()) 
    return str(survey[0].id)

@surveys_blueprint.route('/view', methods=['GET'])
def view():
    survey = Survey.select().order_by(Survey.id.desc())  
    return render_template('students/surveys.html', survey=survey)