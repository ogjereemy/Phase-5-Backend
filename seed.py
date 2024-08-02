from models import *
from app import app

with app.app_context():
    pass
    # cardio_plan = WorkoutPlan(name="Cardio Plan")
    # db.session.add(cardio_plan)

    # # Create Exercises for the plan
    # exercise1 = Exercise(name="Running", duration=30, type="Cardio", workout_plan=cardio_plan)
    # exercise2 = Exercise(name="Cycling", duration=45, type="Cardio", workout_plan=cardio_plan)
    # db.session.add(exercise1)
    # db.session.add(exercise2)
    # db.session.commit() 