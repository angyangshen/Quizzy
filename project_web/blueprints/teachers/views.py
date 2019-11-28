from flask import Blueprint, render_template,request,redirect,url_for,flash
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from flask_login import login_required,login_user,logout_user,current_user

teachers_blueprint = Blueprint('teachers',
                            __name__,
                            template_folder='templates')


@teachers_blueprint.route('/home', methods=['GET'])
def new():
    return render_template('teachers/home.html')
