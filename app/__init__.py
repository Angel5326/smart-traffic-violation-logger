from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from datetime import datetime
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()          # 👈 NEW

login_manager.login_view = 'auth.login'
login_manager.login_message_category = 'warning'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)        # 👈 NEW — registers {{ csrf_token() }} globally

    # Make `now()` available inside all templates
    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow}

    from app.auth.routes import auth_bp
    from app.main.routes import main_bp
    from app.violations.routes import violations_bp
    from app.public.routes import public_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(violations_bp, url_prefix='/violations')
    app.register_blueprint(public_bp, url_prefix='/public')

    with app.app_context():
        db.create_all()

    return app