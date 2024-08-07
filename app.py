import os
from flask import Flask, request, session,jsonify,make_response , Blueprint
from flask_restful import Api,Resource, reqparse
from flask_jwt_extended import jwt_required,current_user,get_jwt_identity,JWTManager
# from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
# from flask_cors import CORS
from models import *
from datetime import timedelta,datetime
from config import *
from auth import auth_bp


app.config['SECRET_KEY'] = 'bf33b4e2a163a29294876531f6ba53ead9'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=25)
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=60)

app_bp = Blueprint('app_bp', __name__, url_prefix='/app')
app_api = Api(app_bp)
app.register_blueprint(app_bp)
app.register_blueprint(auth_bp)


 

class Users(Resource):
    @jwt_required()
    def get(self):##for coaches
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        coach_id = current_identity['id']

        if user_type == 'coach':
            users=User.query.filter_by(coach_id=coach_id).all()
            users_dict= [user.to_dict()for user in users]
            response = make_response(jsonify(users_dict),200)
            return response
        else: 
            response=make_response(jsonify({"msg":"Unauthorized Access"}),401)
            return response

    @jwt_required()     
    def delete(self):##only coaches can delete users
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        coach_id = current_identity['id']
        if user_type == 'coach':
            user_id= request.get_json()['user_id']
            user=User.query.filter_by(id=user_id,coach_id=coach_id).first()
            db.session.delete(user)
            db.session.commit()
            response=make_response(jsonify({'msg':'User deleted successfully'}),200)
            return response
        else: 
            response=make_response(jsonify({"msg":"Unauthorized Access"}),401)
            return response
        

goals_args=reqparse.RequestParser()
goals_args.add_argument('title',type=str)
goals_args.add_argument('description',type=str)
goals_args.add_argument('achieved',type=bool)

class Goals(Resource):##for users
    @jwt_required()
    def post(self):
        data=goals_args.parse_args()        
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        user_id = current_identity['id']

        if user_type == 'user':
            datestr=request.get_json()['target_date']
            target_date = datetime.strptime(datestr, '%Y-%m-%d').date()
            
            new_goal=Goal(
                user_id=user_id,
                title=data.get('title'),
                description=data.get('description'),
                target_date=target_date,
                achieved=data.get('achieved')
        )
            db.session.add(new_goal)
            db.session.commit()
            new_goal_dict=new_goal.to_dict()
            response = make_response(jsonify(new_goal_dict),201)
            return response


    @jwt_required()##for users
    def get(self):        
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        user_id = current_identity['id']
        if user_type =='user':
            goals=Goal.query.filter_by(user_id=user_id).all()
            goals_dict=[goal.to_dict()for goal in goals]
            response=make_response(jsonify(goals_dict),200)
            return response
    @jwt_required()
    def patch(self):##for users
        data=goals_args.parse_args()
        description= data.get('description')        
        datestr=request.get_json()['target_date']
        target_date = datetime.strptime(datestr, '%Y-%m-%d').date()
            
        goal_id=request.get_json()['goal_id']
        goal=Goal.query.filter_by(id=goal_id).first()
        if goal :
            goal.description=description
            goal.target_date=target_date ##(YYYY-MM-DD)
            db.session.commit()
            goal_dict=goal.to_dict()
            response=make_response(jsonify(goal_dict),200)
            return response
        else : 
            response=make_response(jsonify({'msg':'Goal not found'}),404)
            return response
    @jwt_required()
    def delete(self):##for users        
        goal_id=request.get_json()['goal_id']
        goal=Goal.query.filter_by(id=goal_id).first()
        db.session.delete(goal)
        db.session.commit()
        response=make_response(jsonify({'msg':'Goal deleted successfully'}),200)
        return response

        

class Coaches(Resource):
    @jwt_required()
    def get(self):##for coaches
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        coach_id = current_identity['id']

        if user_type == 'coach':
            coach=Coach.query.filter_by(id=coach_id).first()
            if coach and coach.is_admin== True:
                coaches=Coach.query.all()
                coaches_dict=[coach.to_dict()for coach in coaches]
                response=make_response(jsonify(coaches_dict),200)
                return response
        else:
            response=make_response(jsonify({"msg":"Unauthorized Access"}),401)
            return response
    @jwt_required()
    def delete(self): ##for coaches
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        coach_id = current_identity['id']
        if user_type=='coach':
            coach=Coach.query.filter_by(id=coach_id).first()
            if coach and coach.is_admin== True:
                coach_id=request.get_json()['coach_id']
                coach=Coach.query.filter_by(id=coach_id).first()
                if coach:
                    db.session.delete(coach)
                    db.session.commit()
                    response=make_response(jsonify({'msg':'Coach removed successfully'}),200)
                    return response
                else: 
                    return make_response(jsonify({'msg':'Coach not found'}),404)
        else:
            response=make_response(jsonify({"msg":"Unauthorized Access"}),401)
            return response        
            

