from app import app
from flask import render_template
from project_web.blueprints.teachers.views import teachers_blueprint
from project_web.blueprints.students.views import students_blueprint
from project_web.blueprints.sessions.views import sessions_blueprint
from flask_assets import Environment, Bundle
from .util.assets import bundles

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(teachers_blueprint, url_prefix="/teachers")
app.register_blueprint(students_blueprint, url_prefix="/students")
app.register_blueprint(sessions_blueprint, url_prefix="/sessions")


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/contact")
def contact():
    return render_template('contact_us.html')

@app.route("/aboutus")
def about():
    return render_template('about_us.html')

@app.route("/pricingplan")
def pricing():
    return render_template('pricing_plan.html')


