from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import Officer
from app.forms import LoginForm, RegistrationForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        officer = Officer.query.filter_by(email=form.email.data).first()
        if officer and officer.check_password(form.password.data):
            login_user(officer, remember=form.remember.data)
            flash('Logged in successfully.', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.dashboard'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = RegistrationForm()
    if form.validate_on_submit():
        if Officer.query.filter_by(email=form.email.data).first():
            flash('Email already registered.', 'danger')
            return redirect(url_for('auth.register'))
        if Officer.query.filter_by(badge_id=form.badge_id.data).first():
            flash('Badge ID already exists.', 'danger')
            return redirect(url_for('auth.register'))
        is_first = Officer.query.count() == 0
        officer = Officer(
            badge_id=form.badge_id.data,
            full_name=form.full_name.data,
            rank=form.rank.data,
            email=form.email.data,
            is_admin=is_first
        )
        officer.set_password(form.password.data)
        db.session.add(officer)
        db.session.commit()
        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('public.verify'))

@auth_bp.route('/officers')
@login_required
def officers():
    if not current_user.is_admin:
        flash('Access denied. Admin only.', 'danger')
        return redirect(url_for('main.dashboard'))
    officers_list = Officer.query.order_by(Officer.created_at.desc()).all()
    return render_template('officers.html', officers=officers_list)