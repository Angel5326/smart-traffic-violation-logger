from flask import Blueprint, render_template
from flask_login import login_required
from app.models import Violation
from app import db
from sqlalchemy import func
from datetime import datetime, timedelta

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/dashboard')
@login_required
def dashboard():
    total_violations = Violation.query.count()
    unpaid_count = Violation.query.filter_by(status='Unpaid').count()
    paid_count = Violation.query.filter_by(status='Paid').count()
    total_fine = db.session.query(func.sum(Violation.fine_amount)).scalar() or 0
    collected_fine = db.session.query(func.sum(Violation.fine_amount)).filter_by(status='Paid').scalar() or 0

    today = datetime.utcnow().date()
    labels = []
    data = []
    for i in range(6, -1, -1):
        day = today - timedelta(days=i)
        count = Violation.query.filter(Violation.date == day).count()
        labels.append(day.strftime('%b %d'))
        data.append(count)

    recent = Violation.query.order_by(Violation.created_at.desc()).limit(5).all()

    return render_template('dashboard.html',
                           total_violations=total_violations,
                           unpaid_count=unpaid_count,
                           paid_count=paid_count,
                           total_fine=total_fine,
                           collected_fine=collected_fine,
                           labels=labels,
                           data=data,
                           recent=recent)