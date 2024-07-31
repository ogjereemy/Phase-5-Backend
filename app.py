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
            db.session.commit()
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

nut_args=reqparse.RequestParser()
nut_args.add_argument('date',type=date)
nut_args.add_argument('meal_type',type=enumerate)
nut_args.add_argument('calory_intake',type=int)
nut_args.add_argument('protein',type=int)
nut_args.add_argument('fat',type=int)
nut_args.add_argument('carbs',type=int)
nut_args.add_argument('notes',type=str)


class NutritionLogs(Resource):
    def get(self):
        nutlogs=NutritionLog.query.all()
        nutlogs_dict=[nutlog.to_dict() for nutlog  in nutlogs]
        response=make_response(jsonify(nutlogs_dict),200)
        return response
    
    def  post(self):
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        user_id = current_identity['id']
        if user_type=='user':
            data=nut_args.parse_args()
            new_nutlog=NutritionLog(
                user_id=user_id,
                date=data.get('date'),
                meal_type=data.get('meal_type'),
                calory_intake=data.get('calory_intake'),
                protein=data.get('protein'),
                fat=data.get('fat'),
                carbs=data.get('carbs'),
                notes=data.get('notes')

            )
            db.session.add(new_nutlog)
            db.session.commit()
            new_dict=new_nutlog.to_dict()
            response=make_response(jsonify(new_dict),201)
            return response


prog_args=reqparse.RequestParser()
prog_args.add_argument('date',type=date)
prog_args.add_argument('weight',type=int)
prog_args.add_argument('body_fat_percerntage',type=int)
prog_args.add_argument('muscle_mass',type=int)
prog_args.add_argument('notes',type=str)



class ProgressLogs(Resource):
    def get(self):
        proglogs=ProgressLog.query.all()
        proglogs_dict=[proglog.to_dict() for proglog in proglogs]
        response= make_response(jsonify(proglogs_dict),200)
        return response
    
    def post(self):
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        user_id = current_identity['id']
        data=prog_args.parse_args()
        if user_type=='user':
            new_prog=ProgressLog(
                user_id= user_id,
                date=data.get('date'),
                weight=data.get('weight'),
                body_fat_percentage=data.get('body_fat_percentage'),
                muscle_mass=data.get('muscle_mass'),
                notes=data.get('notes')

            )
            db.session.add(new_prog)
            db.session.commit()
            new_dict=new_prog.to_dict()
            response=make_response(jsonify(new_dict),201)
            return response


class Exercises(Resource):
    pass

class Workouts(Resource):
    pass

class WorkoutPlans(Resource):
    pass

class UserProfile(Resource):
    def get(self):
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        user_id = current_identity['id']
        if user_type=='user':
            user=User.query.filter_by(id=user_id).first()
            if user:
                user_dict=user.to_dict()
                response=make_response(jsonify(user_dict),200)
                return response
            else:
                response=make_response(jsonify({'msg':'User not found'}),404)
                return response
            
    def patch(self):
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        user_id = current_identity['id']
        if user_type=='user':
            user=User.query.filter_by(id=user_id).first()
            if user:
                username=request.get_json()['username']
                photo=request.get_json()['photo']
                user.username=username
                user.photo=photo
                db.session.commit()
                user_dict=user.to_dict()
                response=make_response(jsonify(user_dict),200)
                return response
            else:
                response=make_response(jsonify({'msg':'User not found'}),404)
                return response
                            
                            
                    

class CoachProfile(Resource):
    def get(self):
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        user_id = current_identity['id']
        if user_type=='coach':
            coach=Coach.query.filter_by(id=user_id).first()
            if coach:
                coach_dict=coach.to_dict()
                response=make_response(jsonify(coach_dict),200)
                return response
            else:
                response=make_response(jsonify({'msg':'Coach not found'}),404)
                return response
            

    def patch(self):
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        user_id = current_identity['id']
        if user_type=='coach':
            coach=Coach.query.filter_by(id=user_id).first()
            if coach:
                username=request.get_json()['username']
                photo=request.get_json()['photo']
                bio=request.get_json()['bio']
                specialities=request.get_json()['specialities']
                coach.username=username
                coach.photo=photo
                coach.bio=bio
                coach.specialities=specialities
                db.session.commit()
                coach_dict=coach.to_dict()
                response=make_response(jsonify({coach_dict}),200)
                return response
            else:
                response=make_response(jsonify({'msg':'Coach not found'}),404)
                return response

    

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





