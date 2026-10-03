from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Violation
from app.forms import ViolationForm, UpdateStatusForm
from app.utils import generate_qr_code
from datetime import datetime
import random
import string

violations_bp = Blueprint('violations', __name__)

def generate_challan_number():
    date_str = datetime.now().strftime('%Y%m%d')
    random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
    return f'CH-{date_str}-{random_str}'

@violations_bp.route('/')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    vehicle = request.args.get('vehicle', '')
    status = request.args.get('status', '')
    vtype = request.args.get('type', '')
    date_from = request.args.get('date_from', '')
    date_to = request.args.get('date_to', '')

    query = Violation.query
    if vehicle:
        query = query.filter(Violation.vehicle_number.ilike(f'%{vehicle}%'))
    if status:
        query = query.filter(Violation.status == status)
    if vtype:
        query = query.filter(Violation.violation_type == vtype)
    if date_from:
        query = query.filter(Violation.date >= datetime.strptime(date_from, '%Y-%m-%d').date())
    if date_to:
        query = query.filter(Violation.date <= datetime.strptime(date_to, '%Y-%m-%d').date())

    violations = query.order_by(Violation.created_at.desc()).paginate(page=page, per_page=10)
    return render_template('records.html', violations=violations, filters=request.args)

@violations_bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = ViolationForm()
    if form.validate_on_submit():
        challan_number = generate_challan_number()
        violation = Violation(
            challan_number=challan_number,
            vehicle_number=form.vehicle_number.data.upper(),
            violation_type=form.violation_type.data,
            location=form.location.data,
            date=form.date.data,
            fine_amount=form.fine_amount.data,
            status='Unpaid',
            officer_id=current_user.id
        )
        db.session.add(violation)
        db.session.commit()
        flash(f'Violation recorded. Challan No: {challan_number}', 'success')
        return redirect(url_for('violations.challan', challan_number=challan_number))
    return render_template('add_violation.html', form=form)

@violations_bp.route('/challan/<challan_number>')
@login_required
def challan(challan_number):
    violation = Violation.query.filter_by(challan_number=challan_number).first_or_404()
    verify_url = url_for('public.verify_challan', challan_number=challan_number, _external=True)
    qr_code = generate_qr_code(verify_url)
    return render_template('challan.html', violation=violation, qr_code=qr_code, verify_url=verify_url)

@violations_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    violation = Violation.query.get_or_404(id)
    form = UpdateStatusForm(obj=violation)
    if form.validate_on_submit():
        violation.status = form.status.data
        violation.payment_reference = form.payment_reference.data
        db.session.commit()
        flash('Violation status updated.', 'success')
        return redirect(url_for('violations.index'))
    return render_template('edit_violation.html', form=form, violation=violation)

@violations_bp.route('/export')
@login_required
def export():
    import csv
    from io import StringIO
    from flask import Response

    violations = Violation.query.all()
    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['Challan No', 'Vehicle', 'Type', 'Location', 'Date', 'Fine', 'Status', 'Officer'])
    for v in violations:
        cw.writerow([v.challan_number, v.vehicle_number, v.violation_type, v.location, v.date, v.fine_amount, v.status, v.officer.full_name])
    output = si.getvalue()
    return Response(output, mimetype='text/csv', headers={'Content-Disposition': 'attachment;filename=violations.csv'})