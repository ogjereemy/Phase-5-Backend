from models import * 
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