nut_args=reqparse.RequestParser()
# nut_args.add_argument('date',type=date)
# nut_args.add_argument('meal_type',type=enumerate)
nut_args.add_argument('calory_intake',type=int)
nut_args.add_argument('protein',type=int)
nut_args.add_argument('fat',type=int)
nut_args.add_argument('carbs',type=int)
nut_args.add_argument('notes',type=str)


class NutritionLogs(Resource):
    @jwt_required()
    def get(self):##for users
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        user_id = current_identity['id']

        if user_type == 'user':
            nutlogs=NutritionLog.query.filter_by(user_id=user_id).all()
            nutlogs_dict=[nutlog.to_dict() for nutlog  in nutlogs]
            response=make_response(jsonify(nutlogs_dict),200)
            return response
    @jwt_required()
    def  post(self):##for users
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        user_id = current_identity['id']
        if user_type=='user':
            data=nut_args.parse_args()
            datestr=request.get_json()['date']
            nut_date = datetime.strptime(datestr, '%Y-%m-%d').date()
            
            new_nutlog=NutritionLog(
                user_id=user_id,
                date=nut_date,
                meal_type=request.get_json()['meal_type'],
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
# prog_args.add_argument('date',type=datetime)
prog_args.add_argument('weight',type=int)
prog_args.add_argument('body_fat_percentage',type=int)
prog_args.add_argument('muscle_mass',type=int)
prog_args.add_argument('notes',type=str)



class ProgressLogs(Resource):
    @jwt_required()
    def get(self):##for users
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        user_id = current_identity['id']

        if user_type == 'user':
            proglogs=ProgressLog.query.filter_by(user_id=user_id).all()
            proglogs_dict=[proglog.to_dict() for proglog in proglogs]
            response= make_response(jsonify(proglogs_dict),200)
            return response
    @jwt_required()
    def post(self):##for users
        datestr=request.get_json()['date']
        progdate= datetime.strptime(datestr, '%Y-%m-%d').date()
            
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        user_id = current_identity['id']
        data=prog_args.parse_args()
        if user_type=='user':
            new_prog=ProgressLog(
                user_id= user_id,
                date=progdate,
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
    @jwt_required()
    def post(self): ## for coaches
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        coach_id = current_identity['id']
        if user_type == 'coach':
            coach=Coach.query.filter_by(id=coach_id).first()
            if coach:
                new_exercise =Exercise(
                workout_id=request.get_json()['workout_id'] ,
                name=request.get_json()['name'],
                sets=request.get_json()['sets'] ,
                reps= request.get_json()['reps'],
                weight= request.get_json()['weight'],
                description=request.get_json()['description']
            )
            db.session.add(new_exercise)
            db.session.commit()
            new_dict=new_exercise.to_dict()
            response=make_response(jsonify(new_dict),201)
            return  response
        else:
            response=make_response(jsonify({"msg":"Unauthorized Access"}),401)
            return response


    @jwt_required()
    def get(self): ## for everybody
        exercises = Exercise.query.all()
        exercises_dict=[exercise.to_dict() for exercise in exercises]
        response=make_response(jsonify(exercises_dict),200)
        return response
    @jwt_required()
    def patch(self): ## for coaches
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        coach_id = current_identity['id']
        if user_type == 'coach':
            coach=Coach.query.filter_by(id=coach_id).first()
            if coach:
                exercise_id=request.get_json()['exercise_id']
                exercise=Exercise.query.filter_by(id=exercise_id).first()
                if exercise:
                    exercise.sets=request.get_json()['sets']
                    exercise.reps=request.get_json()['reps']
                    exercise.weight=request.get_json()['weight']
                    db.session.commit()
                    exe_dict=exercise.to_dict()
                    response=make_response(jsonify(exe_dict),200)
                    return response
                else:
                    response=make_response(jsonify({'msg':'Exercise not found'}),404)
                    return response
        else:
            response=make_response(jsonify({"msg":"Unauthorized Access"}),401)
            return response


class Workouts(Resource):
    @jwt_required()
    def post(self): ## for coaches
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        coach_id = current_identity['id']
        data=request.get_json()
        if user_type=='coach':
            new_workout=Workout(
                workout_plan_id= data.get('workout_plan_id'),
                user_id=data.get('user_id'),
                coach_id=coach_id,
                title= data.get('title'),
                day_of_week=data.get('day_of_week'), ##the days of the week that the workout is supposed to be done , type(str)                                   
                exercises=data.get('exercises')
            )
            db.session.add(new_workout)
            db.session.commit()
            new_dict=new_workout.to_dict()
            response=make_response(jsonify(new_dict),201)
            return response

    @jwt_required()   
    def get(self): ## for users
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        user_id = current_identity['id']
        if user_type == 'user':            
            workouts=Workout.query.filter_by(user_id=user_id).all()
            work_dict=[workout.to_dict() for workout in workouts]
            response=make_response(jsonify(work_dict),200)
            return response
    @jwt_required()
    def patch(self):## for coaches
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        coach_id = current_identity['id']
        if user_type == 'coach':
            coach=Coach.query.filter_by(id=coach_id).first()
            if coach:
                workout_id=request.get_json()['workout_id']
                workout=Workout.query.filter_by(id=workout_id).first()
                if workout:
                    workout.title=request.get_json()['title']
                    workout.day_of_week =request.get_json()['day_of_week']
                    workout.exercises=request.get_json()['exercises']
                    db.session.commit()
                    work_dict=workout.to_dict()
                    response=make_response(jsonify(work_dict),200)
                    return response

                else :
                    response=make_response(jsonify({'msg':'Workout not found'}),404)
                    return response
        else:
            response=make_response(jsonify({"msg":"Unauthorized Access"}),401)
            return response

    @jwt_required()   
    def delete(self):## for coaches
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        coach_id = current_identity['id']
        if user_type == 'coach':
            coach=Coach.query.filter_by(id=coach_id).first()
            if coach:
                workout_id=request.get_json()['workout_id']
                workout=Workout.query.filter_by(id=workout_id).first()
                if workout:
                    db.session.delete(workout)
                    db.session.commit()
                    response=make_response(jsonify({'msg':'Workout deleted successfully.'}),200)
                    return response
                else :
                    response=make_response(jsonify({'msg':'Workout not found'}),404)
                    return response
        
        else:
            response=make_response(jsonify({"msg":"Unauthorized Access"}),401)
            return response



class WorkoutPlans(Resource):
    @jwt_required()
    def post(self):   ## for coaches
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        coach_id = current_identity['id']
        data=request.get_json()
        if user_type=='coach':
            new_workoutplan=WorkoutPlan(
                coach_id=coach_id,
                user_id=data.get('user_id'),
                title=data.get('title'),
                description=data.get('description') ,
                workout_days =data.get('workout_days') ## the number of days to be done in a week , type(int)

            )
            db.session.add(new_workoutplan)
            db.session.commit()
            new_dict=new_workoutplan.to_dict()
            response=make_response(jsonify(new_dict),201)
            return response
        else: 
            response=make_response(jsonify({"msg":"Unauthorized Access"}),401)
            return response
        

    @jwt_required()
    def get(self):  ## for users
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        user_id = current_identity['id']
        if user_type == 'user':
            workout_plans=WorkoutPlan.query.filter_by(user_id=user_id).all()
            work_dict=[workout_plan.to_dict() for workout_plan in workout_plans]
            response=make_response(jsonify(work_dict),200)
            return response
        

    @jwt_required()    
    def patch(self): ## for coaches
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        coach_id = current_identity['id']
        if user_type == 'coach':
            coach=Coach.query.filter_by(id=coach_id).first()
            if coach:
                workout_plan_id=request.get_json()['workout_plan_id']
                workout_plan= WorkoutPlan.query.filter_by(id=workout_plan_id).first()
                if workout_plan:
                    title=request.get_json()['title']
                    description=request.get_json()['description']
                    workout_days=request.get_json()['workout_days']

                    workout_plan.title=title
                    workout_plan.description=description
                    workout_plan.workout_days=workout_days
                    db.session.commit()
                    work_dict=workout_plan.to_dict()
                    response = make_response(jsonify(work_dict),200)
                    return response               
                else:
                    response=make_response(jsonify({'msg':'Workout Plan not found'}),404)
                    return response
                
        else:
            response=make_response(jsonify({"msg":"Unauthorized Access"}),401)
            return response

    @jwt_required()   
    def delete(self):  ## for coaches
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        coach_id = current_identity['id']
        if user_type == 'coach':
            coach=Coach.query.filter_by(id=coach_id).first()
            if coach:
                work_id=request.get_json()['workout_plan_id']
                workout_plan= WorkoutPlan.query.filter_by(id=work_id).first()
                if workout_plan:
                    db.session.delete(workout_plan)
                    db.session.commit()
                    response=make_response(jsonify({'msg':'Workout plan deleted successfully.'}),200)
                    return response
                else:
                    response=make_response(jsonify({'msg':'Workout plan not found'}),404)
                    return response
                
        else: 
            response=make_response(jsonify({"msg":"Unauthorized Access"}),401)
            return response


class UserProfile(Resource):##for user
    @jwt_required()
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
                            
                            
                    

class CoachProfile(Resource): ##for coach
    @jwt_required()
    def get(self):
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        coach_id = current_identity['id']
        if user_type=='coach':
            coach=Coach.query.filter_by(id=coach_id).first()
            if coach:
                coach_dict=coach.to_dict()
                response=make_response(jsonify(coach_dict),200)
                return response
            else:
                response=make_response(jsonify({'msg':'Coach not found'}),404)
                return response
            
        else: 
            response=make_response(jsonify({"msg":"Unauthorized Access"}),401)
            return response
            
    @jwt_required()
    def patch(self):
        current_identity = get_jwt_identity()
        user_type = current_identity['type']
        coach_id = current_identity['id']
        if user_type=='coach':
            coach=Coach.query.filter_by(id=coach_id).first()
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
app_api.add_resource(CoachProfile,'/coachprofile')






if __name__ == '__main__':
    app.run(port=5555, debug=True)





