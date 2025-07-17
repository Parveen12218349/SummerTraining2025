from functools import wraps

from flask import session, flash, redirect, url_for

from models import User

# Admin only decorator
def admin_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        user_id = session.get('user_id')
        user = User.query.get(user_id)
        if not user or not user.is_admin:
            flash("Admins only.")
            return redirect(url_for('home'))
        return f(*args, **kwargs)
    return wrapper


# Login required decorator
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please log in to continue.")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapper