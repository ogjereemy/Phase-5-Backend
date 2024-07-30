import os
from flask import Flask, request, session,jsonify,make_response , Blueprint
from flask_restful import Api,Resource, reqparse
from flask_jwt_extended import jwt_required,current_user,get_jwt_identity,JWTManager
# from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
# from flask_cors import CORS
from models import db
from datetime import timedelta
from config import *


app.config['SECRET_KEY'] = 'bf33b4e2a163a29294876531f6ba53ead9'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=25)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=90)
app_api = Api(app_bp)

app.register_blueprint(app_bp)
# app.register_blueprint(auth_bp)







if __name__ == '__main__':
    app.run(port=5555, debug=True)





