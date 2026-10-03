from flask import Blueprint, render_template, abort, request
from app.models import Violation

public_bp = Blueprint('public', __name__)

@public_bp.route('/verify', methods=['GET'])
def verify():
    challan_number = request.args.get('challan_number', '')
    violation = None
    if challan_number:
        violation = Violation.query.filter_by(challan_number=challan_number).first()
        if not violation:
            abort(404)
    return render_template('verify.html', violation=violation, challan_number=challan_number)

@public_bp.route('/verify/<challan_number>')
def verify_challan(challan_number):
    violation = Violation.query.filter_by(challan_number=challan_number).first_or_404()
    return render_template('verify.html', violation=violation)