import os
from flask import Flask, request, session,jsonify,make_response , Blueprint
from flask_restful import Api,Resource, reqparse
from flask_jwt_extended import jwt_required,current_user,get_jwt_identity,JWTManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

from sqlalchemy import MetaData
app = Flask(__name__)

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db =SQLAlchemy(metadata=metadata)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


db.init_app(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app)

app_bp = Blueprint('app_bp', __name__, url_prefix='/app')
auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')