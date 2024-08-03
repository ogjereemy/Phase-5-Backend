from models import *
from config import *
from app import app
from sqlalchemy import text
from datetime import datetime


 # cardio_plan = WorkoutPlan(name="Cardio Plan")
    # db.session.add(cardio_plan)

    # # Create Exercises for the plan
    # exercise1 = Exercise(name="Running", duration=30, type="Cardio", workout_plan=cardio_plan)
    # exercise2 = Exercise(name="Cycling", duration=45, type="Cardio", workout_plan=cardio_plan)
    # db.session.add(exercise1)
    # db.session.add(exercise2)
    # db.session.commit() 


    # cardio=WorkoutPlan()
    # hypertrophe=WorkoutPlan()
    # weight_loss=WorkoutPlan()
    # yoga=WorkoutPlan()
    # stretches=WorkoutPlan()
    # db.session.add(cardio)
    # db.session.add(hypertrophe)
    # db.session.add(weight_loss)
    # db.session.add(yoga)
    # db.session.add(stretches)
    # db.session.commit()


    # steve=Coach(username='steve',email='steve@gmail.com',_password_hash=)



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
    
## coaches

    steve = Coach(
    username="steve",
    email="steve@gmail.com",
    password_hash="steve_123",
    photo="https://images.pexels.com/photos/1092874/pexels-photo-1092874.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    bio="Experienced fitness coach specializing in cardio and strength training.",
    specialities="Cardio, Strength Training",
    is_admin=True)

    jeremy = Coach(
    username="ogola",
    email="ogojeremy@gmail.com",
    password_hash="ogosh",
    photo="https://images.pexels.com/photos/1865131/pexels-photo-1865131.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    bio="Certified personal trainer with 10 years of experience in strength and conditioning.",
    specialities="Strength Training, Conditioning",
    is_admin=True)

    tyra = Coach(
    username="tyra",
    email="tyra@gmail.com",
    password_hash="tyrant",
    photo="https://images.pexels.com/photos/1480520/pexels-photo-1480520.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    bio="Yoga instructor and mindfulness coach with a passion for holistic health and well-being.",
    specialities="Yoga ,Mindfulness",
    is_admin=True)

    ace = Coach(
    username="ace",
    email="simplyace@gmail.com",
    password_hash="samuel",
    photo="https://images.pexels.com/photos/3253501/pexels-photo-3253501.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    bio="Former professional athlete turned fitness coach, focusing on agility and speed training.",
    specialities="Agility, Speed Training",
    is_admin=False)

    mary = Coach(
    username="Mary",
    email="marynjenga@gmail.com",
    password_hash="mary_2885",
    photo="https://images.pexels.com/photos/1638324/pexels-photo-1638324.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    bio="Fitness coach specializing in weight loss and nutritional guidance.",
    specialities="Weight Loss, Nutrition",
    is_admin=False)
    
    derrick = Coach(
    username="ongoma",
    email="derongoma@gmail.com",
    password_hash="odrumzz",
    photo="coach_photo_url",
    bio="Expert in HIIT and functional training, with a background in sports science.",
    specialities="HIIT, Functional Training",
    is_admin=False)
    db.session.add(steve)
    db.session.add(jeremy)
    db.session.add(tyra)
    db.session.add(ace)
    db.session.add(mary)
    db.session.add(derrick)
    db.session.commit()
    print('Coaches added')

    ##users
    jane = User(
    username="jane_doe",
    email="jane_doe@gmail.com",
    password_hash="j@ne123",
    photo="https://images.pexels.com/photos/864939/pexels-photo-864939.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=1  
    )

    mike = User(
    username="michael_smith",
    email="michael_smith@gmail.com",
    password_hash="mike3123",
    photo="https://images.pexels.com/photos/791764/pexels-photo-791764.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=2  
    )

    emily = User(
    username="emily_jones",
    email="emily_jones@gmail.com",
    password_hash="j0n3s_boro",
    photo="https://images.pexels.com/photos/1886487/pexels-photo-1886487.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=3  
    )

    daniel = User(
    username="daniel_wilson",
    email="daniel_wilson@gmail.com",
    password_hash="dannywilis",
    photo="https://images.pexels.com/photos/1552102/pexels-photo-1552102.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=4  
    )

    olivia = User(
    username="olivia_martin",
    email="olivia_martin@gmail.com",
    password_hash="olive_garden",
    photo="https://images.pexels.com/photos/863935/pexels-photo-863935.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=5  
    )

    liam = User(
    username="liam_anderson",
    email="liam_anderson@gmail.com",
    password_hash="YNWA",
    photo="https://images.pexels.com/photos/2149771/pexels-photo-2149771.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=1
    )

    ava = User(
    username="ava_thomas",
    email="ava_thomas@gmail.com",
    password_hash="ava_max",
    photo="https://images.pexels.com/photos/3757941/pexels-photo-3757941.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=2
    )

    noah = User(
    username="noah_taylor",
    email="noah_taylor@gmail.com",
    password_hash="c0ld_#3arted",
    photo="https://images.pexels.com/photos/4720309/pexels-photo-4720309.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=3
    )

    sophia = User(
    username="sophia_white",
    email="sophia_white@gmail.com",
    password_hash="sophia_da_1st",
    photo="https://images.pexels.com/photos/25034152/pexels-photo-25034152/free-photo-of-woman-doing-deadlifts-in-the-gym.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=4
    )

    ben = User(
    username="benjamin_harris",
    email="benjamin_harris@gmail.com",
    password_hash="blue_benji",
    photo="https://images.pexels.com/photos/6389075/pexels-photo-6389075.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=5
    )

    chris = User(
    username="chris_evans",
    email="chris_evans@gmail.com",
    password_hash="CRISTARONALDO_SUI",
    photo="https://images.pexels.com/photos/241456/pexels-photo-241456.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=6  
    )

    nattie = User(
    username="natalie_portman",
    email="natalie_portman@gmail.com",
    password_hash="jamal",
    photo="https://images.pexels.com/photos/1552249/pexels-photo-1552249.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=6  
    )


    db.session.add(jane)
    db.session.add(mike)
    db.session.add(emily)
    db.session.add(daniel)
    db.session.add(olivia)
    db.session.add(liam)
    db.session.add(ava)
    db.session.add(noah)
    db.session.add(sophia)
    db.session.add(ben)
    db.session.add(chris)
    db.session.add(nattie)
    db.session.commit()
    print('Users added successfully.')


    ##goals


    goal1 = Goal(
    user_id=1,  
    title="Increase Cardio Endurance",
    description="Aim to improve your 5K run time by 2 minutes over the next 3 months.",
    target_date=date(2024, 11, 1),
    achieved=False
    )

    goal2 = Goal(
    user_id=1,  
    title="Build Upper Body Strength",
    description="Increase your bench press weight by 20 pounds within the next 6 weeks.",
    target_date=date(2024, 9, 15),
    achieved=False
    )


    goal3 = Goal(
    user_id=2,  
    title="Improve Flexibility",
    description="Achieve a full split by incorporating daily stretching routines for the next 2 months.",
    target_date=date(2024, 10, 30),
    achieved=False
    )

    goal4 = Goal(
    user_id=2,  
    title="Enhance Core Stability",
    description="Hold a plank for 2 minutes by the end of this month.",
    target_date=date(2024, 8, 31),
    achieved=False
    )


    goal5 = Goal(
    user_id=3,  
    title="Reduce Body Fat Percentage",
    description="Decrease body fat by 5% over the next 4 months with a balanced diet and regular exercise.",
    target_date=date(2024, 11, 15),
    achieved=False
    )

    goal6 = Goal(
    user_id=3,  
    title="Increase Running Speed",
    description="Improve your 1-mile run time by 30 seconds within 6 weeks.",
    target_date=date(2024, 9, 30),
    achieved=False
    )


    goal7 = Goal(
    user_id=4,  
    title="Improve Flexibility",
    description="Touch your toes comfortably within 8 weeks by performing daily stretching exercises.",
    target_date=date(2024, 10, 15),
    achieved=False
    )

    goal8 = Goal(
    user_id=4,  
    title="Increase Deadlift Weight",
    description="Add 30 pounds to your current deadlift weight in the next 3 months.",
    target_date=date(2024, 11, 1),
    achieved=False
    )


    goal9 = Goal(
    user_id=5,  
    title="Enhance Agility",
    description="Improve your agility by incorporating ladder drills twice a week for 2 months.",
    target_date=date(2024, 10, 10),
    achieved=False
    )

    goal10 = Goal(
    user_id=5,  
    title="Strengthen Legs",
    description="Increase your squat weight by 25 pounds within 2 months.",
    target_date=date(2024, 10, 31),
    achieved=False
    )


    goal11 = Goal(
    user_id=6,  
    title="Improve Cardio Fitness",
    description="Run 20 miles per week for the next 4 weeks.",
    target_date=date(2024, 8, 31),
    achieved=False
    )

    goal12 = Goal(
    user_id=6,  # Liam Anderson's user_id
    title="Enhance Shoulder Strength",
    description="Increase your shoulder press weight by 15 pounds in 6 weeks.",
    target_date=date(2024, 9, 15),
    achieved=False
    )


    goal13 = Goal(
    user_id=7,  
    title="Boost Running Distance",
    description="Run 10 miles in a single session within the next 8 weeks.",
    target_date=date(2024, 10, 30),
    achieved=False
    )

    goal14 = Goal(
    user_id=7,  
    title="Improve Back Strength",
    description="Increase your deadlift by 40 pounds in 3 months.",
    target_date=date(2024, 11, 15),
    achieved=False
    )


    goal15 = Goal(
    user_id=8,  
    title="Increase Bench Press Weight",
    description="Add 15 pounds to your bench press in 6 weeks.",
    target_date=date(2024, 9, 30),
    achieved=False
    )

    goal16 = Goal(
    user_id=8, 
    title="Enhance Flexibility",
    description="Perform splits on both sides within 2 months.",
    target_date=date(2024, 10, 15),
    achieved=False
)


    goal17 = Goal(
    user_id=9,  
    title="Improve Running Endurance",
    description="Run a half-marathon distance (13.1 miles) in the next 3 months.",
    target_date=date(2024, 11, 15),
    achieved=False
    )

    goal18 = Goal(
    user_id=9,  
    title="Build Core Strength",
    description="Perform 50 sit-ups in a single set by the end of this month.",
    target_date=date(2024, 8, 31),
    achieved=False
    )


    goal19 = Goal(
    user_id=10,  
    title="Increase Cardio Capacity",
    description="Complete a 10K run in under 50 minutes within 2 months.",
    target_date=date(2024, 10, 1),
    achieved=False
    )

    goal20 = Goal(
    user_id=10,  
    title="Strengthen Arm Muscles",
    description="Increase your bicep curl weight by 20 pounds over the next 4 weeks.",
    target_date=date(2024, 9, 10),
    achieved=False
    )


    goal21 = Goal(
    user_id=11, 
    title="Improve Overall Strength",
    description="Achieve personal bests in squat, deadlift, and bench press within 3 months.",
    target_date=date(2024, 11, 1),
    achieved=False
)

    goal22 = Goal(
    user_id=11, 
    title="Enhance Flexibility",
    description="Increase your flexibility with daily stretching to reach toes comfortably within 6 weeks.",
    target_date=date(2024, 9, 15),
    achieved=False
    )


    goal23 = Goal(
    user_id=12,  
    title="Increase Endurance",
    description="Complete a 5K run in under 30 minutes within the next month.",
    target_date=date(2024, 8, 30),
    achieved=False
    )

    goal24 = Goal(
    user_id=12,  
    title="Build Strength",
    description="Increase your maximum pull-ups by 5 in the next 2 months.",
    target_date=date(2024, 10, 15),
    achieved=False
)


    goals = [
    goal1, goal2, goal3, goal4, goal5, goal6, goal7, goal8, goal9, goal10,
    goal11, goal12, goal13, goal14, goal15, goal16, goal17, goal18, goal19, goal20,
    goal21, goal22, goal23, goal24]
    

    for goal in goals:
        db.session.add(goal)
    db.session.commit()
