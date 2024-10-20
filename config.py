import os
from flask import Flask, request, session,jsonify,make_response , Blueprint
from flask_restful import Api,Resource, reqparse
from flask_jwt_extended import jwt_required,current_user,get_jwt_identity,JWTManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

from sqlalchemy import MetaData

from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db =SQLAlchemy(metadata=metadata)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
app.config['SECRET_KEY'] = os.urandom(24).hex()
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'fitt.track1@gmail.com'
app.config['MAIL_PASSWORD'] = 'Jeremy@100'
app.config['MAIL_DEFAULT_SENDER'] = 'fitt.track1@gmail.com'

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'bf33b4e2a163a29294876531f6ba53ead9')

mail = Mail(app)

db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)

# app_bp = Blueprint('app_bp', __name__, url_prefix='/app')
# auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

# app.register_blueprint(app_bp)
# app.register_blueprint(auth_bp)