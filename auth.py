from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, current_user
from flask import Blueprint,jsonify,request,make_response
from flask_restful import Api, Resource, reqparse
from models import *
from config import *




auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')
auth_api = Api(auth_bp)



@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    user_id = identity["id"]
    user_type = identity["type"]
    if user_type == "user":
        return User.query.filter_by(id=user_id).first()
    elif user_type == "coach":
        return Coach.query.filter_by(id=user_id).first()
    return None



register_args = reqparse.RequestParser()
register_coach_args = reqparse.RequestParser()
register_args.add_argument('username', type=str, required=True, help='Username is required')
register_args.add_argument('email', type=str, required=True, help='Email is required')
register_args.add_argument('password1', type=str, required=True, help='Password is required')
register_args.add_argument('password2', type=str, required=True, help='Password confirmation is required')
register_args.add_argument('photo', type=str, required=True, help='Photo is required')
register_args.add_argument('coach_id', type=int, required=True, help='Coach_id is required')

register_coach_args.add_argument('username', type=str, required=True, help='Username is required')
register_coach_args.add_argument('email', type=str, required=True, help='Email is required')
register_coach_args.add_argument('password1', type=str, required=True, help='Password is required')
register_coach_args.add_argument('password2', type=str, required=True, help='Password confirmation is required')
register_coach_args.add_argument('photo', type=str, required=True, help='Photo is required')
register_coach_args.add_argument('bio', type=str, required=True, help='Bio is required')
register_coach_args.add_argument('specialities', type=str, required=True, help='Specialities is required')
register_coach_args.add_argument('is_admin', type=bool, required=True, help='is_admin is required')


class Signup(Resource):
    def post(self):
        
        if 'coach_id' in request.json:
            data = register_args.parse_args()
            if data.get("password1") != data.get("password2"):
                return {"msg": "Passwords don't match"}, 400
            user = User.query.filter_by(email=data.get('email')).first()
            if user:
                return {"msg":"User already exists."},401
            hashed_password = bcrypt.generate_password_hash(data.get('password1')).decode('utf-8')
            new_user = User(
                username=data.get('username'),
                email=data.get('email'),
                _password_hash=hashed_password,
                photo=data.get('photo'),
                coach_id=data.get('coach_id')
            )
            db.session.add(new_user)
            db.session.commit()
            response =make_response(jsonify(new_user.to_dict()), 201)
            return response
        else:
            data = register_coach_args.parse_args()
            if data.get("password1") != data.get("password2"):
                return {"msg": "Passwords don't match"}, 400
            coach = Coach.query.filter_by(email=data.get('email')).first()
            if coach:
                return {"msg":"Coach already exists."},401
            hashed_password = bcrypt.generate_password_hash(data.get('password1')).decode('utf-8')
            new_coach = Coach(
                username=data.get('username'),
                email=data.get('email'),
                _password_hash=hashed_password,
                photo=data.get('photo'),
                bio=data.get('bio'),
                specialities=data.get('specialities'),
                is_admin=data.get('is_admin')
            )
            db.session.add(new_coach)
            db.session.commit()
            response=make_response(jsonify(new_coach.to_dict()), 201)
            return response

login_args = reqparse.RequestParser()
login_coach_args = reqparse.RequestParser()
login_args.add_argument('email', type=str, required=True, help='Email is required')
login_args.add_argument('password', type=str, required=True, help='Password is required')
login_coach_args.add_argument('email', type=str, required=True, help='Email is required')
login_coach_args.add_argument('password', type=str, required=True, help='Password is required')





class Login(Resource):
    def post(self):
        data = login_args.parse_args()
        data1 = login_coach_args.parse_args()   
        
        if 'username' in request.json:               
                coach = Coach.query.filter_by(email=data1.get('email')).first()
                if not bcrypt.check_password_hash(coach._password_hash, data1.get('password')):
                    return {"msg": "Invalid email or password"}, 401
                token =create_access_token(identity={"id":coach.id , "type":"coach"})
                refresh_token = create_refresh_token(identity={"id":coach.id , "type":"coach"})
                return {"token": token, 'refresh_token': refresh_token}, 200
        else:  
            user = User.query.filter_by(email=data.get('email')).first()
            if not bcrypt.check_password_hash(user._password_hash, data.get('password')):
                return {"msg": "Invalid email or password"}, 401
            token=create_access_token(identity={"id":user.id , "type":"user"})
            refresh_token = create_refresh_token(identity={"id":user.id , "type":"user"})
            return {"token": token, 'refresh_token': refresh_token}, 200
      
            
        

    @jwt_required(refresh=True)
    def get():
        current_identity = get_jwt_identity()
        new_access_token = create_access_token(identity=current_identity)
        return jsonify(access_token=new_access_token)

    

# Access to certain resource
auth_api.add_resource(Signup, '/signup')
auth_api.add_resource(Login, '/login')
