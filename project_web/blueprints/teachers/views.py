from flask import Blueprint, render_template,request,redirect,url_for,flash,jsonify
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_required,login_user,logout_user,current_user
from database import db
from models.user import User_
from models.survey import Survey
from models.user_survey import User_survey

teachers_blueprint = Blueprint('teachers',
                            __name__,
                            template_folder='templates')


@teachers_blueprint.route('/home', methods=['GET'])
def new():
    return render_template('teachers/home.html')

@teachers_blueprint.route('/charts', methods=['GET'])
def charts():
    students = User_.select().where(User_.role == "student")
    return render_template('teachers/charts.html', student=students)

@teachers_blueprint.route('/<chart_topic>', methods=['GET'])
def get_topic(chart_topic):
    students = User_.select().where(User_.role == "student")
    print(chart_topic)
    studentlist=[]
    studentids = []
    for s in students:
        studentlist.append(s.username)
        studentids.append(s.id)
    confidencelevel = []
    confidencestudents = []
    scorelevel = []
    scorestudents = []
    # chart_topic = request.form.get('chart_topic')

    # survey = User_survey.select().where(User_survey.user_id.row == "students")
    # surveys = User_survey.select().join(User_, on=(User_survey.user_id == User_.id)).where(User_.role == 'student')
    # final = surveys.join(Survey, on=(Survey.id == User_survey.survey_id)).where(Survey.topic == 'Mathematics')
    surveys = User_survey.select().join(User_, on=(User_survey.user_id == User_.id)).join(Survey, on=(User_survey.survey_id == Survey.id)).where(User_.role == 'student', Survey.topic == chart_topic)
    # print(final)
    for c in surveys:
        confidencelevel.append(c.confidence_level)
        confidencestudents.append(c.user_id.username)
        scorelevel.append(c.percentage_correct)
        scorestudents.append(c.user_id.username)
    return jsonify({ 
        "confidence":confidencelevel, 
        "confidencestudents":confidencestudents,
        "scoring":scorelevel, 
        "scorestudents":scorestudents
    })

    # "students" : students, 
    #     'studentlist':studentlist,


# @teachers_blueprint.route('/<score_topic>', methods=['GET'])
# def get_score(score_topic):
#     students = User_.select().where(User_.role == "student")
#     scorelevel = []
#     scorestudents = []

#     scores = User_survey.select().join(User_, on=(User_survey.user_id == User_.id)).join(Survey, on=(User_survey.survey_id == Survey.id)).where(User_.role == 'student', Survey.topic == score_topic)
#     for c in scores:
#         scorelevel.append(c.percentage_correct)
#         scorestudents.append(c.user_id.username)
#     return jsonify({ 
#         "score":scorelevel, 
#         "scorestudents":scorestudents
#     })
