from flask import Blueprint, flash, render_template
from flask_login import current_user, login_user
from .forms import LoginForm
from .models import User


bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('login'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
    
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return "Login failed!"

        login_user(user, remeber=form.remember_me.data)
        return "Login failed!"
    
    return render_template('auth/login.html', title='Sign In', form=form)


