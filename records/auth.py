from flask import Blueprint, flash, render_template
from flask_login import current_user, login_user
from .forms import LoginForm
#TODO: Configure Admin login 
#TODO: Add URl routes 

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    return render_template('login.html', title='Sign In', form=form)