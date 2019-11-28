from flask import Blueprint, render_template,request,redirect,url_for,flash
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_required,login_user,logout_user,current_user

surveys_blueprint = Blueprint('surveys',
                            __name__,
                            template_folder='templates')


@surveys_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('surveys/new.html')

@surveys_blueprint.route('/create', methods=['GET'])
def create():
    topic = request.form.get('topic')
    question_1 = request.form.get('Question_1')
    answer_1 = request.form.get('Answer_1')
    create_survey = Survey(topic=topic, question_answer={question_1 : answer_1})
    create_survey.save()
    return render_template('teachers/survey.html')