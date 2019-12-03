from flask import Blueprint, render_template,request,redirect,url_for,flash
from flask_login import login_required,login_user,logout_user,current_user
from models.survey import Survey
from models.user_survey import User_survey

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

@surveys_blueprint.route('/view', methods=['POST'])
def view():
    survey_code = request.form.get('survey_code')
    survey = Survey.get_by_id(survey_code)
   
    return render_template('students/surveys.html', survey=survey)

@surveys_blueprint.route('/checkanswer', methods=['POST'])
def checkAnswer():
    create_response = User_survey(question_response = request.json['survey'],student_survey_id = request.json['id'])
    print(create_response)
    current_survey = Survey.get_by_id(request.json['id'])
    print(current_survey)
    question_answer =  current_survey.question_answer
    result = []
    for index, q_r in enumerate(create_response.question_response):
        if q_r['question'] in question_answer[index]['question'] and q_r['answer'] in question_answer[index]['answer']:
            q_r['correct']= True
            result.append(q_r)
            
        else:
            q_r['correct']= False
            result.append(q_r)

    percentage = []        
    test = [q['correct'] for q in result]
    percentage = (test.count(True)/len(test))*100   

    create_response.question_response = result
    create_response.percentage_correct = percentage
    create_response.save()

    return (url_for('surveys.result', survey_id = request.json['id']))
    


@surveys_blueprint.route('/result/<survey_id>', methods =['GET'])
def result(survey_id):
    current_survey = User_survey.get_by_id(survey_id)
    passed = True
    if current_survey.percentage_correct >= 50:
        passed = True
    elif current_survey.percentage_correct < 50:
        passed = False
    print("your mom")
    return render_template('surveys/result.html',percentage = current_survey.percentage_correct, passed = passed)
    
            

        



