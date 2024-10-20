from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, current_user, get_jwt_identity
from flask import Blueprint, jsonify, request, make_response,url_for
from flask_restful import Api, Resource, reqparse
from models import *
from config import *
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
from dotenv import load_dotenv
load_dotenv()


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
register_args.add_argument('username', type=str, required=True, help='Username is required')
register_args.add_argument('email', type=str, required=True, help='Email is required')
register_args.add_argument('password1', type=str, required=True, help='Password is required')
register_args.add_argument('password2', type=str, required=True, help='Password confirmation is required')
register_args.add_argument('photo', type=str, required=True, help='Photo is required')
register_args.add_argument('coach_id', type=int, required=True, help='Coach_id is required')
register_args.add_argument('coach_name', type=str, required=True, help='Coach_id is required')

register_coach_args = reqparse.RequestParser()
register_coach_args.add_argument('username', type=str, required=True, help='Username is required')
register_coach_args.add_argument('email', type=str, required=True, help='Email is required')
register_coach_args.add_argument('password1', type=str, required=True, help='Password is required')
register_coach_args.add_argument('password2', type=str, required=True, help='Password confirmation is required')
register_coach_args.add_argument('photo', type=str, required=True, help='Photo is required')
register_coach_args.add_argument('bio', type=str, required=False, help='Bio is required for coaches')
register_coach_args.add_argument('specialities', type=str, required=False, help='Specialities is required for coaches')
register_coach_args.add_argument('is_admin', type=bool, required=True, help='is_admin is required')

class Signup(Resource):
    def post(self):
        if 'coach_id' in request.json:
            data = register_args.parse_args()
            if data.get("password1") != data.get("password2"):
                return {"msg": "Passwords don't match"}, 400
            user = User.query.filter_by(email=data.get('email')).first()
            if user:
                return {"msg": "User already exists."}, 401
            hashed_password = bcrypt.generate_password_hash(data.get('password1')).decode('utf-8')
            new_user = User(
                username=data.get('username'),
                email=data.get('email'),
                _password_hash=hashed_password,
                photo=data.get('photo'),
                coach_id=data.get('coach_id'),
                coach_name=data.get('coach_name')
            )
            db.session.add(new_user)
            db.session.commit()
            response = make_response(jsonify(new_user.to_dict()), 201)
            return response
        else:
            data = register_coach_args.parse_args()
            if data.get("password1") != data.get("password2"):
                return {"msg": "Passwords don't match"}, 400
            coach = Coach.query.filter_by(email=data.get('email')).first()
            if coach:
                return {"msg": "Coach already exists."}, 401
            
            # Ensure bio and specialities are provided if the user is a coach
            if not data.get('bio'):
                return {"msg": "Bio is required for coaches."}, 400
            if not data.get('specialities'):
                return {"msg": "Specialities are required for coaches."}, 400

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
            response = make_response(jsonify(new_coach.to_dict()), 201)
            return response

login_args = reqparse.RequestParser()
login_args.add_argument('email', type=str, required=True, help='Email is required')
login_args.add_argument('password', type=str, required=True, help='Password is required')

login_coach_args = reqparse.RequestParser()
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
            token = create_access_token(identity={"id": coach.id, "type": "coach"})
            refresh_token = create_refresh_token(identity={"id": coach.id, "type": "coach"})
            return {"token": token, 'refresh_token': refresh_token}, 200
        else:  
            user = User.query.filter_by(email=data.get('email')).first()
            if not bcrypt.check_password_hash(user._password_hash, data.get('password')):
                return {"msg": "Invalid email or password"}, 401
            token = create_access_token(identity={"id": user.id, "type": "user"})
            refresh_token = create_refresh_token(identity={"id": user.id, "type": "user"})
            return {"token": token, 'refresh_token': refresh_token}, 200

    @jwt_required(refresh=True)
    def get(self):
        current_identity = get_jwt_identity()
        new_access_token = create_access_token(identity=current_identity)
        return jsonify(access_token=new_access_token)
    

class ResetPasswordRequest(Resource):
        def post(self):
            email = request.json.get('email')
            user = User.query.filter_by(email=email).first()

            if user:
                token = s.dumps(user.email, salt='password-reset-salt')
                reset_url = url_for('auth_bp.reset_password', token=token, _external=True)
                msg = Message("Password Reset Request", recipients=[user.email])
                msg.body = f'Click the link to reset your password: {reset_url}'
                mail.send(msg)
                return jsonify({'message': 'Password reset email sent'}), 200
            else:
                return jsonify({'message': 'Email not found'}), 404

class ResetPassword(Resource):
    def get(self, token):
        try:
            email = s.loads(token, salt='password-reset-salt', max_age=3600)  # 1 hour expiration
        except:
            return jsonify({'message': 'The reset link is invalid or has expired'}), 400

        return jsonify({'message': 'Please submit your new password'}), 200

    def post(self, token):
        try:
            email = s.loads(token, salt='password-reset-salt', max_age=3600)  # 1 hour expiration
        except:
            return jsonify({'message': 'The reset link is invalid or has expired'}), 400

        new_password = request.json.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            user._password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            db.session.commit()
            return jsonify({'message': 'Your password has been updated'}), 200
        else:
            return jsonify({'message': 'User not found'}), 404

# Access to certain resource
auth_api.add_resource(Signup, '/signup')
auth_api.add_resource(Login, '/login')
auth_api.add_resource(ResetPasswordRequest, '/reset_password_request')
auth_api.add_resource(ResetPassword, '/reset_password/<token>')
