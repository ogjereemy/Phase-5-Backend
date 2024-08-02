from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, current_user
from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from models import *
# from flask_bcrypt import Bcrypt
from config import *


# auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')
auth_api = Api(auth_bp)
# jwt = JWTManager() 

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return User.query.filter_by(id=identity).first()

# bcrypt = Bcrypt()

register_args = reqparse.RequestParser()
register_args.add_argument('username', type=str, required=True, help='Username is required')
register_args.add_argument('email', type=str, required=True, help='Email is required')
register_args.add_argument('password1', type=str, required=True, help='Password is required')
register_args.add_argument('password2', type=str, required=True, help='Password confirmation is required')
register_args.add_argument('photo', type=str, required=True, help='Photo is required')
register_args.add_argument('coach_id', type=int, required=True, help='Coach_id is required')
register_args.add_argument('bio', type=str, required=True, help='Bio is required')
register_args.add_argument('specialities', type=str, required=True, help='Specialities is required')
register_args.add_argument('is_admin', type=bool, required=True, help='is_admin is required')

# Registering
class Signup(Resource):
    def post(self):
        data = register_args.parse_args()
        
        if data.get("password1") != data.get("password2"):
            return {"msg": "Passwords don't match"}, 400
        hashed_password = User.password_hash(data.get('password1'))
        coach_id=data.get('coach_id')
        if coach_id:      ##$Distinguishes a coach from a user  based on whether there is a coach_id field in the request body
            new_user = User(username=data.get('username'),
                        email=data.get('email'),
                        password=hashed_password,
                        photo=data.get('photo'), 
                        coach_id=data.get('coach_id')
                        )
        
            db.session.add(new_user)
            db.session.commit()
            return jsonify({"msg": "You have signed up successfully"}), 201
        else:
            if data.get("password1") != data.get("password2"):
                return {"msg": "Passwords don't match"}, 400
        hashed_password = Coach.password_hash(data.get('password1'))
        new_coach = Coach(username=data.get('username'),
                        email=data.get('email'),
                        password=hashed_password,
                        photo=data.get('photo'),                         
                        bio=data.get('bio'),
                        specialities=data.get('specialities'),
                        is_admin=data.get('is_admin')
                        )
        db.session.add(new_coach)
        db.session.commit()
        return jsonify({"msg": "You have signed up successfully"}), 201


login_args = reqparse.RequestParser()
login_args.add_argument('email', type=str, required=True, help='Email is required')
login_args.add_argument('password', type=str, required=True, help='Password is required')

#login
def authenticate_user(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.authenticate(password):
        return {"type": "user", "id": user.id}
    return None

def authenticate_coach(email, password):
    coach = Coach.query.filter_by(email=email).first()
    if coach and coach.authenticate(password):
        return {"type": "coach", "id": coach.id}
    return None

class Login(Resource):
    def post(self):
        data = login_args.parse_args()
        password=data.get('password')
        email=data.get('email')
        # user = User.query.filter_by(email=email)).first()
        # if not user or not User.authenticate(password):
        #     return {"msg": "Invalid email or password"}, 401
        identity = authenticate_user(email, password) or authenticate_coach(email, password)
        if not identity:
            return jsonify({"msg": "Bad username or password"}), 401
    

        
        token = create_access_token(identity=identity)
        refresh_token = create_refresh_token(identity=identity)
        return {"token": token, 'refresh_token': refresh_token}, 200
    
    @jwt_required(refresh=True)
    def get():
        current_identity = get_jwt_identity()
        new_access_token = create_access_token(identity=current_identity)
        return jsonify(access_token=new_access_token)

    
    # @jwt_required()
    # def get(self):
    #     user = current_user
    #     return {'email': user.email}, 200

# Access to certain resource
auth_api.add_resource(Signup, '/signup')
auth_api.add_resource(Login, '/login')
