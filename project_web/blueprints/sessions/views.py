
from flask import Blueprint, render_template,request,redirect,url_for,flash 
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_required,login_user,logout_user,current_user
from models.user import *

sessions_blueprint = Blueprint('sessions',
                            __name__,
                            template_folder='templates')


@sessions_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('sessions/new.html')

@sessions_blueprint.route('/students/new', methods=['GET'])
def students():
    return render_template('sessions/students.html')

@sessions_blueprint.route('/teachers/new', methods=['GET'])
def teachers():
    return render_template('sessions/teachers.html')

@sessions_blueprint.route('/', methods=['POST'])
def create():
    username= request.form.get('username')
    password= request.form.get('password')
    user = User_.get_or_none(username=username)
    if user:
        result = check_password_hash(user.password,password)
        if result: 
            flash("Login successful!", "success")
        else:
            flash("Wrong password, please try again", "warning")
            return redirect(url_for('sessions.new'))
    else:
        flash("Wrong username","warning")
        return redirect(url_for('sessions.new'))
    
        