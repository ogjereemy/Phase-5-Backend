from models import *
from config import *
from app import app
from sqlalchemy import text
from datetime import datetime,date
from dotenv import load_dotenv
load_dotenv()
   


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
    photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQG7NXVYxEEGOB4Ihfzom3uvEXAk2pupS5Phw&s",
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
    coach_id=1,
    coach_name="Steve"  
    )

    mike = User(
    username="michael_smith",
    email="michael_smith@gmail.com",
    password_hash="mike3123",
    photo="https://images.pexels.com/photos/791764/pexels-photo-791764.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=2,
    coach_name="Jeremy"  
    )

    emily = User(
    username="emily_jones",
    email="emily_jones@gmail.com",
    password_hash="j0n3s_boro",
    photo="https://images.pexels.com/photos/1886487/pexels-photo-1886487.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=3,
    coach_name="Tyra"  
    )

    daniel = User(
    username="daniel_wilson",
    email="daniel_wilson@gmail.com",
    password_hash="dannywilis",
    photo="https://images.pexels.com/photos/1552102/pexels-photo-1552102.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=4,
    coach_name="Ace"
    )


    olivia = User(
    username="olivia_martin",
    email="olivia_martin@gmail.com",
    password_hash="olive_garden",
    photo="https://images.pexels.com/photos/863935/pexels-photo-863935.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=5,
    coach_name="Mary"  
    )

    liam = User(
    username="liam_anderson",
    email="liam_anderson@gmail.com",
    password_hash="YNWA",
    photo="https://images.pexels.com/photos/2149771/pexels-photo-2149771.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=1,
    coach_name="Steve"
    )

    ava = User(
    username="ava_thomas",
    email="ava_thomas@gmail.com",
    password_hash="ava_max",
    photo="https://images.pexels.com/photos/3757941/pexels-photo-3757941.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=2,
    coach_name="Jeremy"
    )

    noah = User(
    username="noah_taylor",
    email="noah_taylor@gmail.com",
    password_hash="c0ld_#3arted",
    photo="https://images.pexels.com/photos/4720309/pexels-photo-4720309.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=3,
    coach_name="Tyra"
    )

    sophia = User(
    username="sophia_white",
    email="sophia_white@gmail.com",
    password_hash="sophia_da_1st",
    photo="https://images.pexels.com/photos/25034152/pexels-photo-25034152/free-photo-of-woman-doing-deadlifts-in-the-gym.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=4,
    coach_name="Ace"
    )

    ben = User(
    username="benjamin_harris",
    email="benjamin_harris@gmail.com",
    password_hash="blue_benji",
    photo="https://images.pexels.com/photos/6389075/pexels-photo-6389075.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=5,
    coach_name="Mary"
    )

    chris = User(
    username="chris_evans",
    email="chris_evans@gmail.com",
    password_hash="CRISTARONALDO_SUI",
    photo="https://images.pexels.com/photos/241456/pexels-photo-241456.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=6,
    coach_name="Derrick"  
    )

    nattie = User(
    username="natalie_portman",
    email="natalie_portman@gmail.com",
    password_hash="jamal",
    photo="https://images.pexels.com/photos/1552249/pexels-photo-1552249.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    coach_id=6,
    coach_name="Derrick"  
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
    user_id=6,  
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

    ###nutrition logs

    nutrition_log1 = NutritionLog(
    user_id=1, 
    date=date(2024, 8, 1), 
    meal_type="breakfast", 
    calory_intake=300, 
    protein=10, 
    fat=5, 
    carbs=50, 
    notes="Oatmeal with berries"
)
    nutrition_log2 = NutritionLog(
    user_id=1, 
    date=date(2024, 8, 1), 
    meal_type="lunch", 
    calory_intake=600, 
    protein=35, 
    fat=30, 
    carbs=20, 
    notes="Chicken Caesar Salad"
)
    nutrition_log3 = NutritionLog(
    user_id=1, 
    date=date(2024, 8, 1), 
    meal_type="dinner", 
    calory_intake=700, 
    protein=45, 
    fat=15, 
    carbs=70, 
    notes="Grilled chicken with quinoa"
)
    nutrition_log4 = NutritionLog(
    user_id=1, 
    date=date(2024, 8, 1), 
    meal_type="snack", 
    calory_intake=200, 
    protein=10, 
    fat=4, 
    carbs=30, 
    notes="Greek yogurt with honey"
)

    nutrition_log5 = NutritionLog(
    user_id=2, 
    date=date(2024, 8, 1), 
    meal_type="breakfast", 
    calory_intake=400, 
    protein=15, 
    fat=20, 
    carbs=35, 
    notes="Avocado toast with egg"
)
    nutrition_log6 = NutritionLog(
    user_id=2, 
    date=date(2024, 8, 1), 
    meal_type="lunch", 
    calory_intake=500, 
    protein=30, 
    fat=20, 
    carbs=40, 
    notes="Turkey sandwich with spinach"
)
    nutrition_log7 = NutritionLog(
    user_id=2, 
    date=date(2024, 8, 1), 
    meal_type="dinner", 
    calory_intake=800, 
    protein=40, 
    fat=25, 
    carbs=95, 
    notes="Spaghetti with meatballs"
)
    nutrition_log8 = NutritionLog(
    user_id=2, 
    date=date(2024, 8, 1), 
    meal_type="snack", 
    calory_intake=250, 
    protein=25, 
    fat=5, 
    carbs=20, 
    notes="Protein shake"
)

    nutrition_log9 = NutritionLog(
    user_id=3, 
    date=date(2024, 8, 1), 
    meal_type="breakfast", 
    calory_intake=350, 
    protein=10, 
    fat=10, 
    carbs=50, 
    notes="Smoothie bowl"
)
    nutrition_log10 = NutritionLog(
    user_id=3, 
    date=date(2024, 8, 1), 
    meal_type="lunch", 
    calory_intake=450, 
    protein=15, 
    fat=15, 
    carbs=50, 
    notes="Veggie wrap with hummus"
)
    nutrition_log11 = NutritionLog(
    user_id=3, 
    date=date(2024, 8, 1), 
    meal_type="dinner", 
    calory_intake=750, 
    protein=35, 
    fat=20, 
    carbs=80, 
    notes="Salmon with sweet potato"
)
    nutrition_log12 = NutritionLog(
    user_id=3, 
    date=date(2024, 8, 1), 
    meal_type="snack", 
    calory_intake=200, 
    protein=6, 
    fat=18, 
    carbs=10, 
    notes="Mixed nuts"
)

    nutrition_log13 = NutritionLog(
    user_id=4, 
    date=date(2024, 8, 1), 
    meal_type="breakfast", 
    calory_intake=250, 
    protein=20, 
    fat=5, 
    carbs=10, 
    notes="Egg whites and spinach"
)
    nutrition_log14 = NutritionLog(
    user_id=4, 
    date=date(2024, 8, 1), 
    meal_type="lunch", 
    calory_intake=550, 
    protein=40, 
    fat=25, 
    carbs=30, 
    notes="Grilled chicken salad"
)
    nutrition_log15 = NutritionLog(
    user_id=4, 
    date=date(2024, 8, 1), 
    meal_type="dinner", 
    calory_intake=850, 
    protein=45, 
    fat=30, 
    carbs=90, 
    notes="Beef stir-fry with broccoli"
)
    nutrition_log16 = NutritionLog(
    user_id=4, 
    date=date(2024, 8, 1), 
    meal_type="snack", 
    calory_intake=180, 
    protein=15, 
    fat=5, 
    carbs=25, 
    notes="Cottage cheese with fruit"
)

    nutrition_log17 = NutritionLog(
    user_id=5, 
    date=date(2024, 8, 1), 
    meal_type="breakfast", 
    calory_intake=300, 
    protein=12, 
    fat=8, 
    carbs=40, 
    notes="Yogurt parfait"
)
    nutrition_log18 = NutritionLog(
    user_id=5, 
    date=date(2024, 8, 1), 
    meal_type="lunch", 
    calory_intake=600, 
    protein=25, 
    fat=20, 
    carbs=75, 
    notes="Quinoa and black bean bowl"
)
    nutrition_log19 = NutritionLog(
    user_id=5, 
    date=date(2024, 8, 1), 
    meal_type="dinner", 
    calory_intake=800, 
    protein=35, 
    fat=30, 
    carbs=90, 
    notes="Chicken and vegetable curry"
)
    nutrition_log20 = NutritionLog(
    user_id=5, 
    date=date(2024, 8, 1), 
    meal_type="snack", 
    calory_intake=200, 
    protein=6, 
    fat=10, 
    carbs=25, 
    notes="Apple with peanut butter"
)

    nutrition_log21 = NutritionLog(
    user_id=6, 
    date=date(2024, 8, 1), 
    meal_type="breakfast", 
    calory_intake=400, 
    protein=20, 
    fat=10, 
    carbs=50, 
    notes="Protein pancakes"
)
    nutrition_log22 = NutritionLog(
    user_id=6, 
    date=date(2024, 8, 1), 
    meal_type="lunch", 
    calory_intake=450, 
    protein=35, 
    fat=15, 
    carbs=20, 
    notes="Tuna salad"
)
    nutrition_log23 = NutritionLog(
    user_id=6, 
    date=date(2024, 8, 1), 
    meal_type="dinner", 
    calory_intake=700, 
    protein=40, 
    fat=20, 
    carbs=80, 
    notes="Shrimp and rice"
)
    nutrition_log24 = NutritionLog(
    user_id=6, 
    date=date(2024, 8, 1), 
    meal_type="snack", 
    calory_intake=200, 
    protein=5, 
    fat=12, 
    carbs=25, 
    notes="Banana with almond butter"
)

    nutrition_log25 = NutritionLog(
    user_id=7, 
    date=date(2024, 8, 1), 
    meal_type="breakfast", 
    calory_intake=350, 
    protein=20, 
    fat=5, 
    carbs=50, 
    notes="Smoothie with protein powder"
)
    nutrition_log26 = NutritionLog(
    user_id=7, 
    date=date(2024, 8, 1), 
    meal_type="lunch", 
    calory_intake=500, 
    protein=30, 
    fat=20, 
    carbs=45, 
    notes="Chicken wrap"
)
    nutrition_log27 = NutritionLog(
    user_id=7, 
    date=date(2024, 8, 1), 
    meal_type="dinner", 
    calory_intake=800, 
    protein=35, 
    fat=25, 
    carbs=90, 
    notes="Beef and broccoli stir-fry"
)
    nutrition_log28 = NutritionLog(
    user_id=7, 
    date=date(2024, 8, 1), 
    meal_type="snack", 
    calory_intake=150, 
    protein=10, 
    fat=3, 
    carbs=25, 
    notes="Carrot sticks with hummus"
)

    nutrition_log29 = NutritionLog(
    user_id=8, 
    date=date(2024, 8, 1), 
    meal_type="breakfast", 
    calory_intake=400, 
    protein=18, 
    fat=12, 
    carbs=45, 
    notes="Egg sandwich"
)
    nutrition_log30 = NutritionLog(
    user_id=8, 
    date=date(2024, 8, 1), 
    meal_type="lunch", 
    calory_intake=500, 
    protein=25, 
    fat=15, 
    carbs=55, 
    notes="Grilled chicken with brown rice"
)
    nutrition_log31 = NutritionLog(
    user_id=8, 
    date=date(2024, 8, 1), 
    meal_type="dinner", 
    calory_intake=700, 
    protein=30, 
    fat=20, 
    carbs=85, 
    notes="Pasta with marinara sauce"
)
    nutrition_log32 = NutritionLog(
    user_id=8, 
    date=date(2024, 8, 1), 
    meal_type="snack", 
    calory_intake=180, 
    protein=8, 
    fat=4, 
    carbs=20, 
    notes="Fruit salad"
)

    nutrition_log33 = NutritionLog(
    user_id=9, 
    date=date(2024, 8, 1), 
    meal_type="breakfast", 
    calory_intake=350, 
    protein=15, 
    fat=8, 
    carbs=45, 
    notes="Omelette with veggies"
)
    nutrition_log34 = NutritionLog(
    user_id=9, 
    date=date(2024, 8, 1), 
    meal_type="lunch", 
    calory_intake=600, 
    protein=40, 
    fat=20, 
    carbs=35, 
    notes="Chicken and quinoa bowl"
)
    nutrition_log35 = NutritionLog(
    user_id=9, 
    date=date(2024, 8, 1), 
    meal_type="dinner", 
    calory_intake=800, 
    protein=35, 
    fat=25, 
    carbs=85, 
    notes="Steak with potatoes"
)
    nutrition_log36 = NutritionLog(
    user_id=9, 
    date=date(2024, 8, 1), 
    meal_type="snack", 
    calory_intake=200, 
    protein=10, 
    fat=8, 
    carbs=25, 
    notes="Cheese and crackers"
)

    nutrition_log37 = NutritionLog(
    user_id=10, 
    date=date(2024, 8, 1), 
    meal_type="breakfast", 
    calory_intake=300, 
    protein=15, 
    fat=10, 
    carbs=35, 
    notes="Yogurt with granola"
)
    nutrition_log38 = NutritionLog(
    user_id=10, 
    date=date(2024, 8, 1), 
    meal_type="lunch", 
    calory_intake=500, 
    protein=30, 
    fat=15, 
    carbs=50, 
    notes="Chicken salad sandwich"
)
    nutrition_log39 = NutritionLog(
    user_id=10, 
    date=date(2024, 8, 1), 
    meal_type="dinner", 
    calory_intake=700, 
    protein=40, 
    fat=20, 
    carbs=75, 
    notes="Pork chops with applesauce"
)
    nutrition_log40 = NutritionLog(
    user_id=10, 
    date=date(2024, 8, 1), 
    meal_type="snack", 
    calory_intake=150, 
    protein=8, 
    fat=5, 
    carbs=20, 
    notes="Trail mix"
)

    nutrition_log41 = NutritionLog(
    user_id=11, 
    date=date(2024, 8, 1), 
    meal_type="breakfast", 
    calory_intake=350, 
    protein=12, 
    fat=15, 
    carbs=35, 
    notes="Bagel with cream cheese"
)
    nutrition_log42 = NutritionLog(
    user_id=11, 
    date=date(2024, 8, 1), 
    meal_type="lunch", 
    calory_intake=600, 
    protein=35, 
    fat=20, 
    carbs=55, 
    notes="Turkey and avocado wrap"
)
    nutrition_log43 = NutritionLog(
    user_id=11, 
    date=date(2024, 8, 1), 
    meal_type="dinner", 
    calory_intake=850, 
    protein=40, 
    fat=25, 
    carbs=90, 
    notes="Roast chicken with vegetables"
)
    nutrition_log44 = NutritionLog(
    user_id=11, 
    date=date(2024, 8, 1), 
    meal_type="snack", 
    calory_intake=180, 
    protein=8, 
    fat=8, 
    carbs=20, 
    notes="Mixed fruit"
)

    nutrition_log45 = NutritionLog(
    user_id=12, 
    date=date(2024, 8, 1), 
    meal_type="breakfast", 
    calory_intake=300, 
    protein=10, 
    fat=10, 
    carbs=50, 
    notes="Oatmeal with honey"
)
    nutrition_log46 = NutritionLog(
    user_id=12, 
    date=date(2024, 8, 1), 
    meal_type="lunch", 
    calory_intake=550, 
    protein=25, 
    fat=15, 
    carbs=60, 
    notes="Chicken and rice bowl"
)
    nutrition_log47 = NutritionLog(
    user_id=12, 
    date=date(2024, 8, 1), 
    meal_type="dinner", 
    calory_intake=700, 
    protein=35, 
    fat=20, 
    carbs=75, 
    notes="Fish tacos"
)
    nutrition_log48 = NutritionLog(
    user_id=12, 
    date=date(2024, 8, 1), 
    meal_type="snack", 
    calory_intake=150, 
    protein=5, 
    fat=5, 
    carbs=20, 
    notes="Granola bar"
)


    nutrition_logs = [
    nutrition_log1, nutrition_log2, nutrition_log3, nutrition_log4, nutrition_log5, nutrition_log6, nutrition_log7, nutrition_log8,
    nutrition_log9, nutrition_log10, nutrition_log11, nutrition_log12, nutrition_log13, nutrition_log14, nutrition_log15, nutrition_log16,
    nutrition_log17, nutrition_log18, nutrition_log19, nutrition_log20, nutrition_log21, nutrition_log22, nutrition_log23, nutrition_log24,
    nutrition_log25, nutrition_log26, nutrition_log27, nutrition_log28, nutrition_log29, nutrition_log30, nutrition_log31, nutrition_log32,
    nutrition_log33, nutrition_log34, nutrition_log35, nutrition_log36, nutrition_log37, nutrition_log38, nutrition_log39, nutrition_log40,
    nutrition_log41, nutrition_log42, nutrition_log43, nutrition_log44, nutrition_log45, nutrition_log46, nutrition_log47, nutrition_log48]
    

    for nutrition_log in nutrition_logs:
        db.session.add_all(nutrition_logs)
    db.session.commit()


    


    progress_log1 = ProgressLog(
    user_id=1, 
    date=date(2024, 8, 4),  #$On Sunday August 4, 2024
    weight=180, 
    body_fat_percentage=20, 
    muscle_mass=75, 
    notes="Started new cardio routine"
)
    progress_log2 = ProgressLog(
    user_id=1, 
    date=date(2024, 8, 11),  #$Next week Sunday
    weight=179, 
    body_fat_percentage=19.8, 
    muscle_mass=75.5, 
    notes="Increased running distance"
)
    progress_log3 = ProgressLog(
    user_id=2, 
    date=date(2024, 8, 4),  #$On Sunday August 4, 2024
    weight=165, 
    body_fat_percentage=18, 
    muscle_mass=68, 
    notes="Started weight training"
)
    progress_log4 = ProgressLog(
    user_id=2, 
    date=date(2024, 8, 11),  #$Next week Sunday
    weight=164, 
    body_fat_percentage=17.8, 
    muscle_mass=68.5, 
    notes="Increased protein intake"
)
    progress_log5 = ProgressLog(
    user_id=3, 
    date=date(2024, 8, 4),  #$On Sunday August 4, 2024
    weight=140, 
    body_fat_percentage=22, 
    muscle_mass=55, 
    notes="Started yoga classes"
)
    progress_log6 = ProgressLog(
    user_id=3, 
    date=date(2024, 8, 11),  #$Next Week Sunday
    weight=139, 
    body_fat_percentage=21.8, 
    muscle_mass=55.5, 
    notes="Improved flexibility"
)
    progress_log7 = ProgressLog(
    user_id=4, 
    date=date(2024, 8, 4),  #$On Sunday August 4, 2024
    weight=190, 
    body_fat_percentage=25, 
    muscle_mass=80, 
    notes="Started HIIT workouts"
)
    progress_log8 = ProgressLog(
    user_id=4, 
    date=date(2024, 8, 11),  #$Next Week Sunday
    weight=189, 
    body_fat_percentage=24.8, 
    muscle_mass=80.5, 
    notes="Increased workout intensity"
)
    progress_log9 = ProgressLog(
    user_id=5, 
    date=date(2024, 8, 4), #$On Sunday August 4, 2024
    weight=175, 
    body_fat_percentage=19, 
    muscle_mass=70, 
    notes="Started swimming sessions"
)
    progress_log10 = ProgressLog(
    user_id=5, 
    date=date(2024, 8, 11),  # Next Week Sunday 
    weight=174, 
    body_fat_percentage=18.8, 
    muscle_mass=70.5, 
    notes="Improved swimming technique"
)
    progress_log11 = ProgressLog(
    user_id=6, 
    date=date(2024, 8, 4),  #$On Sunday August 4, 2024
    weight=160, 
    body_fat_percentage=21, 
    muscle_mass=65, 
    notes="Started cycling"
)
    progress_log12 = ProgressLog(
    user_id=6, 
    date=date(2024, 8, 11),  # Next Week Sunday
    weight=159, 
    body_fat_percentage=20.8, 
    muscle_mass=65.5, 
    notes="Increased cycling distance"
)
    progress_log13 = ProgressLog(
    user_id=7, 
    date=date(2024, 8, 4),  #$On Sunday August 4, 2024
    weight=185, 
    body_fat_percentage=22, 
    muscle_mass=78, 
    notes="Started Pilates"
)
    progress_log14 = ProgressLog(
    user_id=7, 
    date=date(2024, 8, 11),  # Next Week Sunday 
    weight=184, 
    body_fat_percentage=21.8, 
    muscle_mass=78.5, 
    notes="Improved core strength"
)
    progress_log15 = ProgressLog(
    user_id=8, 
    date=date(2024, 8, 4),  #$On Sunday August 4, 2024
    weight=200, 
    body_fat_percentage=26, 
    muscle_mass=85, 
    notes="Started strength training"
)
    progress_log16 = ProgressLog(
    user_id=8, 
    date=date(2024, 8, 11),  # Next Week Sunday
    weight=198, 
    body_fat_percentage=25.8, 
    muscle_mass=85.5, 
    notes="Increased weights"
)
    progress_log17 = ProgressLog(
    user_id=9, 
    date=date(2024, 8, 4),  #$On Sunday August 4, 2024
    weight=155, 
    body_fat_percentage=20, 
    muscle_mass=72, 
    notes="Started running program"
)
    progress_log18 = ProgressLog(
    user_id=9, 
    date=date(2024, 8, 11),  # Next Week Sunday 
    weight=154, 
    body_fat_percentage=19.8, 
    muscle_mass=72.5, 
    notes="Increased running speed"
)
    progress_log19 = ProgressLog(
    user_id=10, 
    date=date(2024, 8, 4),  #$On Sunday August 4, 2024
    weight=170, 
    body_fat_percentage=18, 
    muscle_mass=68, 
    notes="Started boxing training"
)
    progress_log20 = ProgressLog(
    user_id=10, 
    date=date(2024, 8, 11),  # Next Week Sunday
    weight=168, 
    body_fat_percentage=17.8, 
    muscle_mass=68.5, 
    notes="Improved boxing technique"
)
    progress_log21 = ProgressLog(
    user_id=11, 
    date=date(2024, 8, 4),  #$On Sunday August 4, 2024
    weight=180, 
    body_fat_percentage=23, 
    muscle_mass=76, 
    notes="Started mixed martial arts"
)
    progress_log22 = ProgressLog(
    user_id=11, 
    date=date(2024, 8, 11),  # Next  Week Sunday 
    weight=179, 
    body_fat_percentage=22.8, 
    muscle_mass=76.5, 
    notes="Increased endurance"
)
    progress_log23 = ProgressLog(
    user_id=12, 
    date=date(2024, 8, 4),  #$On Sunday August 4, 2024
    weight=145, 
    body_fat_percentage=21, 
    muscle_mass=60, 
    notes="Started resistance training"
)
    progress_log24 = ProgressLog(
    user_id=12, 
    date=date(2024, 8, 11),  # Next Week Sunday 
    weight=144, 
    body_fat_percentage=20.8, 
    muscle_mass=60.5, 
    notes="Improved training regimen"
)

    progress_logs = [
    progress_log1, progress_log2, progress_log3, progress_log4, progress_log5, 
    progress_log6, progress_log7, progress_log8, progress_log9, progress_log10,
    progress_log11, progress_log12, progress_log13, progress_log14, progress_log15,
    progress_log16, progress_log17, progress_log18, progress_log19, progress_log20,
    progress_log21, progress_log22, progress_log23, progress_log24]



    for progress_log in progress_logs:
        db.session.add(progress_log)
    db.session.commit()

    ## Workout_Plans

    cardio=WorkoutPlan(
        coach_id = 1,
        user_id = 1,
        title = "Advanced Cardio Plan",
        description = "An advanced cardio plan for experienced individuals aiming for peak endurance.",
        workout_days = 5
    )
    hypertrophe=WorkoutPlan(
        coach_id = 1,
        user_id = 7,
        title = "Beginner Hypertrophy Plan",
        description = "A beginner hypertrophy plan designed to build muscle mass with basic exercises.",
        workout_days = 3
    )
    weight_loss=WorkoutPlan(
        coach_id = 5,
        user_id = 5,
        title = "Basic Weight Loss Plan",
        description = "A basic weight loss plan focused on cardio and full-body workouts to help shed excess fat.",
        workout_days = 3
    )
    yoga=WorkoutPlan(
        coach_id = 3,
        user_id = 3,
        title = "Beginner Yoga Plan",
        description = "A gentle introduction to yoga focusing on basic poses and breathing techniques.",
        workout_days = 3
    )
    yoga1=WorkoutPlan(
        coach_id = 3,
        user_id = 12,
        title = "Advanced Yoga Plan",
        description = "An advanced yoga plan designed to improve flexibility, strength, and mindfulness through challenging poses.",
        workout_days = 5)  
    stretches=WorkoutPlan(
        coach_id = 3,
        user_id = 8,
        title = "Basic Stretching Routine",
        description = "A daily stretching routine aimed at improving overall flexibility and preventing injuries.",
        workout_days = 7
    )    
    cardio1=WorkoutPlan(
        coach_id = 4,
        user_id = 6,
        title = "Intermediate Cardio Plan",
        description = "An intermediate plan to enhance cardiovascular strength with varied workouts.",
        workout_days = 4
    
    )
    cardio2=WorkoutPlan(
        coach_id = 6,
        user_id = 5,
        title = "Beginner Cardio Plan",
        description = "A beginner-friendly cardio plan focusing on building endurance over 4 weeks.",
        workout_days = 3    
    )
    hypertrophe1=WorkoutPlan(
        coach_id = 2,
        user_id = 2,
        title = "Advanced Hypertrophy Plan",
        description = "An advanced hypertrophy plan with a focus on progressive overload and advanced training techniques.",
        workout_days = 3
    )
    weight_loss1=WorkoutPlan(
        coach_id = 5,
        user_id = 10,
        title = "Intermediate Weight Loss Plan",
        description = "An intermediate weight loss plan with a mix of strength training and high-intensity interval training (HIIT).",
        workout_days = 3
    )
    weight_loss2=WorkoutPlan(
        coach_id = 5,
        user_id = 9,
        title = "Advanced Weight Loss Plan",
        description = "An advanced weight loss plan focusing on full-body strength training and high-intensity interval training (HIIT). ",
        workout_days = 3
    )
    stretches1=WorkoutPlan(
        coach_id = 3,
        user_id = 11,
        title = "Athletic Stretching Routine",
        description = "A stretching routine designed for athletes to enhance performance and recovery.",
        workout_days = 4
    )
    db.session.add(cardio)
    db.session.add(hypertrophe)
    db.session.add(weight_loss)
    db.session.add(yoga)
    db.session.add(stretches)
    db.session.add(cardio1)
    db.session.add(cardio2)
    db.session.add(hypertrophe1)
    db.session.add(weight_loss1)
    db.session.add(weight_loss2)
    db.session.add(stretches1)
    db.session.add(yoga1)
    
    db.session.commit()
    

    ###workouts


    ## cardio workouts
    
    
    hiit_circuit_1 = Workout(
    workout_plan_id=6,
    user_id=6,  
    coach_id=4, 
    title="HIIT Circuit 1",
    day_of_week="Monday,Wednesday,Friday,Saturday",
    exercises="Burpees (1 minute), Jumping Jacks (1 minute), Mountain Climbers (1 minute), Rest (1 minute), Repeat (4 sets)"
)

    hiit_circuit_2 = Workout(
    workout_plan_id=6,
    user_id=6,  
    coach_id=4, 
    title="HIIT Circuit 2",
    day_of_week="Monday,Wednesday,Friday,Saturday",
    exercises="Jump Squats (1 minute), High Knees (1 minute), Lunges (1 minute), Rest (1 minute), Repeat (4 sets)"
)

    steady_state_cardio = Workout(
    workout_plan_id=7,
    user_id=5,  
    coach_id=6, 
    title="Steady-State Cardio",
    day_of_week="Tuesday,Thursday,Saturday",
    exercises="Running or Jogging (30-45 minutes), Cycling (30-45 minutes), Rowing (30 minutes), Elliptical Machine (30-45 minutes)"
)

    tabata_training = Workout(
    workout_plan_id=6,
    user_id=6,  
    coach_id=4, 
    title="Tabata Training",
    day_of_week="Monday,Tuesday,Wednesday,Thursday",
    exercises="Sprints (20 seconds), Rest (10 seconds), Repeat (8 sets), Jumping Squats (20 seconds), Rest (10 seconds), Repeat (8 sets)"
)

    cardio_circuits = Workout(
    workout_plan_id=1,
    user_id=1,  
    coach_id=1, 
    title="Cardio Circuits",
    day_of_week="Monday,Tuesday,Wednesday,Thursday,Friday",
    exercises="Jumping Rope (1 minute), High Knees (1 minute), Jumping Jacks (1 minute), Rest (1 minute), Repeat Circuit 1, Running in Place (1 minute), Butt Kicks (1 minute), Mountain Climbers (1 minute), Rest (1 minute), Repeat Circuit 2"
)

    jump_rope = Workout(
    workout_plan_id=1,
    user_id=1, 
    coach_id=1, 
    title="Jump Rope",
    day_of_week="Monday,Tuesday,Wednesday,Thursday,Friday",
    exercises="Basic Jump Rope (10 minutes), Interval Jump Rope (20 minutes), Alternate Foot Jumping (1 minute), Double Unders (1 minute), Side-to-Side Jumps (1 minute)"
)

    hiking = Workout(
    workout_plan_id=1,
    user_id=1, 
    coach_id=1, 
    title="Hiking",
    day_of_week="Monday,Tuesday,Wednesday,Thursday,Friday",
    exercises="Hill Hike (45-60 minutes), Trail Hike (1-2 hours), Uphill Hiking (30 minutes), Downhill Hiking (30 minutes), Steep Inclines (30 minutes), Trail Exploration (1-2 hours)"
)

    stair_climbing = Workout(
    workout_plan_id=7,
    user_id=5,  
    coach_id=6, 
    title="Stair Climbing",
    day_of_week="Tuesday,Thursday,Saturday",
    exercises="Stair Climb (20-30 minutes), Stair Intervals (20 minutes), Basic Stair Climbing (10 minutes), Step-Ups (10 minutes), High Knees on Stairs (10 minutes), Fast Steps (10 minutes)"
)

    bodyweight_cardio = Workout(
    workout_plan_id=6,
    user_id=6, 
    coach_id=4, 
    title="Bodyweight Cardio",
    day_of_week="Monday,Wednesday,Friday,Saturday",
    exercises="Burpees (1 minute), High Knees (1 minute), Jumping Jacks (1 minute), Mountain Climbers (1 minute), Rest (1 minute), Repeat Circuit, Jump Squats (30 seconds), Skaters (30 seconds), Jump Lunges (30 seconds), Rest (30 seconds), Repeat Intervals"
)

    elliptical_trainer = Workout(
    workout_plan_id=7,
    user_id=5, 
    coach_id=6, 
    title="Elliptical Trainer",
    day_of_week="Monday,Thursday,Saturday",
    exercises="Steady-State Elliptical (30-45 minutes), Elliptical Intervals (20 minutes), Forward Elliptical Stride (10 minutes), Backward Elliptical Stride (10 minutes), High-Resistance Intervals (10 minutes), Low-Resistance Endurance (10 minutes), Incline Adjustments (10 minutes)"
)

    recumbent_bike = Workout(
    workout_plan_id=6,
    user_id=6,  
    coach_id=4,
    title="Recumbent Bike",
    day_of_week="Tuesday,Friday,Thursday,Monday",
    exercises="Steady-State Recumbent Bike (30-45 minutes), Recumbent Bike Intervals (20 minutes), Steady Cycling (10 minutes), High-Resistance Intervals (10 minutes), Low-Resistance Endurance (10 minutes), Hill Climb Simulation (20-30 minutes)"
)

    forest_biking = Workout(
    workout_plan_id=7,
    user_id=5,  
    coach_id=6, 
    title="Forest Biking",
    day_of_week="Wednesday,Saturday,Sunday",
    exercises="Trail Ride (45-60 minutes), Interval Trail Riding (30-45 minutes), Technical Trail Ride (30-45 minutes), Trail Cycling (30 minutes), Interval Trail Riding (30 minutes), Technical Trail Navigation (30 minutes), Hill Climbing on Trails (30 minutes)"
)



    ##hypertrophe workouts

    chest_and_triceps = Workout(
    workout_plan_id=2,
    user_id=7,
    coach_id=1,
    title="Chest and Triceps",
    day_of_week="Monday,Tuesday,Saturday",
    exercises="Bench Press, Incline Dumbbell Press, Chest Flyes, Tricep Dips, Tricep Pushdowns"
)

    back_and_biceps = Workout(
    workout_plan_id=2,
    user_id=7,
    coach_id=1,
    title="Back and Biceps",
    day_of_week="Sunday,Thursday,Friday",
    exercises="Deadlift, Bent-Over Rows, Pull-Ups, Barbell Curls, Hammer Curls"
)

    legs_workout = Workout(
    workout_plan_id=2,
    user_id=7,
    coach_id=1,
    title="Legs",
    day_of_week="Monday,Thursday,Friday",
    exercises="Squats, Leg Press, Lunges, Leg Curls, Calf Raises"
)

    shoulders_and_abs = Workout(
    workout_plan_id=2,
    user_id=7,
    coach_id=1,
    title="Shoulders and Abs",
    day_of_week="Wednesday,Thursday,Saturday",
    exercises="Overhead Press, Lateral Raises, Front Raises, Russian Twists, Plank"
)

    

    chest_and_back = Workout(
    workout_plan_id=8,
    user_id=2,
    coach_id=2,
    title="Chest and Back",
    day_of_week="Monday,Wednesday,Friday",
    exercises="Dumbbell Pullover, Chest Press Machine, Single-Arm Dumbbell Row, T-Bar Row, Decline Push-Ups"
)

    legs_and_shoulders = Workout(
    workout_plan_id=8,
    user_id=2,
    coach_id=2,
    title="Legs and Shoulders",
    day_of_week="Tuesday,Thursday,Saturday",
    exercises="Bulgarian Split Squats, Leg Extensions, Seated Calf Raises, Arnold Press, Shrugs"
)

    full_body = Workout(
    workout_plan_id=8,
    user_id=2,
    coach_id=2,
    title="Full Body",
    day_of_week="Sunday,Thursday,Monday",
    exercises="Clean and Press, Goblet Squats, Kettlebell Swings, Renegade Rows, Medicine Ball Slams"
)



    ## yoga  workouts
    beginner = Workout(
    workout_plan_id=4,
    user_id=3,
    coach_id=3,
    title="Beginner's Flow",
    day_of_week="Monday , Wednesday ,Friday",
    exercises="Cat-Cow Pose, Downward-Facing Dog, Child's Pose, Cobra Pose, Warrior I Pose"
)

    intermediate = Workout(
    workout_plan_id=4,
    user_id=3,
    coach_id=3,
    title="Intermediate Flow",
    day_of_week="Wednesday ,Friday, Monday",
    exercises="Sun Salutation A, Warrior II Pose, Triangle Pose, Extended Side Angle Pose, Boat Pose"
)

    advanced = Workout(
    workout_plan_id=12,
    user_id=12,
    coach_id=3,
    title="Advanced Flow",
    day_of_week="Monday,Tuesday ,Wednesday,Thursday,Friday",
    exercises="Crow Pose, Headstand, Forearm Stand, King Pigeon Pose, Wheel Pose"
)

    flexibility = Workout(
    workout_plan_id=4,
    user_id=3,
    coach_id=3,
    title="Flexibility and Balance Flow",
    day_of_week="Tuesday,Thursday,Saturday",
    exercises="Half Moon Pose, Tree Pose, Dancer's Pose, Standing Forward Bend, Pigeon Pose"
)

    core = Workout(
    workout_plan_id=12,
    user_id=12,
    coach_id=3,
    title="Core Strength Flow",
    day_of_week="Monday,Tuesday,Wednesday,Thursday,Friday",
    exercises="Plank Pose, Side Plank Pose, Boat Pose, Crow Pose, Dolphin Plank Pose"
)

    recovery = Workout(
    workout_plan_id=4,
    user_id=3,
    coach_id=3,
    title="Relaxation and Recovery Flow",
    day_of_week="Saturday ,Wednesday ,Friday",
    exercises="Legs-Up-the-Wall Pose, Reclining Bound Angle Pose, Supine Twist, Corpse Pose, Happy Baby Pose"
)
 
##stretches    

    daily_routine_stretch = Workout(
    workout_plan_id=5,
    user_id=8,
    coach_id=3,
    title="Daily Routine Stretch",
    day_of_week="Sunday,Monday,Tuesday,Wednesday,Thursday,Friday,Saturday",
    exercises="Forward Tilt, Backward Tilt, Side Tilt, Side Rotation, Neck Extension, Chin Tucks, Standing Bicep Stretch, Wall Bicep Stretch, Doorway Bicep Stretch, Seated Bicep Stretch, Overhead Bicep Stretch, Cat-Cow Stretch, Cobra Stretch, Child's Pose, Seated Forward Bend, Standing Side Stretch, Cross-Body Shoulder Stretch, Overhead Tricep Stretch, Shoulder Blade Squeeze, Thread the Needle, Doorway Stretch, Knee-to-Chest Stretch, Quadriceps Stretch, Hamstring Stretch, Standing Hamstring Stretch, Butterfly Stretch, Side Lunge Stretch, Seated Glute Stretch, Lying Glute Stretch, Standing Figure-Four Stretch, Standing Calf Stretch, Seated Calf Stretch, Dynamic Hamstring Stretch, Hamstring Stretch on a Chair, Hamstring Stretch with Foam Roller"
)

    athletic_routine_stretch = Workout(
    workout_plan_id=11,
    user_id=11,
    coach_id=3,
    title="Athletic Routine Stretch",
    day_of_week="Monday,Wednesday,Friday,Sunday",
    exercises="Levator Scapulae Stretch, Upper Trapezius Stretch, Scalene Stretch, Isometric Neck Exercises (Front of Neck, Back of Neck, Sides of Neck), Cross-Body Arm Stretch, Towel Bicep Stretch, Spinal Twist, Bridge Pose, Pigeon Pose, Kneeling Side Stretch, Extended Triangle Pose, Eagle Arms (Garudasana), Child's Pose with Shoulder Stretch, Cow-Face Pose (Gomukhasana) Arms, Shoulder Circles, Lat Stretch at a Wall, Cobra Stretch (II), Seated Forward Hinge, Sphinx Pose, Spinal Twist (II), Lying Quad Stretch, Hip Flexor Stretch, Pigeon Pose (II), Seated Thigh Stretch, Supine Glute Stretch, Seated Glute Stretch (II), Pigeon Pose (III), Downward Dog Stretch, Calf Stretch on a Step, Wall Calf Stretch with Bent Knee, Standing Forward Bend with Bent Knee"
)

## weight loss
    full_body_hiit = Workout(
    workout_plan_id=3,
    user_id=5,
    coach_id=5,
    title="Full Body HIIT",
    day_of_week="Wednesday,Thursday,Sunday",
    exercises="Jumping Jacks: 30-45 seconds, 3 sets; Burpees: 15-20 reps, 3 sets; Mountain Climbers: 30-45 seconds, 3 sets; High Knees: 30-45 seconds, 3 sets; Plank: 30-60 seconds, 3 sets"
)

    lower_body_burn = Workout(
    workout_plan_id=3,
    user_id=5,
    coach_id=5,
    title="Lower Body Burn",
    day_of_week="Tuesday,Thursday,Saturday",
    exercises="Squats: 15-20 reps, 3 sets; Lunges: 12-15 reps each leg, 3 sets; Glute Bridges: 15-20 reps, 3 sets; Step-Ups: 12-15 reps each leg, 3 sets; Calf Raises: 20-25 reps, 3 sets"
)

    upper_body_blast = Workout(
    workout_plan_id=3,
    user_id=5,
    coach_id=5,
    title="Upper Body Blast",
    day_of_week="Monday,Wednesday,Friday",
    exercises="Push-Ups: 10-15 reps, 3 sets; Dumbbell Rows: 12-15 reps, 3 sets; Shoulder Press: 10-12 reps, 3 sets; Bicep Curls: 12-15 reps, 3 sets; Tricep Dips: 10-15 reps, 3 sets"
)

    core_conditioning = Workout(
    workout_plan_id=3,
    user_id=5,
    coach_id=5,
    title="Core Conditioning",
    day_of_week="Wednesday,Thursday,Saturday",
    exercises="Bicycle Crunches: 20-30 reps, 3 sets; Russian Twists: 20-30 reps, 3 sets; Plank with Shoulder Taps: 20-30 taps, 3 sets; Leg Raises: 15-20 reps, 3 sets; Side Plank: 30-45 seconds each side, 3 sets"
)


    cardio_circuit = Workout(
    workout_plan_id=9,
    user_id=10,
    coach_id=5,
    title="Cardio Circuit",
    day_of_week="Monday,Wednesday,Friday",  
    exercises="Jump Rope: 1-2 minutes, 3 sets; Box Jumps: 10-15 reps, 3 sets; Skaters: 30-45 seconds, 3 sets; Battle Ropes: 30-45 seconds, 3 sets; Treadmill Sprints: 30 seconds on, 30 seconds off, 5-10 sets"
)

    upper_body_circuit = Workout(
    workout_plan_id=9,
    user_id=10,
    coach_id=5,
    title="Upper Body Circuit",
    day_of_week="Tuesday,Thursday,Saturday",  
    exercises="Dumbbell Chest Press: 12-15 reps, 3 sets; Dumbbell Flyes: 12-15 reps, 3 sets; Lat Pulldowns: 12-15 reps, 3 sets; Dumbbell Shoulder Raises: 12-15 reps, 3 sets; Tricep Kickbacks: 12-15 reps, 3 sets"
)

    lower_body_circuit = Workout(
    workout_plan_id=9,
    user_id=10,
    coach_id=5,
    title="Lower Body Circuit",
    day_of_week="Sunday,Tuesday,Saturday", 
    exercises="Goblet Squats: 15-20 reps, 3 sets; Bulgarian Split Squats: 12-15 reps each leg, 3 sets; Deadlifts: 12-15 reps, 3 sets; Lateral Lunges: 12-15 reps each leg, 3 sets; Hamstring Curls: 15-20 reps, 3 sets"
)

    

    core_circuit = Workout(
    workout_plan_id=10,
    user_id=9,
    coach_id=5,
    title="Core Circuit",
    day_of_week="Monday,Wednesday,Friday", 
    exercises="V-Ups: 15-20 reps, 3 sets; Hanging Leg Raises: 10-15 reps, 3 sets; Side Plank Hip Lifts: 15-20 reps each side, 3 sets; Reverse Crunches: 15-20 reps, 3 sets; Ab Wheel Rollouts: 10-15 reps, 3 sets"
)

    hiit_challenge = Workout(
    workout_plan_id=10,
    user_id=9,
    coach_id=5,
    title="HIIT Challenge",
    day_of_week="Tuesday,Thursday,Saturday",  
    exercises="Burpees: 20-25 reps, 3 sets; Jump Squats: 15-20 reps, 3 sets; Mountain Climbers: 30-45 seconds, 3 sets; High Knees: 30-45 seconds, 3 sets; Plank Jacks: 30-45 seconds, 3 sets"
)

    workouts = [
    hiit_circuit_1,
    hiit_circuit_2,
    steady_state_cardio,
    tabata_training,
    cardio_circuits,
    jump_rope,
    hiking,
    stair_climbing,
    bodyweight_cardio,
    elliptical_trainer,
    recumbent_bike,
    forest_biking,
    chest_and_triceps,
    back_and_biceps,
    legs_workout,
    shoulders_and_abs,
    chest_and_back,
    legs_and_shoulders,
    full_body,
    beginner,
    intermediate,
    advanced,
    flexibility,
    core,
    recovery,
    daily_routine_stretch,
    athletic_routine_stretch,
    full_body_hiit,
    lower_body_burn,
    upper_body_blast,
    core_conditioning,
    cardio_circuit,
    upper_body_circuit,
    lower_body_circuit,
    core_circuit,
    hiit_challenge]
    for workout in workouts:
        db.session.add(workout)
        db.session.commit()

###exercises
   
    #**Hypertrophe**#

# Chest and Triceps
    bench_press = Exercise(
    workout_id=13,
    name='Bench Press',
    sets=3,
    reps='8-12',
    weight='Moderate to heavy',
    description='Lie on a flat bench with your feet flat on the floor. Grip the barbell slightly wider than shoulder-width apart. Lower the barbell to your chest, then press it back up to the starting position.'
)

    incline_dumbbell_press = Exercise(
    workout_id=13,
    name='Incline Dumbbell Press',
    sets=3,
    reps='8-12',
    weight='Moderate',
    description='Set an incline bench at 30-45 degrees. Hold a dumbbell in each hand, press the weights overhead until your arms are fully extended. Lower the weights to the sides of your chest.'
)

    chest_flyes = Exercise(
    workout_id=13,
    name='Chest Flyes',
    sets=3,
    reps='10-15',
    weight='Light to moderate',
    description='Lie on a flat bench with a dumbbell in each hand. Extend your arms above your chest with a slight bend in your elbows. Lower the weights out to the sides, then bring them back together above your chest.'
)

    tricep_dips = Exercise(
    workout_id=13,
    name='Tricep Dips',
    sets=3,
    reps='8-12',
    weight='Bodyweight or added weight',
    description='Position your hands shoulder-width apart on a bench or parallel bars. Lower your body until your upper arms are parallel to the floor, then push back up to the starting position.'
)

    tricep_pushdowns = Exercise(
    workout_id=13,
    name='Tricep Pushdowns',
    sets=3,
    reps='10-15',
    weight='Moderate',
    description='Attach a rope or bar to a high pulley. Stand with your feet shoulder-width apart and grasp the attachment with both hands. Push the attachment down until your arms are fully extended, then return to the starting position.'
)

# Back and Biceps
    deadlift = Exercise(
    workout_id=14,
    name='Deadlift',
    sets=3,
    reps='6-8',
    weight='Heavy',
    description='Stand with your feet hip-width apart, grip the barbell with your hands just outside your knees. Keeping your back flat, lift the bar by extending your hips and knees to full extension.'
)

    bent_over_rows = Exercise(
    workout_id=14,
    name='Bent-Over Rows',
    sets=3,
    reps='8-12',
    weight='Moderate',
    description='Hold a barbell with a pronated grip, bend at the waist with a slight bend in the knees. Pull the barbell to your lower ribcage, then lower it back to the starting position.'
)

    pull_ups = Exercise(
    workout_id=14,
    name='Pull-Ups',
    sets=3,
    reps='8-12',
    weight='Bodyweight or added weight',
    description='Grip a pull-up bar with an overhand grip, hands shoulder-width apart. Pull yourself up until your chin is above the bar, then lower yourself back down.'
)

    barbell_curls = Exercise(
    workout_id=14,
    name='Barbell Curls',
    sets=3,
    reps='10-15',
    weight='Light to moderate',
    description='Stand with your feet shoulder-width apart, hold a barbell with an underhand grip. Curl the barbell up to shoulder height, then lower it back to the starting position.'
)

    hammer_curls = Exercise(
    workout_id=14,
    name='Hammer Curls',
    sets=3,
    reps='10-15',
    weight='Light to moderate',
    description='Stand with a dumbbell in each hand, arms at your sides with palms facing your torso. Curl the weights while keeping your palms facing each other.'
)

# Legs
    squats = Exercise(
    workout_id=15,
    name='Squats',
    sets=3,
    reps='8-12',
    weight='Moderate to heavy',
    description='Stand with your feet shoulder-width apart, barbell across your upper back. Lower your body by bending your hips and knees until your thighs are parallel to the floor, then stand back up.'
)

    leg_press = Exercise(
    workout_id=15,
    name='Leg Press',
    sets=3,
    reps='10-15',
    weight='Moderate',
    description='Sit on a leg press machine with your feet shoulder-width apart on the platform. Lower the platform by bending your knees, then press it back up to the starting position.'
)

    lunges = Exercise(
    workout_id=15,
    name='Lunges',
    sets=3,
    reps='10-12 each leg',
    weight='Light to moderate',
    description='Stand with your feet together, holding a dumbbell in each hand. Step forward with one leg and lower your body until your front thigh is parallel to the floor, then push back to the starting position.'
)

    leg_curls = Exercise(
    workout_id=15,
    name='Leg Curls',
    sets=3,
    reps='10-15',
    weight='Light to moderate',
    description='Lie face down on a leg curl machine, place your legs under the padded lever. Curl your legs up as far as possible, then slowly lower them back to the starting position.'
)

    calf_raises = Exercise(
    workout_id=15,
    name='Calf Raises',
    sets=3,
    reps='12-20',
    weight='Bodyweight or added weight',
    description='Stand on the edge of a step or platform with your heels hanging off. Raise your heels as high as possible, then lower them back down.'
)

# Shoulders and Abs
    overhead_press = Exercise(
    workout_id=16,
    name='Overhead Press',
    sets=3,
    reps='8-12',
    weight='Moderate',
    description='Stand with your feet shoulder-width apart, hold a barbell at shoulder height. Press the barbell overhead until your arms are fully extended, then lower it back to the starting position.'
)

    lateral_raises = Exercise(
    workout_id=16,
    name='Lateral Raises',
    sets=3,
    reps='10-15',
    weight='Light to moderate',
    description='Stand with a dumbbell in each hand, arms at your sides. Raise the weights out to the sides until your arms are parallel to the floor, then lower them back down.'
)

    front_raises = Exercise(
    workout_id=16,
    name='Front Raises',
    sets=3,
    reps='10-15',
    weight='Light to moderate',
    description='Stand with a dumbbell in each hand, arms at your sides. Raise the weights in front of you until your arms are parallel to the floor, then lower them back down.'
)

    russian_twists = Exercise(
    workout_id=16,
    name='Russian Twists',
    sets=3,
    reps='15-20 each side',
    weight='Light to moderate',
    description='Sit on the floor with your knees bent, hold a weight or medicine ball with both hands. Lean back slightly and twist your torso to move the weight from side to side.'
)

    plank = Exercise(
    workout_id=16,
    name='Plank',
    sets=3,
    reps='Hold for 30-60 seconds',
    weight='Bodyweight',
    description='Position yourself on your forearms and toes, keeping your body in a straight line from head to heels. Hold this position without letting your hips sag.'
)

# Chest and Back
    dumbbell_pullover = Exercise(
    workout_id=17,
    name='Dumbbell Pullover',
    sets=3,
    reps='8-12',
    weight='Moderate',
    description='Lie on a flat bench with a dumbbell held with both hands above your chest. Lower the dumbbell back over your head until you feel a stretch in your chest, then pull it back to the starting position.'
)

    chest_press_machine = Exercise(
    workout_id=17,
    name='Chest Press Machine',
    sets=3,
    reps='10-15',
    weight='Moderate',
    description='Sit on a chest press machine and grasp the handles. Press the handles forward until your arms are fully extended, then slowly return to the starting position.'
)

    single_arm_dumbbell_row = Exercise(
    workout_id=17,
    name='Single-Arm Dumbbell Row',
    sets=3,
    reps='8-12 each arm',
    weight='Moderate',
    description='Place one knee and hand on a bench for support, hold a dumbbell in the other hand. Pull the dumbbell towards your hip, keeping your back flat, then lower it back down.'
)

    t_bar_row = Exercise(
    workout_id=17,
    name='T-Bar Row',
    sets=3,
    reps='8-12',
    weight='Moderate',
    description='Stand over a T-bar row machine with your feet shoulder-width apart. Grip the handles and row the bar towards your torso, then lower it back down.'
)

    decline_push_ups = Exercise(
    workout_id=17,
    name='Decline Push-Ups',
    sets=3,
    reps='10-15',
    weight='Bodyweight',
    description='Place your feet on an elevated surface with your hands on the floor. Lower your body until your chest nearly touches the ground, then push back up.'
)

    # Legs and Shoulders
    bulgarian_split_squats = Exercise(
    workout_id=18, 
    name='Bulgarian Split Squats',
    sets=3,
    reps='10-12 each leg',
    weight='Moderate',
    description='Stand a few feet in front of a bench with one foot elevated behind you on the bench. Lower your body until your front thigh is parallel to the ground, then press back up to the starting position.'
)

    leg_extensions = Exercise(
    workout_id=18,
    name='Leg Extensions',
    sets=3,
    reps='12-15',
    weight='Moderate',
    description='Sit on a leg extension machine with your legs under the padded lever. Extend your legs until they are straight, then lower them back to the starting position.'
)

    seated_calf_raises = Exercise(
    workout_id=18,
    name='Seated Calf Raises',
    sets=3,
    reps='12-15',
    weight='Moderate',
    description='Sit on a calf raise machine with your feet on the platform and the pads resting on your knees. Raise your heels as high as possible, then lower them back down.'
)

    arnold_press = Exercise(
    workout_id=18,
    name='Arnold Press',
    sets=3,
    reps='8-12',
    weight='Moderate',
    description='Sit on a bench with back support, hold a dumbbell in each hand with palms facing you. Press the weights overhead while rotating your palms to face forward, then lower back to the starting position.'
)

    shrugs = Exercise(
    workout_id=18,
    name='Shrugs',
    sets=3,
    reps='10-15',
    weight='Moderate to heavy',
    description='Hold a dumbbell or barbell in your hands, arms at your sides. Raise your shoulders towards your ears as high as possible, then lower them back down.'
)

    # Full Body
    clean_and_press = Exercise(
    workout_id=19,  
    name='Clean and Press',
    sets=3,
    reps='6-8',
    weight='Heavy',
    description='Start with the barbell on the ground. Clean the barbell to shoulder height, then press it overhead. Lower the barbell back to shoulder height and then back to the ground.'
)

    goblet_squats = Exercise(
    workout_id=19,
    name='Goblet Squats',
    sets=3,
    reps='10-12',
    weight='Moderate',
    description='Hold a dumbbell or kettlebell close to your chest. Squat down until your thighs are parallel to the ground, then stand back up.'
)

    kettlebell_swings = Exercise(
    workout_id=19,
    name='Kettlebell Swings',
    sets=3,
    reps='12-15',
    weight='Moderate',
    description='Hold a kettlebell with both hands and swing it between your legs. Propel the kettlebell forward and upward to shoulder height using the power from your hips and legs.'
)

    renegade_rows = Exercise(
    workout_id=19,
    name='Renegade Rows',
    sets=3,
    reps='8-12 each side',
    weight='Moderate',
    description='Start in a plank position with a dumbbell in each hand. Row one dumbbell towards your hip while balancing on the other hand and feet. Alternate sides.'
)

    medicine_ball_slam = Exercise(
    workout_id=19,
    name='Medicine Ball Slams',
    sets=3,
    reps='10-15',
    weight='Moderate',
    description='Hold a medicine ball overhead with both hands. Slam the ball down to the ground as hard as possible, then pick it up and repeat.'
)

#**yoga**#
    # Beginner's Flow
    cat_cow_pose = Exercise(
    workout_id=20,  
    name='Cat-Cow Pose',
    sets=2,
    reps='10-15',
    weight='Bodyweight',
    description='This gentle flow between two poses warms the body and brings flexibility to the spine. Start on your hands and knees, with your wrists directly under your shoulders and your knees under your hips. Inhale as you arch your back, lifting your head and tailbone (Cow Pose), then exhale as you round your spine, tucking your chin and pelvis (Cat Pose).'
)

    downward_facing_dog = Exercise(
    workout_id=20,
    name='Downward-Facing Dog',
    sets=2,
    reps='Hold for 5-10 breaths',
    weight='Bodyweight',
    description='A full-body stretch that targets the shoulders, hamstrings, and calves. Start on your hands and knees, then lift your hips towards the ceiling, straightening your legs and forming an inverted V shape. Press your heels towards the ground and relax your head between your arms.'
)

    childs_pose = Exercise(
    workout_id=20,
    name='Child\'s Pose',
    sets=1,
    reps='Hold for 5-10 breaths',
    weight='Bodyweight',
    description='A resting pose that stretches the hips, thighs, and ankles while calming the mind. Sit back on your heels with your knees together or apart. Extend your arms forward on the mat, lowering your torso between your thighs and resting your forehead on the ground.'
)

    cobra_pose = Exercise(
    workout_id=20,
    name='Cobra Pose',
    sets=2,
    reps='10-12',
    weight='Bodyweight',
    description='This backbend strengthens the spine and opens the chest and shoulders. Lie on your stomach with your hands under your shoulders. Press into your hands, lifting your chest off the ground while keeping your elbows slightly bent.'
)

    warrior_i_pose = Exercise(
    workout_id=20,
    name='Warrior I Pose',
    sets=2,
    reps='Hold for 5-10 breaths each side',
    weight='Bodyweight',
    description='Strengthens the legs and arms while improving balance and concentration. From a standing position, step one foot back, turning it slightly outward. Bend your front knee and raise your arms overhead, keeping your hips square to the front.'
)


    # Intermediate Flow
    sun_salutation_a = Exercise(
    workout_id=21,  
    name='Sun Salutation A',
    sets=2,
    reps='5-7',
    weight='Bodyweight',
    description='A series of poses that warm up the body and increase flexibility. This flow typically includes Mountain Pose, Forward Bend, Plank, Chaturanga, Upward Dog, and Downward Dog, repeated in a sequence.'
)

    warrior_ii_pose = Exercise(
    workout_id=21,
    name='Warrior II Pose',
    sets=2,
    reps='Hold for 5-10 breaths each side',
    weight='Bodyweight',
    description='Strengthens the legs, opens the hips and chest, and improves focus. From Warrior I, open your hips to the side, extend your arms out parallel to the ground, and gaze over your front hand.'
)

    triangle_pose = Exercise(
    workout_id=21,
    name='Triangle Pose',
    sets=2,
    reps='Hold for 5-10 breaths each side',
    weight='Bodyweight',
    description='Stretches the legs, groin, hips, shoulders, chest, and spine. From Warrior II, straighten your front leg and reach your front hand towards your shin or the floor, while extending your other arm towards the ceiling.'
)

    extended_side_angle_pose = Exercise(
    workout_id=21,
    name='Extended Side Angle Pose',
    sets=2,
    reps='Hold for 5-10 breaths each side',
    weight='Bodyweight',
    description='Strengthens and stretches the legs, knees, and ankles, while also stretching the groin, spine, waist, chest, lungs, and shoulders. From Warrior II, lower your front elbow to your knee or place your hand on the ground inside your foot, extending your top arm over your ear.'
)

    boat_pose_intermediate = Exercise(
    workout_id=21,
    name='Boat Pose',
    sets=2,
    reps='Hold for 5-10 breaths',
    weight='Bodyweight',
    description='Strengthens the abdominal muscles, hip flexors, and spine. Sit on the ground with your knees bent. Lean back slightly and lift your feet off the ground, extending your legs and balancing on your sit bones.'
)

    # Advanced Flow
    crow_pose = Exercise(
    workout_id=22,  
    name='Crow Pose',
    sets=2,
    reps='Hold for 5-10 breaths',
    weight='Bodyweight',
    description='An arm balance that strengthens the arms, wrists, and abdominal muscles. Squat with your hands on the ground in front of you. Lean forward, lifting your feet off the ground, and balance your knees on the backs of your upper arms.'
)

    headstand = Exercise(
    workout_id=22,
    name='Headstand',
    sets=2,
    reps='Hold for 5-10 breaths',
    weight='Bodyweight',
    description='Increases strength in the shoulders, arms, and core while improving balance. Kneel on the ground and interlace your fingers, placing your forearms on the ground. Place the crown of your head on the ground and lift your legs towards the ceiling, balancing on your head and forearms.'
)

    forearm_stand = Exercise(
    workout_id=22,
    name='Forearm Stand',
    sets=2,
    reps='Hold for 5-10 breaths',
    weight='Bodyweight',
    description='Strengthens the shoulders, arms, and core, and improves balance and concentration. Start in a dolphin pose with your forearms on the ground. Kick up into a forearm stand, balancing your legs in the air.'
)

    king_pigeon_pose = Exercise(
    workout_id=22,
    name='King Pigeon Pose',
    sets=2,
    reps='Hold for 5-10 breaths each side',
    weight='Bodyweight',
    description='Stretches the thighs, groins, and abdomen, opens the shoulders and chest, and stimulates the organs of the abdomen. From a low lunge, slide your front foot towards your opposite hand, extending your back leg straight. Bend your back leg and reach for your foot with your hands.'
)

    wheel_pose = Exercise(
    workout_id=22,
    name='Wheel Pose',
    sets=2,
    reps='Hold for 5-10 breaths',
    weight='Bodyweight',
    description='A backbend that strengthens the arms, legs, abdomen, and spine, while also opening the chest and shoulders. Lie on your back with your knees bent and feet flat on the ground. Place your hands by your ears and press into your hands and feet, lifting your body into a bridge.'
)

    # Flexibility and Balance Flow
    half_moon_pose = Exercise(
    workout_id=23,  
    name='Half Moon Pose',
    sets=2,
    reps='Hold for 5-10 breaths each side',
    weight='Bodyweight',
    description='Improves balance and strengthens the legs and core while opening the hips and chest. From Warrior II, place your front hand on the ground or a block, and lift your back leg parallel to the ground while extending your top arm towards the ceiling.'
)

    tree_pose = Exercise(
    workout_id=23,
    name='Tree Pose',
    sets=2,
    reps='Hold for 10-15 breaths each side',
    weight='Bodyweight',
    description='Enhances balance and stability in the legs, and strengthens the calves and ankles. Stand on one leg and place the sole of your other foot on your inner thigh or calf. Bring your hands together in front of your chest or extend them overhead.'
)

    dancers_pose = Exercise(
    workout_id=23,
    name='Dancer\'s Pose',
    sets=2,
    reps='Hold for 5-10 breaths each side',
    weight='Bodyweight',
    description='Stretches the shoulders, chest, thighs, groin, and abdomen, and strengthens the legs and ankles. Stand on one leg, bend your other knee and grab your ankle or foot behind you. Lift your leg and extend your opposite arm forward.'
)

    standing_forward_bend = Exercise(
    workout_id=23,
    name='Standing Forward Bend',
    sets=2,
    reps='Hold for 10-15 breaths',
    weight='Bodyweight',
    description='Stretches the hamstrings, calves, and hips, and strengthens the thighs and knees. Stand with your feet hip-width apart, bend forward from your hips, and reach for the ground or your feet.'
)

    pigeon_pose = Exercise(
    workout_id=23,
    name='Pigeon Pose',
    sets=2,
    reps='Hold for 5-10 breaths each side',
    weight='Bodyweight',
    description='Opens the hips and stretches the thighs and glutes. From a downward-facing dog, bring one knee forward and place it behind your wrist. Extend the other leg straight back and lower your hips towards the ground.'
)

    # Core Strength Flow
    plank_pose = Exercise(
    workout_id=24,  
    name='Plank Pose',
    sets=3,
    reps='Hold for 30-60 seconds',
    weight='Bodyweight',
    description='Strengthens the core, shoulders, and back. Start in a push-up position with your body in a straight line from head to heels. Engage your core and hold the position.'
)

    side_plank_pose = Exercise(
    workout_id=24,
    name='Side Plank Pose',
    sets=3,
    reps='Hold for 20-40 seconds each side',
    weight='Bodyweight',
    description='Targets the obliques and strengthens the shoulders. Lie on your side, propped up on your forearm, and lift your hips off the ground, holding the position. Repeat on the other side.'
)

    boat_pose = Exercise(
    workout_id=24,
    name='Boat Pose',
    sets=3,
    reps='Hold for 20-40 seconds',
    weight='Bodyweight',
    description='Strengthens the abdominal muscles and hip flexors. Sit on the floor, lean back slightly, and lift your legs to form a V shape with your body. Extend your arms forward and hold the position.'
)

    crow_pose = Exercise(
    workout_id=24,
    name='Crow Pose',
    sets=3,
    reps='Hold for 10-20 seconds',
    weight='Bodyweight',
    description='An arm balance that engages the core and arms. Squat with your hands on the ground, lean forward, and lift your feet off the ground, balancing on your arms.'
)

    dolphin_plank_pose = Exercise(
    workout_id=24,
    name='Dolphin Plank Pose',
    sets=3,
    reps='Hold for 30-60 seconds',
    weight='Bodyweight',
    description='A variation of the plank pose that engages the core and shoulders. Start in a forearm plank position, keeping your body in a straight line. Press your heels towards the ground and hold.'
)

    # Relaxation and Recovery Flow
    legs_up_the_wall_pose = Exercise(
    workout_id=25, 
    name='Legs-Up-the-Wall Pose',
    sets=1,
    reps='Hold for 5-15 minutes',
    weight='Bodyweight',
    description='A restorative pose that promotes relaxation and improves circulation. Lie on your back with your legs extended up against a wall and your arms at your sides. Close your eyes and breathe deeply.'
)

    reclining_bound_angle_pose = Exercise(
    workout_id=25,
    name='Reclining Bound Angle Pose',
    sets=1,
    reps='Hold for 5-10 minutes',
    weight='Bodyweight',
    description='Opens the hips and stretches the inner thighs. Lie on your back with the soles of your feet together and knees dropping towards the floor. Place your hands on your abdomen or extend them out to the sides.'
)

    supine_twist = Exercise(
    workout_id=25,
    name='Supine Twist',
    sets=1,
    reps='Hold for 1-2 minutes each side',
    weight='Bodyweight',
    description='Relieves tension in the spine and stretches the back and hips. Lie on your back, draw one knee towards your chest, and then gently twist it across your body to the floor, extending your arm out to the side.'
)

    corpse_pose = Exercise(
    workout_id=25,
    name='Corpse Pose',
    sets=1,
    reps='Hold for 5-10 minutes',
    weight='Bodyweight',
    description='A resting pose that promotes relaxation and mindfulness. Lie flat on your back with your arms at your sides and palms facing up. Close your eyes and focus on your breath, letting go of any tension.'
)

    happy_baby_pose = Exercise(
    workout_id=25,
    name='Happy Baby Pose',
    sets=1,
    reps='Hold for 1-2 minutes',
    weight='Bodyweight',
    description='Stretches the hips and relieves tension in the lower back. Lie on your back, bend your knees towards your chest, and hold the outer edges of your feet with your hands. Gently rock side to side if desired.'
)


#**Weight_loss**#
    # Full Body HIIT Exercises
    jumping_jacks = Exercise(
    workout_id=28,
    name="Jumping Jacks",
    sets=3,
    reps="30-45 seconds",    
    weight="Bodyweight",
    description="Stand with your feet together and hands by your sides. Jump your feet out to the sides while raising your arms overhead. Jump back to the starting position. Repeat quickly."
)

    burpees = Exercise(
    workout_id=28,
    name="Burpees",
    sets=3,
    reps="15-20",    
    weight="Bodyweight",
    description="Stand with your feet shoulder-width apart. Drop into a squat position, place your hands on the floor, and kick your feet back into a plank position. Perform a push-up, then jump your feet back to your hands and explosively jump into the air."
)

    mountain_climbers = Exercise(
    workout_id=28,
    name="Mountain Climbers",
    sets=3,
    reps="30-45 seconds",
    weight="Bodyweight",
    description="Start in a plank position with your hands under your shoulders. Quickly alternate driving your knees towards your chest as if running in place, keeping your core tight and back straight."
)

    high_knees = Exercise(
    workout_id=28,
    name="High Knees",
    sets=3,
    reps="30-45 seconds",
    weight="Bodyweight",
    description="Stand with your feet hip-width apart. Run in place, bringing your knees as high as possible towards your chest while pumping your arms."
)

    plank = Exercise(
    workout_id=28,
    name="Plank",
    sets=3,
    reps="30-60 seconds",
    weight="Bodyweight",
    description="Start in a forearm plank position with your body in a straight line from head to heels. Engage your core and hold this position without letting your hips sag or rise."
)

# Lower Body Burn Exercises
    squats = Exercise(
    workout_id=29,
    name="Squats",
    sets=3,
    reps="15-20",    
    weight="Bodyweight or light dumbbells",
    description="Stand with your feet shoulder-width apart. Lower your body by bending your knees and pushing your hips back as if sitting in a chair. Keep your chest up and lower until your thighs are parallel to the ground, then stand back up."
)

    lunges = Exercise(
    workout_id=29,
    name="Lunges",
    sets=3,
    reps="12-15 each leg",    
    weight="Bodyweight or light dumbbells",
    description="Stand with your feet together. Step forward with one leg and lower your body until both knees are bent at 90-degree angles. Push through the front heel to return to the starting position and switch legs.",
)

    glute_bridges = Exercise(
    workout_id=29,
    name="Glute Bridges",
    sets=3,
    reps="15-20",    
    weight="Bodyweight or light dumbbells",
    description="Lie on your back with your knees bent and feet flat on the floor. Lift your hips towards the ceiling by squeezing your glutes and pressing through your heels. Hold at the top for a moment, then lower back down."
)

    step_ups = Exercise(
    workout_id=29,
    name="Step-Ups",
    sets=3,
    reps="12-15 each leg",
    weight="Bodyweight or light dumbbells",
    description="Stand in front of a sturdy bench or step. Step up with one foot, then the other, bringing both feet onto the bench. Step back down with the same leg first. Alternate starting legs."
)

    calf_raises = Exercise(
    workout_id=29,
    name="Calf Raises",
    sets=3,
    reps="20-25",
    weight="Bodyweight or light dumbbells",
    description="Stand with your feet hip-width apart. Raise your heels off the ground as high as possible, then lower back down. You can hold onto a wall or chair for balance."
)

# Upper Body Blast Exercises
    push_ups = Exercise(
    workout_id=30,
    name="Push-Ups",
    sets=3,
    reps="10-15",
    weight="Bodyweight",
    description="Start in a plank position with your hands slightly wider than shoulder-width apart. Lower your body until your chest nearly touches the floor, keeping your elbows close to your body. Push back up to the starting position."
)

    dumbbell_rows = Exercise(
    workout_id=30,
    name="Dumbbell Rows",
    sets=3,
    reps="12-15",
    weight="Light to moderate dumbbells",
    description="Stand with your feet hip-width apart, holding a dumbbell in each hand. Bend forward at the hips, keeping your back straight. Pull the dumbbells towards your hips, squeezing your shoulder blades together, then lower back down."
)

    shoulder_press = Exercise(
    workout_id=30,
    name="Shoulder Press",
    sets=3,
    reps="10-12",    
    weight="Light to moderate dumbbells",
    description="Stand with your feet shoulder-width apart, holding dumbbells at shoulder height. Press the dumbbells overhead until your arms are fully extended, then lower them back to shoulder height."
)

    bicep_curls = Exercise(
    workout_id=30,
    name="Bicep Curls",
    sets=3,
    reps="12-15",    
    weight="Light to moderate dumbbells",
    description="Stand with your feet shoulder-width apart, holding a dumbbell in each hand. Curl the dumbbells towards your shoulders, keeping your elbows close to your body, then lower back down."
)

    tricep_dips = Exercise(
    workout_id=30,
    name="Tricep Dips",
    sets=3,
    reps="10-15",    
    weight="Bodyweight",
    description="Sit on the edge of a bench or chair with your hands next to your hips. Slide your butt off the edge and lower your body by bending your elbows. Push through your palms to return to the starting position."
)

# Core Conditioning Exercises
    bicycle_crunches = Exercise(
    workout_id=31,
    name="Bicycle Crunches",
    sets=3,
    reps="20-30",    
    weight="Bodyweight",
    description="Lie on your back with your hands behind your head and legs lifted off the ground. Bring one knee towards your chest while rotating your opposite elbow towards it. Switch sides in a pedaling motion."
)

    russian_twists = Exercise(
    workout_id=31,
    name="Russian Twists",
    sets=3,
    reps="20-30",    
    weight="Light dumbbell or medicine ball",
    description="Sit on the floor with your knees bent and feet lifted off the ground. Hold a dumbbell or medicine ball with both hands and rotate your torso to the left, then to the right, tapping the weight on the floor each side."
)

    plank_with_shoulder_taps = Exercise(
    workout_id=31,
    name="Plank with Shoulder Taps",
    sets=3,
    reps="20-30 taps",    
    weight="Bodyweight",
    description="Start in a plank position with your hands under your shoulders. Tap one hand to the opposite shoulder while maintaining a stable core. Alternate sides."
)

    leg_raises = Exercise(
    workout_id=31,
    name="Leg Raises",
    sets=3,
    reps="15-20",
    weight="Bodyweight",
    description="Lie on your back with your legs straight. Lift your legs towards the ceiling until they are perpendicular to the floor, then lower them back down without touching the ground."
)

    side_plank = Exercise(
    workout_id=31,
    name="Side Plank",
    sets=3,
    reps="30-45 seconds each side",    
    weight="Bodyweight",
    description="Lie on your side with your elbow directly under your shoulder. Lift your hips off the ground, creating a straight line from head to feet. Hold this position, then switch sides."
)

# Cardio Circuit Exercises
    jump_rope = Exercise(
    workout_id=32,
    name="Jump Rope",
    sets=3,
    reps="1-2 minutes",    
    weight="Bodyweight",
    description="Stand with your feet together and hold the jump rope handles with your hands at your sides. Swing the rope over your head and jump as it passes under your feet. Continue jumping in a smooth, continuous motion."
)

    running = Exercise(
    workout_id=32,
    name="Running",
    sets=1,
    reps="20-30 minutes",    
    weight="Bodyweight",
    description="Run at a steady pace on a treadmill or outside, maintaining a consistent speed that challenges you but allows you to keep moving."
)

    cycling = Exercise(
    workout_id=32,
    name="Cycling",
    sets=1,
    reps="20-30 minutes",    
    weight="Bodyweight",
    description="Cycle on a stationary bike or outdoor bike at a moderate to high intensity, adjusting the resistance to challenge your cardiovascular system."
)

    rowing = Exercise(
    workout_id=32,
    name="Rowing",
    sets=1,
    reps="15-20 minutes",    
    weight="Bodyweight",
    description="Use a rowing machine to perform rowing motions with a focus on engaging both your upper and lower body. Maintain a steady pace and proper form."
)

    burpees_cardio = Exercise(
    workout_id=32,
    name="Burpees",
    sets=3,
    reps="10-15",    
    weight="Bodyweight",
    description="Stand with your feet shoulder-width apart. Drop into a squat position, place your hands on the floor, and kick your feet back into a plank position. Perform a push-up, then jump your feet back to your hands and explosively jump into the air."
)

    # Upper Body Circuit Exercises
    dumbbell_chest_press = Exercise(
    workout_id=33,
    name="Dumbbell Chest Press",
    sets=3,
    reps="12-15",
    weight="Moderate dumbbells",
    description="Lie on a bench with a dumbbell in each hand, palms facing forward. Press the dumbbells above your chest and then lower them until your elbows are at a 90-degree angle."
)

    dumbbell_flyes = Exercise(
    workout_id=33,
    name="Dumbbell Flyes",
    sets=3,
    reps="12-15",
    weight="Moderate dumbbells",
    description="Lie on a bench with a dumbbell in each hand, palms facing each other. With a slight bend in your elbows, open your arms out to the sides and then bring them back together above your chest."
)

    lat_pulldowns = Exercise(
    workout_id=33,
    name="Lat Pulldowns",
    sets=3,
    reps="12-15",
    weight="Machine weight",
    description="Sit at a lat pulldown machine and grip the bar with your hands slightly wider than shoulder-width. Pull the bar down towards your chest, squeezing your shoulder blades together, then slowly return to the starting position."
)

    dumbbell_shoulder_raises = Exercise(
    workout_id=33,
    name="Dumbbell Shoulder Raises",
    sets=3,
    reps="12-15",
    weight="Light to moderate dumbbells",
    description="Stand with a dumbbell in each hand at your sides. Raise the dumbbells to shoulder height, keeping your arms straight, then lower them back down."
)

    tricep_kickbacks = Exercise(
    workout_id=33,
    name="Tricep Kickbacks",
    sets=3,
    reps="12-15",
    weight="Light to moderate dumbbells",
    description="Lean forward with a dumbbell in one hand, elbow bent at 90 degrees. Extend your arm behind you until it's straight, then return to the starting position."
)

    # Lower Body Circuit Exercises
    goblet_squats = Exercise(
    workout_id=34,
    name="Goblet Squats",
    sets=3,
    reps="15-20",
    weight="Moderate dumbbell or kettlebell",
    description="Hold a dumbbell or kettlebell close to your chest with both hands. Squat down by bending your knees and pushing your hips back, keeping your chest up. Return to standing."
)

    bulgarian_split_squats = Exercise(
    workout_id=34,
    name="Bulgarian Split Squats",
    sets=3,
    reps="12-15 each leg",
    weight="Bodyweight or light dumbbells",
    description="Stand with one foot on a bench behind you. Lower your body by bending your front knee until your thigh is parallel to the ground, then return to the starting position."
)

    deadlifts = Exercise(
    workout_id=34,
    name="Deadlifts",
    sets=3,
    reps="12-15",
    weight="Barbell or dumbbells",
    description="Stand with your feet hip-width apart and a barbell in front of you. Bend at the hips and knees to grip the bar, then lift it by extending your hips and knees until you’re standing upright."
)

    lateral_lunges = Exercise(
    workout_id=34,
    name="Lateral Lunges",
    sets=3,
    reps="12-15 each leg",
    weight="Bodyweight or light dumbbells",
    description="Step out to the side with one leg and lower your body by bending that knee, keeping the other leg straight. Push back to the starting position and switch legs."
)

    hamstring_curls = Exercise(
    workout_id=34,
    name="Hamstring Curls",
    sets=3,
    reps="15-20",
    weight="Machine weight",
    description="Lie face down on a hamstring curl machine with your legs under the pad. Curl your legs up towards your glutes, then lower them back down."
)

    # Core Circuit Exercises
    v_ups = Exercise(
    workout_id=35,
    name="V-Ups",
    sets=3,
    reps="15-20",
    weight="Bodyweight",
    description="Lie on your back with your arms extended overhead and legs straight. Lift your legs and upper body simultaneously to form a V shape, reaching your hands towards your feet."
)

    hanging_leg_raises = Exercise(
    workout_id=35,
    name="Hanging Leg Raises",
    sets=3,
    reps="10-15",
    weight="Bodyweight",
    description="Hang from a pull-up bar with your legs straight. Raise your legs until they are parallel to the ground, then lower them back down."
)

    side_plank_hip_lifts = Exercise(
    workout_id=35,
    name="Side Plank Hip Lifts",
    sets=3,
    reps="15-20 each side",
    weight="Bodyweight",
    description="Lie on your side with your elbow under your shoulder. Lift your hips off the ground and hold, then lower back down. Perform on each side."
)

    reverse_crunches = Exercise(
    workout_id=35,
    name="Reverse Crunches",
    sets=3,
    reps="15-20",
    weight="Bodyweight",
    description="Lie on your back with your legs bent and feet off the ground. Lift your hips towards your chest and then lower them back down."
)

    ab_wheel_rollouts = Exercise(
    workout_id=35,
    name="Ab Wheel Rollouts",
    sets=3,
    reps="10-15",
    weight="Ab wheel",
    description="Kneel on the ground and grip an ab wheel. Roll the wheel forward while keeping your body in a straight line, then roll it back to the starting position."
)

    # HIIT Challenge Exercises
    burpees = Exercise(
    workout_id=36,
    name="Burpees",
    sets=3,
    reps="20-25",
    weight="Bodyweight",
    description="Stand with your feet shoulder-width apart. Drop into a squat position, place your hands on the floor, and kick your feet back into a plank position. Perform a push-up, then jump your feet back to your hands and explosively jump into the air."
)

    jump_squats = Exercise(
    workout_id=36,
    name="Jump Squats",
    sets=3,
    reps="15-20",
    weight="Bodyweight",
    description="Stand with your feet shoulder-width apart. Lower into a squat and then explode upward into a jump. Land softly and repeat."
)

    mountain_climbers = Exercise(
    workout_id=36,
    name="Mountain Climbers",
    sets=3,
    reps="30-45 seconds",
    weight="Bodyweight",
    description="Start in a plank position with your hands under your shoulders. Quickly alternate driving your knees towards your chest as if running in place, keeping your core tight and back straight."
)

    high_knees = Exercise(
    workout_id=36,
    name="High Knees",
    sets=3,
    reps="30-45 seconds",
    weight="Bodyweight",
    description="Stand with your feet hip-width apart. Run in place, bringing your knees as high as possible towards your chest while pumping your arms."
)

    plank_jacks = Exercise(
    workout_id=36,
    name="Plank Jacks",
    sets=3,
    reps="30-45 seconds",
    weight="Bodyweight",
    description="Start in a plank position with your hands under your shoulders. Jump your feet out to the sides and then back together, keeping your core tight and body steady."
)

#**Cardio**#
    # HIIT Circuit 1

    burpees = Exercise(
    workout_id=1,
    name="Burpees",
    sets=4,
    reps="1 minute",
    weight="Bodyweight",
    description="Start standing, drop into a squat, kick your feet back into a plank, perform a push-up, jump your feet back to your hands, and explosively jump into the air. Repeat."
)

    jumping_jacks = Exercise(
    workout_id=1,
    name="Jumping Jacks",
    sets=4,
    reps="1 minute",
    weight="Bodyweight",
    description="Stand with feet together and jump while spreading your legs and raising your arms above your head. Return to the starting position and repeat."
)

    mountain_climbers = Exercise(
    workout_id=1,
    name="Mountain Climbers",
    sets=4,
    reps="1 minute",
    weight="Bodyweight",
    description="In a plank position, alternate bringing your knees towards your chest rapidly as if climbing."
)

    rest_hiit_circuit_1 = Exercise(
    workout_id=1,
    name="Rest",
    sets=4,
    reps="1 minute",
    weight="Bodyweight",
    description="Rest between sets."
)

# HIIT Circuit 2
    jump_squats = Exercise(
    workout_id=2,
    name="Jump Squats",
    sets=4,
    reps="1 minute",
    weight="Bodyweight",
    description="Perform a squat and then explode upwards into a jump, landing softly and going straight back into the squat."
)

    high_knees = Exercise(
    workout_id=2,
    name="High Knees",
    sets=4,
    reps="1 minute",
    weight="Bodyweight",
    description="Jog in place while lifting your knees as high as possible, aiming to get your thighs parallel to the ground."
)

    lunges = Exercise(
    workout_id=2,
    name="Lunges",
    sets=4,
    reps="1 minute",
    weight="Bodyweight",
    description="Perform alternating lunges, stepping forward and lowering your hips until both knees are bent at about a 90-degree angle."
)

    rest_hiit_circuit_2 = Exercise(
    workout_id=2,
    name="Rest",
    sets=4,
    reps="1 minute",
    weight="Bodyweight",
    description="Rest between sets."
)

# Steady-State Cardio
    running_or_jogging = Exercise(
    workout_id=3,
    name="Running or Jogging",
    sets=1,
    reps="30-45 minutes",
    weight="Bodyweight",
    description="Maintain a steady pace, focusing on breathing and endurance."
)

    cycling = Exercise(
    workout_id=3,
    name="Cycling",
    sets=1,
    reps="30-45 minutes",
    weight="Bodyweight",
    description="Ride at a consistent speed on a stationary bike or outdoors."
)

    rowing = Exercise(
    workout_id=3,
    name="Rowing",
    sets=1,
    reps="30 minutes",
    weight="Bodyweight",
    description="Use a rowing machine at a steady pace to engage the full body."
)

    elliptical_machine = Exercise(
    workout_id=3,
    name="Elliptical Machine",
    sets=1,
    reps="30-45 minutes",
    weight="Bodyweight",
    description="Low-impact machine simulating running or walking."
)

# Tabata Training
    sprints = Exercise(
    workout_id=4,
    name="Sprints",
    sets=8,
    reps="20 seconds",
    weight="Bodyweight",
    description="Sprint as fast as possible."
)

    rest_tabata_1 = Exercise(
    workout_id=4,
    name="Rest",
    sets=8,
    reps="10 seconds",
    weight="Bodyweight",
    description="Rest between sprints."
)

    jumping_squats = Exercise(
    workout_id=4,
    name="Jumping Squats",
    sets=8,
    reps="20 seconds",
    weight="Bodyweight",
    description="Perform squats with an explosive jump."
)

    rest_tabata_2 = Exercise(
    workout_id=4,
    name="Rest",
    sets=8,
    reps="10 seconds",
    weight="Bodyweight",
    description="Rest between jumping squats."
)

# Cardio Circuits
    jumping_rope = Exercise(
    workout_id=5,
    name="Jumping Rope",
    sets=2,
    reps="1 minute",
    weight="Bodyweight",
    description="Continuous jumping rope to elevate heart rate."
)

    high_knees_cardio_circuits = Exercise(
    workout_id=5,
    name="High Knees",
    sets=2,
    reps="1 minute",
    weight="Bodyweight",
    description="Jog in place with high knee lifts."
)

    jumping_jacks_cardio_circuits = Exercise(
    workout_id=5,
    name="Jumping Jacks",
    sets=2,
    reps="1 minute",
    weight="Bodyweight",
    description="Full-body exercise with jumping and arm movements."
)

    rest_cardio_circuits = Exercise(
    workout_id=5,
    name="Rest",
    sets=2,
    reps="1 minute",
    weight="Bodyweight",
    description="Rest between circuits."
)

    running_in_place = Exercise(
    workout_id=5,
    name="Running in Place",
    sets=2,
    reps="1 minute",
    weight="Bodyweight",
    description="Jogging on the spot to keep the heart rate up."
)

    butt_kicks = Exercise(
    workout_id=5,
    name="Butt Kicks",
    sets=2,
    reps="1 minute",
    weight="Bodyweight",
    description="High-speed jogging with heel kicks towards glutes."
)

    mountain_climbers_cardio_circuits = Exercise(
    workout_id=5,
    name="Mountain Climbers",
    sets=2,
    reps="1 minute",
    weight="Bodyweight",
    description="Perform rapid knee-to-chest movement in a standing plank position."
)

# Jump Rope
    basic_jump_rope = Exercise(
    workout_id=6,
    name="Basic Jump Rope",
    sets=1,
    reps="10 minutes",
    weight="Bodyweight",
    description="Continuous jumping at a steady pace."
)

    interval_jump_rope = Exercise(
    workout_id=6,
    name="Interval Jump Rope",
    sets=1,
    reps="20 minutes",
    weight="Bodyweight",
    description="Alternate between 1 minute of fast jumping and 30 seconds of slow jumping or rest."
)

    alternate_foot_jumping = Exercise(
    workout_id=6,
    name="Alternate Foot Jumping",
    sets=1,
    reps="1 minute",
    weight="Bodyweight",
    description="Jump rope while alternating feet."
)

    double_unders = Exercise(
    workout_id=6,
    name="Double Unders",
    sets=1,
    reps="1 minute",
    weight="Bodyweight",
    description="Rope passes under feet twice per jump."
)

    side_to_side_jumps = Exercise(
    workout_id=6,
    name="Side-to-Side Jumps",
    sets=1,
    reps="1 minute",
    weight="Bodyweight",
    description="Jump rope while moving feet side to side."
)

# Hiking
    hill_hike = Exercise(
    workout_id=7,
    name="Hill Hike",
    sets=1,
    reps="45-60 minutes",
    weight="Bodyweight",
    description="Hike on hilly terrain to challenge endurance and strength."
)

    trail_hike = Exercise(
    workout_id=7,
    name="Trail Hike",
    sets=1,
    reps="1-2 hours",
    weight="Bodyweight",
    description="Hike on varied trails, focusing on endurance and navigation."
)

    uphill_hiking = Exercise(
    workout_id=7,
    name="Uphill Hiking",
    sets=1,
    reps="30 minutes",
    weight="Bodyweight",
    description="Hiking on inclines to increase intensity."
)

    downhill_hiking = Exercise(
    workout_id=7,
    name="Downhill Hiking",
    sets=1,
    reps="30 minutes",
    weight="Bodyweight",
    description="Navigating down slopes to work different muscle groups."
)

    steep_inclines = Exercise(
    workout_id=7,
    name="Steep Inclines",
    sets=1,
    reps="30 minutes",
    weight="Bodyweight",
    description="Hiking on steep trails for added challenge."
)

    trail_exploration = Exercise(
    workout_id=7,
    name="Trail Exploration",
    sets=1,
    reps="1-2 hours",
    weight="Bodyweight",
    description="Hiking diverse trails for a full workout experience."
)


# Stair Climbing Exercises
    stair_climb = Exercise(
    workout_id=8,
    name="Stair Climb",
    sets=1,
    reps="20-30 minutes",
    weight="Bodyweight",
    description="Climb stairs continuously for 20-30 minutes."
)

    stair_intervals = Exercise(
    workout_id=8,
    name="Stair Intervals",
    sets=1,
    reps="20 minutes",
    weight="Bodyweight",
    description="Alternate between running up and walking down the stairs for 20 minutes."
)

    basic_stair_climbing = Exercise(
    workout_id=8,
    name="Basic Stair Climbing",
    sets=1,
    reps="10 minutes",
    weight="Bodyweight",
    description="Climb stairs at a steady pace for 10 minutes."
)

    step_ups = Exercise(
    workout_id=8,
    name="Step-Ups",
    sets=1,
    reps="10 minutes",
    weight="Bodyweight",
    description="Perform step-ups on a platform for 10 minutes."
)

    high_knees_on_stairs = Exercise(
    workout_id=8,
    name="High Knees on Stairs",
    sets=1,
    reps="10 minutes",
    weight="Bodyweight",
    description="Perform high knees while climbing stairs for 10 minutes."
)

    fast_steps = Exercise(
    workout_id=8,
    name="Fast Steps",
    sets=1,
    reps="10 minutes",
    weight="Bodyweight",
    description="Climb stairs as quickly as possible for 10 minutes."
)

# Bodyweight Cardio Exercises
    burpees = Exercise(
    workout_id=9,
    name="Burpees",
    sets=1,
    reps="1 minute",
    weight="Bodyweight",
    description="Perform burpees for 1 minute."
)

    high_knees = Exercise(
    workout_id=9,
    name="High Knees",
    sets=1,
    reps="1 minute",
    weight="Bodyweight",
    description="Run in place with high knees for 1 minute."
)

    jumping_jacks = Exercise(
    workout_id=9,
    name="Jumping Jacks",
    sets=1,
    reps="1 minute",
    weight="Bodyweight",
    description="Perform jumping jacks for 1 minute."
)

    mountain_climbers = Exercise(
    workout_id=9,
    name="Mountain Climbers",
    sets=1,
    reps="1 minute",
    weight="Bodyweight",
    description="Perform mountain climbers for 1 minute."
)

    rest = Exercise(
    workout_id=9,
    name="Rest",
    sets=1,
    reps="1 minute",
    weight="Bodyweight",
    description="Rest for 1 minute."
)

    jump_squats = Exercise(
    workout_id=9,
    name="Jump Squats",
    sets=1,
    reps="30 seconds",
    weight="Bodyweight",
    description="Perform jump squats for 30 seconds."
)

    skaters = Exercise(
    workout_id=9,
    name="Skaters",
    sets=1,
    reps="30 seconds",
    weight="Bodyweight",
    description="Perform skaters for 30 seconds."
)

    jump_lunges = Exercise(
    workout_id=9,
    name="Jump Lunges",
    sets=1,
    reps="30 seconds",
    weight="Bodyweight",
    description="Perform jump lunges for 30 seconds."
)

    rest_30s = Exercise(
    workout_id=9,
    name="Rest",
    sets=1,
    reps="30 seconds",
    weight="Bodyweight",
    description="Rest for 30 seconds."
)

# Elliptical Trainer Exercises
    steady_state_elliptical = Exercise(
    workout_id=10,
    name="Steady-State Elliptical",
    sets=1,
    reps="30-45 minutes",
    weight="Bodyweight",
    description="Use the elliptical machine at a steady pace for 30-45 minutes."
)

    elliptical_intervals = Exercise(
    workout_id=10,
    name="Elliptical Intervals",
    sets=1,
    reps="20 minutes",
    weight="Bodyweight",
    description="Alternate between high and low resistance on the elliptical for 20 minutes."
)

    forward_elliptical_stride = Exercise(
    workout_id=10,
    name="Forward Elliptical Stride",
    sets=1,
    reps="10 minutes",
    weight="Bodyweight",
    description="Perform forward strides on the elliptical for 10 minutes."
)

    backward_elliptical_stride = Exercise(
    workout_id=10,
    name="Backward Elliptical Stride",
    sets=1,
    reps="10 minutes",
    weight="Bodyweight",
    description="Perform backward strides on the elliptical for 10 minutes."
)

    high_resistance_intervals = Exercise(
    workout_id=10,
    name="High-Resistance Intervals",
    sets=1,
    reps="10 minutes",
    weight="Bodyweight",
    description="Alternate between high and low resistance intervals on the elliptical for 10 minutes."
)

    low_resistance_endurance = Exercise(
    workout_id=10,
    name="Low-Resistance Endurance",
    sets=1,
    reps="10 minutes",
    weight="Bodyweight",
    description="Maintain a low resistance for endurance training on the elliptical for 10 minutes."
)

    incline_adjustments = Exercise(
    workout_id=10,
    name="Incline Adjustments",
    sets=1,
    reps="10 minutes",
    weight="Bodyweight",
    description="Adjust the incline of the elliptical and perform exercises for 10 minutes."
)

# Recumbent Bike Exercises
    steady_state_recumbent_bike = Exercise(
    workout_id=11,
    name="Steady-State Recumbent Bike",
    sets=1,
    reps="30-45 minutes",
    weight="Bodyweight",
    description="Cycle on the recumbent bike at a steady pace for 30-45 minutes."
)

    recumbent_bike_intervals = Exercise(
    workout_id=11,
    name="Recumbent Bike Intervals",
    sets=1,
    reps="20 minutes",
    weight="Bodyweight",
    description="Alternate between high and low resistance on the recumbent bike for 20 minutes."
)

    steady_cycling = Exercise(
    workout_id=11,
    name="Steady Cycling",
    sets=1,
    reps="10 minutes",
    weight="Bodyweight",
    description="Cycle steadily on the recumbent bike for 10 minutes."
)

    high_resistance_intervals_recumbent = Exercise(
    workout_id=11,
    name="High-Resistance Intervals",
    sets=1,
    reps="10 minutes",
    weight="Bodyweight",
    description="Alternate between high and low resistance intervals on the recumbent bike for 10 minutes."
)

    low_resistance_endurance_recumbent = Exercise(
    workout_id=11,
    name="Low-Resistance Endurance",
    sets=1,
    reps="10 minutes",
    weight="Bodyweight",
    description="Maintain a low resistance for endurance cycling on the recumbent bike for 10 minutes."
)

    hill_climb_simulation = Exercise(
    workout_id=11,
    name="Hill Climb Simulation",
    sets=1,
    reps="20-30 minutes",
    weight="Bodyweight",
    description="Simulate hill climbing on the recumbent bike for 20-30 minutes."
)

# Forest Biking Exercises
    trail_ride = Exercise(
    workout_id=12,
    name="Trail Ride",
    sets=1,
    reps="45-60 minutes",
    weight="Bodyweight",
    description="Ride on trails for 45-60 minutes."
)

    interval_trail_riding = Exercise(
    workout_id=12,
    name="Interval Trail Riding",
    sets=1,
    reps="30-45 minutes",
    weight="Bodyweight",
    description="Alternate between fast and slow riding intervals on trails for 30-45 minutes."
)

    technical_trail_ride = Exercise(
    workout_id=12,
    name="Technical Trail Ride",
    sets=1,
    reps="30-45 minutes",
    weight="Bodyweight",
    description="Ride on technical trails for 30-45 minutes."
)

    trail_cycling = Exercise(
    workout_id=12,
    name="Trail Cycling",
    sets=1,
    reps="30 minutes",
    weight="Bodyweight",
    description="Cycle on trails for 30 minutes."
)

    interval_trail_riding_2 = Exercise(
    workout_id=12,
    name="Interval Trail Riding",
    sets=1,
    reps="30 minutes",
    weight="Bodyweight",
    description="Alternate between fast and slow riding intervals on trails for 30 minutes."
)

    technical_trail_navigation = Exercise(
    workout_id=12,
    name="Technical Trail Navigation",
    sets=1,
    reps="30 minutes",
    weight="Bodyweight",
    description="Navigate technical trails for 30 minutes."
)

    hill_climbing_on_trails = Exercise(
    workout_id=12,
    name="Hill Climbing on Trails",
    sets=1,
    reps="30 minutes",
    weight="Bodyweight",
    description="Climb hills on trails for 30 minutes."
)


#**stretches**#

    # Daily Routine Stretch Exercises
    forward_tilt = Exercise(
    workout_id=26,
    name="Forward Tilt",
    sets=1,
    reps="10-15 seconds",
    weight="Bodyweight",
    description="Tilt your head forward, bringing your chin to your chest. Hold for 10-15 seconds."
)

    backward_tilt = Exercise(
    workout_id=26,
    name="Backward Tilt",
    sets=1,
    reps="10-15 seconds",
    weight="Bodyweight",
    description="Tilt your head backward, looking up towards the ceiling. Hold for 10-15 seconds."
)

    side_tilt = Exercise(
    workout_id=26,
    name="Side Tilt",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Tilt your head to the side, bringing your ear towards your shoulder. Hold for 10-15 seconds on each side."
)

    side_rotation = Exercise(
    workout_id=26,
    name="Side Rotation",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Rotate your head to the side, looking over your shoulder. Hold for 10-15 seconds on each side."
)

    neck_extension = Exercise(
    workout_id=26,
    name="Neck Extension",
    sets=1,
    reps="10-15 seconds",
    weight="Bodyweight",
    description="Extend your neck, pushing your head back gently. Hold for 10-15 seconds."
)

    chin_tucks = Exercise(
    workout_id=26,
    name="Chin Tucks",
    sets=1,
    reps="10-15 seconds",
    weight="Bodyweight",
    description="Tuck your chin in towards your neck, creating a double chin. Hold for 10-15 seconds."
)

    standing_bicep_stretch = Exercise(
    workout_id=26,
    name="Standing Bicep Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Extend your arm out to the side and turn your palm up, then gently pull your fingers back to stretch your bicep. Hold for 10-15 seconds on each side."
)

    wall_bicep_stretch = Exercise(
    workout_id=26,
    name="Wall Bicep Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Place your hand on a wall with your arm extended and gently turn your body away to stretch your bicep. Hold for 10-15 seconds on each side."
)

    doorway_bicep_stretch = Exercise(
    workout_id=26,
    name="Doorway Bicep Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Place your arm against the doorway and step forward to stretch your bicep. Hold for 10-15 seconds on each side."
)

    seated_bicep_stretch = Exercise(
    workout_id=26,
    name="Seated Bicep Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Sit down, place your hands behind you on the floor, and gently slide your body forward to stretch your biceps. Hold for 10-15 seconds on each side."
)

    overhead_bicep_stretch = Exercise(
    workout_id=26,
    name="Overhead Bicep Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Reach one arm overhead and gently pull on the elbow with the opposite hand to stretch your bicep. Hold for 10-15 seconds on each side."
)

    cat_cow_stretch = Exercise(
    workout_id=26,
    name="Cat-Cow Stretch",
    sets=1,
    reps="10-15 repetitions",
    weight="Bodyweight",
    description="Start on your hands and knees, arch your back up towards the ceiling (cat), then drop your belly down and lift your head and tailbone up (cow)."
)

    cobra_stretch = Exercise(
    workout_id=26,
    name="Cobra Stretch",
    sets=1,
    reps="10-15 seconds",
    weight="Bodyweight",
    description="Lie face down, place your hands under your shoulders, and press up, lifting your chest off the ground. Hold for 10-15 seconds."
)

    childs_pose = Exercise(
    workout_id=26,
    name="Child's Pose",
    sets=1,
    reps="10-15 seconds",
    weight="Bodyweight",
    description="Sit back on your heels, extend your arms forward, and lower your forehead to the ground. Hold for 10-15 seconds."
)

    seated_forward_bend = Exercise(
    workout_id=26,
    name="Seated Forward Bend",
    sets=1,
    reps="10-15 seconds",
    weight="Bodyweight",
    description="Sit with your legs extended and reach forward towards your toes. Hold for 10-15 seconds."
)

    standing_side_stretch = Exercise(
    workout_id=26,
    name="Standing Side Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Stand with your feet together, reach one arm overhead, and lean to the opposite side. Hold for 10-15 seconds on each side."
)

    cross_body_shoulder_stretch = Exercise(
    workout_id=26,
    name="Cross-Body Shoulder Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Bring one arm across your body and use the opposite hand to pull it towards your chest. Hold for 10-15 seconds on each side."
)

    overhead_tricep_stretch = Exercise(
    workout_id=26,
    name="Overhead Tricep Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Reach one arm overhead and bend your elbow, then use the opposite hand to gently pull on the elbow to stretch your tricep. Hold for 10-15 seconds on each side."
)

    shoulder_blade_squeeze = Exercise(
    workout_id=26,
    name="Shoulder Blade Squeeze",
    sets=1,
    reps="10-15 repetitions",
    weight="Bodyweight",
    description="Squeeze your shoulder blades together and hold for a few seconds, then release. Repeat for 10-15 repetitions."
)

    thread_the_needle = Exercise(
    workout_id=26,
    name="Thread the Needle",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Start on your hands and knees, thread one arm under the other, and lower your shoulder to the ground. Hold for 10-15 seconds on each side."
)

    doorway_stretch = Exercise(
    workout_id=26,
    name="Doorway Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Place your arm against the doorway and step forward to stretch your chest. Hold for 10-15 seconds on each side."
)

    knee_to_chest_stretch = Exercise(
    workout_id=26,
    name="Knee-to-Chest Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Lie on your back, pull one knee towards your chest, and hold for 10-15 seconds. Repeat on the other side."
)

    quadriceps_stretch = Exercise(
    workout_id=26,
    name="Quadriceps Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Stand on one leg, pull your opposite foot towards your buttocks, and hold for 10-15 seconds. Repeat on the other side."
)

    hamstring_stretch = Exercise(
    workout_id=26,
    name="Hamstring Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Sit with one leg extended and the other bent, reach towards your toes of the extended leg, and hold for 10-15 seconds. Repeat on the other side."
)

    standing_hamstring_stretch = Exercise(
    workout_id=26,
    name="Standing Hamstring Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Stand with one foot elevated on a surface, reach towards your toes, and hold for 10-15 seconds. Repeat on the other side."
)

    butterfly_stretch = Exercise(
    workout_id=26,
    name="Butterfly Stretch",
    sets=1,
    reps="10-15 seconds",
    weight="Bodyweight",
    description="Sit with the soles of your feet together and gently press your knees towards the ground. Hold for 10-15 seconds."
)

    side_lunge_stretch = Exercise(
    workout_id=26,
    name="Side Lunge Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Step out to the side into a lunge position, keeping your other leg straight, and hold for 10-15 seconds. Repeat on the other side."
)

    seated_glute_stretch = Exercise(
    workout_id=26,
    name="Seated Glute Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Sit with one leg crossed over the other, and gently pull the top knee towards your chest to stretch your glute. Hold for 10-15 seconds. Repeat on the other side."
)

    lying_glute_stretch = Exercise(
    workout_id=26,
    name="Lying Glute Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Lie on your back, cross one ankle over the opposite knee, and gently pull the bottom leg towards your chest to stretch your glute. Hold for 10-15 seconds. Repeat on the other side."
)

    standing_figure_four_stretch = Exercise(
    workout_id=26,
    name="Standing Figure-Four Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Stand on one leg, cross the opposite ankle over your knee, and sit back into a squat position to stretch your glute. Hold for 10-15 seconds. Repeat on the other side."
)

    standing_calf_stretch = Exercise(
    workout_id=26,
    name="Standing Calf Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Stand with one foot forward and the other foot back, pressing your heel into the ground to stretch your calf. Hold for 10-15 seconds. Repeat on the other side."
)

    seated_calf_stretch = Exercise(
    workout_id=26,
    name="Seated Calf Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Sit with one leg extended and the other bent, use a towel to pull your toes towards you to stretch your calf. Hold for 10-15 seconds. Repeat on the other side."
)

    dynamic_hamstring_stretch = Exercise(
    workout_id=26,
    name="Dynamic Hamstring Stretch",
    sets=1,
    reps="10-15 repetitions each side",
    weight="Bodyweight",
    description="Stand and swing one leg forward and backward in a controlled motion to stretch your hamstring. Repeat for 10-15 repetitions on each side."
)

    hamstring_stretch_on_a_chair = Exercise(
    workout_id=26,
    name="Hamstring Stretch on a Chair",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Place one foot on a chair, reach towards your toes to stretch your hamstring, and hold for 10-15 seconds. Repeat on the other side."
)

    hamstring_stretch_with_foam_roller = Exercise(
    workout_id=26,
    name="Hamstring Stretch with Foam Roller",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Sit on the floor with a foam roller under your hamstring, gently roll back and forth to stretch the muscle. Hold for 10-15 seconds. Repeat on the other side."
)

# Athletic Routine Stretch Exercises
    levator_scapulae_stretch = Exercise(
    workout_id=27,
    name="Levator Scapulae Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Tilt your head to one side and gently pull on the opposite shoulder to stretch the levator scapulae. Hold for 10-15 seconds on each side."
)

    upper_trapezius_stretch = Exercise(
    workout_id=27,
    name="Upper Trapezius Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Tilt your head to one side and gently pull on the opposite shoulder to stretch the upper trapezius. Hold for 10-15 seconds on each side."
)

    scalene_stretch = Exercise(
    workout_id=27,
    name="Scalene Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Tilt your head to one side and gently pull on the opposite shoulder to stretch the scalene muscles. Hold for 10-15 seconds on each side."
)

    isometric_neck_exercises_front = Exercise(
    workout_id=27,
    name="Isometric Neck Exercises (Front of Neck)",
    sets=1,
    reps="10-15 seconds",
    weight="Bodyweight",
    description="Press your forehead into your hand, resisting the motion to strengthen the front of your neck. Hold for 10-15 seconds."
)

    isometric_neck_exercises_back = Exercise(
    workout_id=27,
    name="Isometric Neck Exercises (Back of Neck)",
    sets=1,
    reps="10-15 seconds",
    weight="Bodyweight",
    description="Press the back of your head into your hand, resisting the motion to strengthen the back of your neck. Hold for 10-15 seconds."
)

    isometric_neck_exercises_sides = Exercise(
    workout_id=27,
    name="Isometric Neck Exercises (Sides of Neck)",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Press the side of your head into your hand, resisting the motion to strengthen the sides of your neck. Hold for 10-15 seconds on each side."
)

    cross_body_arm_stretch = Exercise(
    workout_id=27,
    name="Cross-Body Arm Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Bring one arm across your body and use the opposite hand to pull it towards your chest. Hold for 10-15 seconds on each side."
)

    towel_bicep_stretch = Exercise(
    workout_id=27,
    name="Towel Bicep Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Hold a towel behind your back with one hand over your shoulder and the other behind your back, gently pull on the towel to stretch your bicep. Hold for 10-15 seconds on each side."
)

    spinal_twist = Exercise(
    workout_id=27,
    name="Spinal Twist",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Sit with one leg extended and the other bent, twist your torso towards the bent leg and hold for 10-15 seconds. Repeat on the other side."
)

    bridge_pose = Exercise(
    workout_id=27,
    name="Bridge Pose",
    sets=1,
    reps="10-15 seconds",
    weight="Bodyweight",
    description="Lie on your back with your knees bent, lift your hips towards the ceiling, and hold for 10-15 seconds."
)

    pigeon_pose = Exercise(
    workout_id=27,
    name="Pigeon Pose",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="From a plank position, bring one knee towards your hand and extend the opposite leg back, lowering your hips to the ground. Hold for 10-15 seconds. Repeat on the other side."
)

    kneeling_side_stretch = Exercise(
    workout_id=27,
    name="Kneeling Side Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Kneel on one knee, reach your arm overhead, and lean to the opposite side. Hold for 10-15 seconds. Repeat on the other side."
)

    extended_triangle_pose = Exercise(
    workout_id=27,
    name="Extended Triangle Pose",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Stand with your feet wide apart, extend your arms to the sides, and reach towards your front foot while keeping your torso long. Hold for 10-15 seconds. Repeat on the other side."
)

    eagle_arms = Exercise(
    workout_id=27,
    name="Eagle Arms (Garudasana)",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Wrap your arms around each other, bringing your palms together, and lift your elbows to stretch your shoulders. Hold for 10-15 seconds. Repeat on the other side."
)

    childs_pose_with_shoulder_stretch = Exercise(
    workout_id=27,
    name="Child's Pose with Shoulder Stretch",
    sets=1,
    reps="10-15 seconds",
    weight="Bodyweight",
    description="Sit back on your heels, extend your arms forward, and lower your forehead to the ground. Then walk your hands to one side to stretch your shoulders. Hold for 10-15 seconds."
)

    cow_face_pose_arms = Exercise(
    workout_id=27,
    name="Cow-Face Pose (Gomukhasana) Arms",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Reach one arm overhead and the other behind your back, trying to clasp your hands together. Hold for 10-15 seconds. Repeat on the other side."
)

    shoulder_circles = Exercise(
    workout_id=27,
    name="Shoulder Circles",
    sets=1,
    reps="10-15 repetitions",
    weight="Bodyweight",
    description="Stand with your arms at your sides, make circles with your shoulders, moving them forward and backward for 10-15 repetitions."
)

    lat_stretch_at_a_wall = Exercise(
    workout_id=27,
    name="Lat Stretch at a Wall",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Stand facing a wall, place your hands on the wall, and lean forward to stretch your lats. Hold for 10-15 seconds. Repeat on the other side."
)

    cobra_stretch_ii = Exercise(
    workout_id=27,
    name="Cobra Stretch (II)",
    sets=1,
    reps="10-15 seconds",
    weight="Bodyweight",
    description="Lie face down, place your hands under your shoulders, and press up into a cobra stretch. Hold for 10-15 seconds."
)

    seated_forward_hinge = Exercise(
    workout_id=27,
    name="Seated Forward Hinge",
    sets=1,
    reps="10-15 seconds",
    weight="Bodyweight",
    description="Sit with your legs extended in front of you, hinge at your hips, and reach towards your toes. Hold for 10-15 seconds."
)

    sphinx_pose = Exercise(
    workout_id=27,
    name="Sphinx Pose",
    sets=1,
    reps="10-15 seconds",
    weight="Bodyweight",
    description="Lie face down, prop yourself up on your elbows, and lift your chest. Hold for 10-15 seconds."
)

    spinal_twist_ii = Exercise(
    workout_id=27,
    name="Spinal Twist (II)",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Lie on your back, bring one knee across your body, and twist your torso to the opposite side. Hold for 10-15 seconds. Repeat on the other side."
)

    lying_quad_stretch = Exercise(
    workout_id=27,
    name="Lying Quad Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Lie on your side, grab your top ankle, and gently pull it towards your glutes to stretch your quad. Hold for 10-15 seconds. Repeat on the other side."
)

    hip_flexor_stretch = Exercise(
    workout_id=27,
    name="Hip Flexor Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Kneel on one knee, tilt your pelvis forward, and gently press your hips down to stretch your hip flexors. Hold for 10-15 seconds. Repeat on the other side."
)

    pigeon_pose_ii = Exercise(
    workout_id=27,
    name="Pigeon Pose (II)",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="From a plank position, bring one knee towards your hand and extend the opposite leg back, lowering your hips to the ground. Hold for 10-15 seconds. Repeat on the other side."
)

    seated_thigh_stretch = Exercise(
    workout_id=27,
    name="Seated Thigh Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Sit on the floor with one leg bent behind you, lean back to stretch your thigh. Hold for 10-15 seconds. Repeat on the other side."
)

    supine_glute_stretch = Exercise(
    workout_id=27,
    name="Supine Glute Stretch",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Lie on your back, cross one ankle over the opposite knee, and gently pull the bottom leg towards your chest to stretch your glute. Hold for 10-15 seconds. Repeat on the other side."
)

    seated_glute_stretch_ii = Exercise(
    workout_id=27,
    name="Seated Glute Stretch (II)",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Sit with one leg crossed over the other, and gently pull the top knee towards your chest to stretch your glute. Hold for 10-15 seconds. Repeat on the other side."
)

    pigeon_pose_iii = Exercise(
    workout_id=27,
    name="Pigeon Pose (III)",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="From a plank position, bring one knee towards your hand and extend the opposite leg back, lowering your hips to the ground. Hold for 10-15 seconds. Repeat on the other side."
)

    downward_dog_stretch = Exercise(
    workout_id=27,
    name="Downward Dog Stretch",
    sets=1,
    reps="10-15 seconds",
    weight="Bodyweight",
    description="Start in a plank position, lift your hips towards the ceiling to form an inverted V-shape, and hold for 10-15 seconds."
)

    calf_stretch_on_a_step = Exercise(
    workout_id=27,
    name="Calf Stretch on a Step",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Stand on a step with your heels hanging off, lower your heels to stretch your calves. Hold for 10-15 seconds. Repeat on the other side."
)

    wall_calf_stretch_with_bent_knee = Exercise(
    workout_id=27,
    name="Wall Calf Stretch with Bent Knee",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Stand facing a wall, place your hands on the wall, and bend one knee to stretch your calf. Hold for 10-15 seconds. Repeat on the other side."
)

    standing_forward_bend_with_bent_knee = Exercise(
    workout_id=27,
    name="Standing Forward Bend with Bent Knee",
    sets=1,
    reps="10-15 seconds each side",
    weight="Bodyweight",
    description="Stand with your feet hip-width apart, bend forward at your hips, and bend your knees slightly to stretch your hamstrings. Hold for 10-15 seconds. Repeat on the other side."
)






    exercises = [
    bench_press,
    incline_dumbbell_press,
    chest_flyes,
    tricep_dips,
    tricep_pushdowns,
    deadlift,
    bent_over_rows,
    pull_ups,
    barbell_curls,
    hammer_curls,
    squats,
    leg_press,
    lunges,
    leg_curls,
    calf_raises,
    overhead_press,
    lateral_raises,
    front_raises,
    russian_twists,
    plank,
    dumbbell_pullover,
    chest_press_machine,
    single_arm_dumbbell_row,
    t_bar_row,
    decline_push_ups,
    bulgarian_split_squats,
    leg_extensions,
    seated_calf_raises,
    arnold_press,
    shrugs,
    clean_and_press,
    goblet_squats,
    kettlebell_swings,
    renegade_rows,
    medicine_ball_slam,
    cat_cow_pose,
    downward_facing_dog,
    childs_pose,
    cobra_pose,
    warrior_i_pose,
    sun_salutation_a,
    warrior_ii_pose,
    triangle_pose,
    extended_side_angle_pose,
    boat_pose_intermediate,
    crow_pose,
    headstand,
    forearm_stand,
    king_pigeon_pose,
    wheel_pose,
    half_moon_pose,
    tree_pose,
    dancers_pose,
    standing_forward_bend,
    pigeon_pose,
    plank_pose,
    side_plank_pose,
    boat_pose,
    crow_pose,
    dolphin_plank_pose,
    legs_up_the_wall_pose,
    reclining_bound_angle_pose,
    supine_twist,
    corpse_pose,
    happy_baby_pose,
    jumping_jacks,
    burpees,
    mountain_climbers,
    high_knees,
    plank,
    squats,
    lunges,
    glute_bridges,
    step_ups,
    calf_raises,
    push_ups,
    dumbbell_rows,
    shoulder_press,
    bicep_curls,
    tricep_dips,
    bicycle_crunches,
    russian_twists,
    plank_with_shoulder_taps,
    leg_raises,
    side_plank,
    jump_rope,
    running,
    cycling,
    rowing,
    burpees_cardio,
    dumbbell_chest_press,
    dumbbell_flyes,
    lat_pulldowns,
    dumbbell_shoulder_raises,
    tricep_kickbacks,
    goblet_squats,
    bulgarian_split_squats,
    deadlifts,
    lateral_lunges,
    hamstring_curls,
    v_ups,
    hanging_leg_raises,
    side_plank_hip_lifts,
    reverse_crunches,
    ab_wheel_rollouts,
    burpees,
    jump_squats,
    mountain_climbers,
    high_knees,
    plank_jacks,
    burpees ,
    jumping_jacks , 
    mountain_climbers ,
    rest_hiit_circuit_1 ,
    jump_squats ,
    high_knees ,
    lunges , 
    rest_hiit_circuit_2 , 
    running_or_jogging ,
    cycling,
    rowing , 
    elliptical_machine,
    sprints ,
    rest_tabata_1,
    jumping_squats ,
    rest_tabata_2 ,
    jumping_rope ,
    high_knees_cardio_circuits ,
    jumping_jacks_cardio_circuits ,
    rest_cardio_circuits , 
    running_in_place ,
    butt_kicks ,
    mountain_climbers_cardio_circuits ,
    basic_jump_rope , 
    interval_jump_rope , 
    alternate_foot_jumping ,
    double_unders , 
    side_to_side_jumps , 
    hill_hike, 
    trail_hike ,
    uphill_hiking,
    downhill_hiking ,
    steep_inclines ,
    trail_exploration ,
    stair_climb , 
    stair_intervals ,
    basic_stair_climbing ,
    step_ups ,
    high_knees_on_stairs ,
    fast_steps ,
    burpees ,
    high_knees ,
    jumping_jacks,
    mountain_climbers ,
    rest ,
    jump_squats ,
    skaters, 
    jump_lunges , 
    rest_30s ,
    steady_state_elliptical ,
    elliptical_intervals ,
    forward_elliptical_stride , 
    backward_elliptical_stride ,
    high_resistance_intervals , 
    low_resistance_endurance,
    incline_adjustments ,
    steady_state_recumbent_bike ,
    recumbent_bike_intervals ,
    steady_cycling ,
    high_resistance_intervals_recumbent ,
    low_resistance_endurance_recumbent ,
    hill_climb_simulation ,
    trail_ride, 
    interval_trail_riding,
    technical_trail_ride,
    trail_cycling ,
    interval_trail_riding_2 ,
    technical_trail_navigation ,
    hill_climbing_on_trails,
    forward_tilt , 
    backward_tilt ,
    side_tilt , 
    side_rotation , 
    neck_extension,
    chin_tucks , 
    standing_bicep_stretch , 
    wall_bicep_stretch , 
    doorway_bicep_stretch ,
    seated_bicep_stretch , 
    overhead_bicep_stretch , 
    cat_cow_stretch , 
    cobra_stretch , 
    childs_pose , 
    seated_forward_bend ,  
    standing_side_stretch,
    cross_body_shoulder_stretch , 
    overhead_tricep_stretch , 
    shoulder_blade_squeeze , 
    thread_the_needle , 
    doorway_stretch , 
    knee_to_chest_stretch,  
    quadriceps_stretch , 
    hamstring_stretch, 
    standing_hamstring_stretch , 
    butterfly_stretch, 
    side_lunge_stretch , 
    seated_glute_stretch , 
    lying_glute_stretch , 
    standing_figure_four_stretch , 
    standing_calf_stretch ,  
    seated_calf_stretch , 
    dynamic_hamstring_stretch , 
    hamstring_stretch_on_a_chair ,
    hamstring_stretch_with_foam_roller ,
    levator_scapulae_stretch ,
    upper_trapezius_stretch ,
    scalene_stretch ,
    isometric_neck_exercises_front ,  
    isometric_neck_exercises_back , 
    isometric_neck_exercises_sides , 
    cross_body_arm_stretch ,
    towel_bicep_stretch , 
    spinal_twist , 
    bridge_pose , 
    pigeon_pose , 
    kneeling_side_stretch , 
    extended_triangle_pose , 
    eagle_arms , 
    childs_pose_with_shoulder_stretch , 
    cow_face_pose_arms , 
    shoulder_circles ,  
    lat_stretch_at_a_wall , 
    cobra_stretch_ii , 
    seated_forward_hinge , 
    sphinx_pose , 
    spinal_twist_ii , 
    lying_quad_stretch , 
    hip_flexor_stretch,
    pigeon_pose_ii ,
    seated_thigh_stretch ,
    supine_glute_stretch , 
    seated_glute_stretch_ii , 
    pigeon_pose_iii , 
    downward_dog_stretch ,
    calf_stretch_on_a_step,
    wall_calf_stretch_with_bent_knee ,
    standing_forward_bend_with_bent_knee
]




    for exercise in exercises:
        db.session.add(exercise)
        db.session.commit()
    print('Success!!')

    

