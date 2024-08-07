from models import *
from config import *
from app import app
from sqlalchemy import text
from datetime import datetime,date
   


#$ used drop tables because query.delete() brings id error
#$ used text because sql alchemy expects the sql-commands as text


with app.app_context():
    print('Deleting tables')    
    db.session.execute(text("DROP TABLE IF EXISTS progress_logs CASCADE;"))
    db.session.execute(text("DROP TABLE IF EXISTS nutrition_logs CASCADE;"))
    db.session.execute(text("DROP TABLE IF EXISTS exercises CASCADE;"))
    db.session.execute(text("DROP TABLE IF EXISTS workouts CASCADE;"))
    db.session.execute(text("DROP TABLE IF EXISTS workout_plans CASCADE;"))
    db.session.execute(text("DROP TABLE IF EXISTS goals CASCADE;"))
    db.session.execute(text("DROP TABLE IF EXISTS coaches CASCADE;"))
    db.session.execute(text("DROP TABLE IF EXISTS users CASCADE;"))
    
    db.session.commit()

    print('Creating Tables')
    db.create_all()