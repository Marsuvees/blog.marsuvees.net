from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import Base, session as sess, User

auth_bp = Blueprint('auth', __name__)

def login_required(view_page):
    def wrapper(*args, **kwargs):
        if ["username"] not in session:
            result = None
        else:
            print("You are logged in as: " + session["username"])
            result = view_page(*args, **kwargs)
        return result
    return wrapper

@auth_bp.route("/auth")
def auth():
    return render_template('auth.html')

@auth_bp.route('/login', methods=['POST'])
def login():
    ...
    return redirect(url_for('auth.auth'))

@auth_bp.route('/sign_up', methods=['POST'])
def sign_up():
    error = None
    username = request.form['username'].lower()
    password = request.form['password']
    user = sess.query(User).filter_by(username=username).first()
    if user:
        error = "User already exists"
    else:
        if password == request.form['confirm_password']:
            new_user = User(username=username, password=password)
            sess.add(new_user)
            sess.commit()
            session['username'] = username
            return redirect(url_for('posts.index'))
        else:
            error = "Passwords do not match"

    
    return redirect(url_for('auth.auth'))