from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views',__name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/recommender')
@login_required
def recommender():
    return render_template("recommender.html", user=current_user)

@views.route('/results')
@login_required
def results():
    return render_template("results.html", user=current_user)

@views.route('/negative')
@login_required
def negative():
    return render_template("negative.html", user=current_user)
