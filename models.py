from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates,relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime,time,date
from werkzeug.security import generate_password_hash, check_password_hash
from enum import Enum as PyEnum
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy import Enum
from config import *

class MealType(PyEnum):
        BREAKFAST= 'breakfast'
        LUNCH= 'lunch'
        DINNER= 'dinner'
        SNACK = 'snack'


class User(db.Model,SerializerMixin):
    __tablename__="users"
    id= db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(50), unique=True, nullable=False)
    email= db.Column(db.String(100),nullable=False)
    _password_hash=db.Column(db.String,nullable =False)
    photo=db.Column(db.String(255), nullable=False )
    coach_id=db.Column(db.Integer,db.ForeignKey('coaches.id'),nullable=False)
    goals=db.relationship('Goal',back_populates='user')
    coach=db.relationship('Coach',back_populates='users')
    nutrition_logs=db.relationship('NutritionLog',back_populates='user')
    workouts=db.relationship('Workout',back_populates='user')
    workout_plans=db.relationship('WorkoutPlan',back_populates='user')
    progress_logs=db.relationship('ProgressLog',back_populates='user')
    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self,password):
        password_hash=bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash=password_hash.decode('utf-8')
    def authenticate(self,password):
        return bcrypt.check_password_hash(
            self._password_hash,password.encode('utf-8')
        )
    
class Coach(db.Model,SerializerMixin):
    __tablename__="coaches"
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email= db.Column(db.String(100),nullable=False)
    _password_hash =db.Column(db.String,nullable =False)
    photo =db.Column(db.String(255), nullable=False )
    bio = db.Column(db.String,nullable=False)
    specialities = db.Column(db.String,nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    users=db.relationship('User',back_populates='coach')
    workout_plans=db.relationship('WorkoutPlan',back_populates='coach')
    workouts=db.relationship('Workout',back_populates='coach')
    @hybrid_property
    def password_hash(self):
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self,password):
        password_hash=bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash=password_hash.decode('utf-8')
    def authenticate(self,password):
        return bcrypt.check_password_hash(
            self._password_hash,password.encode('utf-8')
        )

class WorkoutPlan(db.Model,SerializerMixin):
    __tablename__="workout_plans"
    id=db.Column(db.Integer, primary_key=True)
    coach_id= db.Column(db.Integer ,db.ForeignKey('coaches.id'),nullable=False)
    user_id= db.Column(db.Integer ,db.ForeignKey('users.id'),nullable=False)
    title=db.Column(db.String(50),nullable=False)
    description= db.Column(db.String,nullable=False)
    workout_days=db.Column(db.Integer , nullable=False)
    workouts=db.relationship('Workout',back_populates='workout_plan')
    coach=db.relationship('Coach',back_populates='workout_plans')
    user=db.relationship('User',back_populates='workout_plans')
class Workout(db.Model,SerializerMixin):
    __tablename__="workouts"
    id= db.Column(db.Integer,primary_key=True)
    workout_plan_id =db.Column(db.Integer,db.ForeignKey('workout_plans.id'),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    coach_id=db.Column(db.Integer,db.ForeignKey('coaches.id'),nullable=False)
    title= db.Column(db.String(50),nullable=False)
    day_of_week=db.Column(db.String(20),nullable=False)
    # workout_date=db.Column(db.Date,nullable=False,default=datetime.utcnow().date())
    exercises=db.Column(db.String,nullable=False)
    user=db.relationship('User',back_populates='workouts')
    exercises1=db.relationship('Exercise',back_populates='workout')
    workout_plan=db.relationship('WorkoutPlan',back_populates='workouts')
    coach=db.relationship('Coach',back_populates='workouts')
class Exercise(db.Model,SerializerMixin):
    __tablename__='exercises'
    id=db.Column(db.Integer,primary_key=True)
    workout_id=db.Column(db.Integer,db.ForeignKey('workouts.id'),nullable=False)
    name=db.Column(db.String(50),nullable=False)
    sets=db.Column(db.Integer,nullable=False)
    reps=db.Column(db.Integer,nullable=False)
    weight=db.Column(db.Integer,nullable=False)
    description=db.Column(db.String,nullable=False)
    workout=db.relationship('Workout',back_populates='exercises1')

class ProgressLog(db.Model,SerializerMixin): ##weekly input 
    __tablename__="progress_logs"
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    date=db.Column(db.Date,nullable=False)
    weight=db.Column(db.Integer,nullable=False)
    body_fat_percentage=db.Column(db.Integer,nullable=False)
    muscle_mass=db.Column(db.Integer,nullable=False)
    notes=db.Column(db.String(100),nullable=False)
    user=db.relationship('User',back_populates='progress_logs')



class NutritionLog(db.Model,SerializerMixin): ##update nutrition log for every meal that is taken
    __tablename__='nutrition_logs'
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    date=db.Column(db.Date,nullable=False)
    meal_type=db.Column(Enum(MealType),nullable=False)
    calory_intake=db.Column(db.Integer,nullable=False)
    protein=db.Column(db.Integer,nullable=False)
    fat=db.Column(db.Integer,nullable=False)
    carbs=db.Column(db.Integer,nullable=False)
    notes=db.Column(db.String(100),nullable=False)
    user=db.relationship('User',back_populates='nutrition_logs')

class Goal(db.Model,SerializerMixin):
    __tablename__="goals"
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    title=db.Column(db.String(50),nullable=False)
    description=db.Column(db.String,nullable=False)
    target_date=db.Column(db.Date,nullable=False)
    achieved=db.Column(db.Boolean ,default=False,nullable=False)
    user=db.relationship('User',back_populates='goals')