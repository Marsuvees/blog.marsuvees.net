from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import Base, session as sess, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/auth")
def auth():
    return render_template('auth.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass