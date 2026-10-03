from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return Officer.query.get(int(user_id))

class Officer(UserMixin, db.Model):
    __tablename__ = 'officers'
    id = db.Column(db.Integer, primary_key=True)
    badge_id = db.Column(db.String(20), unique=True, nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    rank = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    violations = db.relationship('Violation', backref='officer', lazy=True)

    @property
    def initials(self):
        parts = self.full_name.split()
        if len(parts) >= 2:
            return (parts[0][0] + parts[-1][0]).upper()
        return self.full_name[:2].upper()

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Violation(db.Model):
    __tablename__ = 'violations'
    id = db.Column(db.Integer, primary_key=True)
    challan_number = db.Column(db.String(30), unique=True, nullable=False, index=True)
    vehicle_number = db.Column(db.String(20), nullable=False, index=True)
    violation_type = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date, nullable=False)
    fine_amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(10), default='Unpaid', nullable=False)
    payment_reference = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    officer_id = db.Column(db.Integer, db.ForeignKey('officers.id'), nullable=False)

    def __repr__(self):
        return f'<Violation {self.challan_number} - {self.vehicle_number}>'