from flask import Blueprint, render_template,request,redirect,url_for,flash
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_required,login_user,logout_user,current_user
from database import db
from models.user import User_
from models.survey import Survey

teachers_blueprint = Blueprint('teachers',
                            __name__,
                            template_folder='templates')


@teachers_blueprint.route('/home', methods=['GET'])
def new():
    students = User_.select()
    return render_template('teachers/home.html', students = students)


@teachers_blueprint.route('/survey', methods=['GET'])
def survey():
    return render_template('teachers/survey.html')

@teachers_blueprint.route('/survey', methods=['POST'])
def create():
    topic = request.form.get('topic')
    question_1 = request.form.get('Question_1')
    answer_1 = request.form.get('Answer_1')
    create_survey = Survey(topic=topic, question_answer={question_1 : answer_1})
    create_survey.save()
    return render_template('teachers/survey.html')
    