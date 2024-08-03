from models import * 
from app import app

with app.app_context():
    
    print('Deleting tables')
    ProgressLog.query.delete()
    NutritionLog.query.delete()
    Exercise.query.delete()
    Workout.query.delete()
    WorkoutPlan.query.delete()
    Goal.query.delete()
    Coach.query.delete()
    User.query.delete()
    db.session.commit()
    db.engine.execute("DROP TABLE IF EXISTS progress_logs;")
    db.engine.execute("DROP TABLE IF EXISTS nutrition_logs;")
    db.engine.execute("DROP TABLE IF EXISTS exercises;")
    db.engine.execute("DROP TABLE IF EXISTS workouts;")
    db.engine.execute("DROP TABLE IF EXISTS workout_plans;")
    db.engine.execute("DROP TABLE IF EXISTS goals;")
    db.engine.execute("DROP TABLE IF EXISTS coaches;")
    db.engine.execute("DROP TABLE IF EXISTS users;")






