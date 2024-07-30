import os
from flask import Flask, request, session,jsonify,make_response , Blueprint
from flask_restful import Api,Resource, reqparse
from flask_jwt_extended import jwt_required,current_user,get_jwt_identity,JWTManager
# from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
# from flask_cors import CORS
from models import *
from datetime import timedelta
from config import *



app.config['SECRET_KEY'] = 'bf33b4e2a163a29294876531f6ba53ead9'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=25)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=90)
app_api = Api(app_bp)

app.register_blueprint(app_bp)
# app.register_blueprint(auth_bp)

class Users(Resource):
    def get(self):
        users=User.query.all()
        users_dict= [user.to_dict()for user in users]
        response = make_response(jsonify(users_dict),200)
        return response
    
    def delete(self):
        user_id= request.get_json()['user_id']
        user=User.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()
        response=make_response(jsonify({'msg':'User deleted successfully'}),200)
        return response
        

goals_args=reqparse.RequestParser()
goals_args.add_argument('title',type=str)
goals_args.add_argument('description',type=str)
goals_args.add_argument('target_date',type=date)
goals_args.add_argument('achieved',type=bool)

class Goals(Resource):
    def post(self):
        data=goals_args.parse_args()
        # user_id =get_jwt_identity()

        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        user_id = current_identity['id']

        if user_type == 'user':

            new_goal=Goal(
                user_id=user_id,
                title=data.get('title'),
                description=data.get('description'),
                target_date= data.get('target_date'),
                achieved=data.get('achieved')
        )
            db.session.add(new_goal)
            db.session.commit()
            new_goal_dict=new_goal.to_dict()
            response = make_response(jsonify(new_goal_dict),201)
            return response



    def get(self):
        goals=Goal.query.all()
        goals_dict=[goal.to_dict()for goal in goals]
        response=make_response(jsonify(goals_dict),200)
        return response

    def patch(self):
        data=goals_args.parse_args()
        description= data.get('description')
        target_date= data.get('target_date')
        goal_id=request.get_json()['goal_id']
        goal=Goal.query.filter_by(id=goal_id)
        if goal :
            goal.description=description
            goal.target_date=target_date
            goal_dict=goal.to_dict()
            response=make_response(jsonify(goal_dict),200)
            return response
        else : 
            response=make_response(jsonify({'msg':'Goal not found'}),404)
            return response

    def delete(self):
        # user_id=get_jwt_identity()
        goal_id=request.get_json()['goal_id']
        goal=Goal.query.filter_by(id=goal_id).first()
        db.session.delete(goal)
        db.session.commit()
        response=make_response(jsonify({'msg':'Goal deleted successfully'}),200)
        return response

        

class Coaches(Resource):
    def get(self):
        coaches=Coach.query.all()
        coaches_dict=[coach.to_dict()for coach in coaches]
        response=make_response(jsonify(coaches_dict),200)
        return response
    def delete(self):
        # current_identity = get_jwt_identity()
        # user_type = current_identity['type']
        # user_id = current_identity['id']
        # if user_type=='coach':
            coach_id=request.get_json()['coach_id']
            coach=Coach.query.filter_by(id=coach_id).first()
            if coach:
                db.session.delete(coach)
                db.session.commit()
                response=make_response(jsonify({'msg':'Coach removed successfully'}),200)
                return response
            else: 
                return make_response(jsonify({'msg':'Coach not found'}),404)


class NutritionLogs(Resource):
    pass

class ProgressLogs(Resource):
    pass

class Exercises(Resource):
    pass

class Workouts(Resource):
    pass

class WorkoutPlans(Resource):
    pass

class UserProfile(Resource):
    pass

class CoachProfile(Resource):
    pass

app_api.add_resource(Goals,'/goals')
app_api.add_resource(Workouts,'/workouts')
app_api.add_resource(Exercises,'/exercises')
app_api.add_resource(NutritionLogs,'/nutrition_logs')
app_api.add_resource(ProgressLogs,'/progress_logs')  
app_api.add_resource(WorkoutPlans,'/workout_plans')
app_api.add_resource(Users,'/users') ##coaches
app_api.add_resource(Coaches,'/coaches') #admin
app_api.add_resource(UserProfile,'/profile') ##user
app_api.add_resource(CoachProfile,'/coach_Profile')






if __name__ == '__main__':
    app.run(port=5555, debug=True)





