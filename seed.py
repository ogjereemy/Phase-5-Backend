from models import *
from config import *
from app import app
from sqlalchemy import text
from datetime import datetime,date


 

    # # Create Exercises for the plan
    # exercise1 = Exercise(name="Running", duration=30, type="Cardio", workout_plan=cardio_plan)
    # exercise2 = Exercise(name="Cycling", duration=45, type="Cardio", workout_plan=cardio_plan)
    # db.session.add(exercise1)
    # db.session.add(exercise2)
    # db.session.commit() 


    


    


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
    meal_type=MealType.BREAKFAST, 
    calory_intake=300, 
    protein=10, 
    fat=5, 
    carbs=50, 
    notes="Oatmeal with berries"
)
    nutrition_log2 = NutritionLog(
    user_id=1, 
    date=date(2024, 8, 1), 
    meal_type=MealType.LUNCH, 
    calory_intake=600, 
    protein=35, 
    fat=30, 
    carbs=20, 
    notes="Chicken Caesar Salad"
)
    nutrition_log3 = NutritionLog(
    user_id=1, 
    date=date(2024, 8, 1), 
    meal_type=MealType.DINNER, 
    calory_intake=700, 
    protein=45, 
    fat=15, 
    carbs=70, 
    notes="Grilled chicken with quinoa"
)
    nutrition_log4 = NutritionLog(
    user_id=1, 
    date=date(2024, 8, 1), 
    meal_type=MealType.SNACK, 
    calory_intake=200, 
    protein=10, 
    fat=4, 
    carbs=30, 
    notes="Greek yogurt with honey"
)

    nutrition_log5 = NutritionLog(
    user_id=2, 
    date=date(2024, 8, 1), 
    meal_type=MealType.BREAKFAST, 
    calory_intake=400, 
    protein=15, 
    fat=20, 
    carbs=35, 
    notes="Avocado toast with egg"
)
    nutrition_log6 = NutritionLog(
    user_id=2, 
    date=date(2024, 8, 1), 
    meal_type=MealType.LUNCH, 
    calory_intake=500, 
    protein=30, 
    fat=20, 
    carbs=40, 
    notes="Turkey sandwich with spinach"
)
    nutrition_log7 = NutritionLog(
    user_id=2, 
    date=date(2024, 8, 1), 
    meal_type=MealType.DINNER, 
    calory_intake=800, 
    protein=40, 
    fat=25, 
    carbs=95, 
    notes="Spaghetti with meatballs"
)
    nutrition_log8 = NutritionLog(
    user_id=2, 
    date=date(2024, 8, 1), 
    meal_type=MealType.SNACK, 
    calory_intake=250, 
    protein=25, 
    fat=5, 
    carbs=20, 
    notes="Protein shake"
)

    nutrition_log9 = NutritionLog(
    user_id=3, 
    date=date(2024, 8, 1), 
    meal_type=MealType.BREAKFAST, 
    calory_intake=350, 
    protein=10, 
    fat=10, 
    carbs=50, 
    notes="Smoothie bowl"
)
    nutrition_log10 = NutritionLog(
    user_id=3, 
    date=date(2024, 8, 1), 
    meal_type=MealType.LUNCH, 
    calory_intake=450, 
    protein=15, 
    fat=15, 
    carbs=50, 
    notes="Veggie wrap with hummus"
)
    nutrition_log11 = NutritionLog(
    user_id=3, 
    date=date(2024, 8, 1), 
    meal_type=MealType.DINNER, 
    calory_intake=750, 
    protein=35, 
    fat=20, 
    carbs=80, 
    notes="Salmon with sweet potato"
)
    nutrition_log12 = NutritionLog(
    user_id=3, 
    date=date(2024, 8, 1), 
    meal_type=MealType.SNACK, 
    calory_intake=200, 
    protein=6, 
    fat=18, 
    carbs=10, 
    notes="Mixed nuts"
)

    nutrition_log13 = NutritionLog(
    user_id=4, 
    date=date(2024, 8, 1), 
    meal_type=MealType.BREAKFAST, 
    calory_intake=250, 
    protein=20, 
    fat=5, 
    carbs=10, 
    notes="Egg whites and spinach"
)
    nutrition_log14 = NutritionLog(
    user_id=4, 
    date=date(2024, 8, 1), 
    meal_type=MealType.LUNCH, 
    calory_intake=550, 
    protein=40, 
    fat=25, 
    carbs=30, 
    notes="Grilled chicken salad"
)
    nutrition_log15 = NutritionLog(
    user_id=4, 
    date=date(2024, 8, 1), 
    meal_type=MealType.DINNER, 
    calory_intake=850, 
    protein=45, 
    fat=30, 
    carbs=90, 
    notes="Beef stir-fry with broccoli"
)
    nutrition_log16 = NutritionLog(
    user_id=4, 
    date=date(2024, 8, 1), 
    meal_type=MealType.SNACK, 
    calory_intake=180, 
    protein=15, 
    fat=5, 
    carbs=25, 
    notes="Cottage cheese with fruit"
)

    nutrition_log17 = NutritionLog(
    user_id=5, 
    date=date(2024, 8, 1), 
    meal_type=MealType.BREAKFAST, 
    calory_intake=300, 
    protein=12, 
    fat=8, 
    carbs=40, 
    notes="Yogurt parfait"
)
    nutrition_log18 = NutritionLog(
    user_id=5, 
    date=date(2024, 8, 1), 
    meal_type=MealType.LUNCH, 
    calory_intake=600, 
    protein=25, 
    fat=20, 
    carbs=75, 
    notes="Quinoa and black bean bowl"
)
    nutrition_log19 = NutritionLog(
    user_id=5, 
    date=date(2024, 8, 1), 
    meal_type=MealType.DINNER, 
    calory_intake=800, 
    protein=35, 
    fat=30, 
    carbs=90, 
    notes="Chicken and vegetable curry"
)
    nutrition_log20 = NutritionLog(
    user_id=5, 
    date=date(2024, 8, 1), 
    meal_type=MealType.SNACK, 
    calory_intake=200, 
    protein=6, 
    fat=10, 
    carbs=25, 
    notes="Apple with peanut butter"
)

    nutrition_log21 = NutritionLog(
    user_id=6, 
    date=date(2024, 8, 1), 
    meal_type=MealType.BREAKFAST, 
    calory_intake=400, 
    protein=20, 
    fat=10, 
    carbs=50, 
    notes="Protein pancakes"
)
    nutrition_log22 = NutritionLog(
    user_id=6, 
    date=date(2024, 8, 1), 
    meal_type=MealType.LUNCH, 
    calory_intake=450, 
    protein=35, 
    fat=15, 
    carbs=20, 
    notes="Tuna salad"
)
    nutrition_log23 = NutritionLog(
    user_id=6, 
    date=date(2024, 8, 1), 
    meal_type=MealType.DINNER, 
    calory_intake=700, 
    protein=40, 
    fat=20, 
    carbs=80, 
    notes="Shrimp and rice"
)
    nutrition_log24 = NutritionLog(
    user_id=6, 
    date=date(2024, 8, 1), 
    meal_type=MealType.SNACK, 
    calory_intake=200, 
    protein=5, 
    fat=12, 
    carbs=25, 
    notes="Banana with almond butter"
)

    nutrition_log25 = NutritionLog(
    user_id=7, 
    date=date(2024, 8, 1), 
    meal_type=MealType.BREAKFAST, 
    calory_intake=350, 
    protein=20, 
    fat=5, 
    carbs=50, 
    notes="Smoothie with protein powder"
)
    nutrition_log26 = NutritionLog(
    user_id=7, 
    date=date(2024, 8, 1), 
    meal_type=MealType.LUNCH, 
    calory_intake=500, 
    protein=30, 
    fat=20, 
    carbs=45, 
    notes="Chicken wrap"
)
    nutrition_log27 = NutritionLog(
    user_id=7, 
    date=date(2024, 8, 1), 
    meal_type=MealType.DINNER, 
    calory_intake=800, 
    protein=35, 
    fat=25, 
    carbs=90, 
    notes="Beef and broccoli stir-fry"
)
    nutrition_log28 = NutritionLog(
    user_id=7, 
    date=date(2024, 8, 1), 
    meal_type=MealType.SNACK, 
    calory_intake=150, 
    protein=10, 
    fat=3, 
    carbs=25, 
    notes="Carrot sticks with hummus"
)

    nutrition_log29 = NutritionLog(
    user_id=8, 
    date=date(2024, 8, 1), 
    meal_type=MealType.BREAKFAST, 
    calory_intake=400, 
    protein=18, 
    fat=12, 
    carbs=45, 
    notes="Egg sandwich"
)
    nutrition_log30 = NutritionLog(
    user_id=8, 
    date=date(2024, 8, 1), 
    meal_type=MealType.LUNCH, 
    calory_intake=500, 
    protein=25, 
    fat=15, 
    carbs=55, 
    notes="Grilled chicken with brown rice"
)
    nutrition_log31 = NutritionLog(
    user_id=8, 
    date=date(2024, 8, 1), 
    meal_type=MealType.DINNER, 
    calory_intake=700, 
    protein=30, 
    fat=20, 
    carbs=85, 
    notes="Pasta with marinara sauce"
)
    nutrition_log32 = NutritionLog(
    user_id=8, 
    date=date(2024, 8, 1), 
    meal_type=MealType.SNACK, 
    calory_intake=180, 
    protein=8, 
    fat=4, 
    carbs=20, 
    notes="Fruit salad"
)

    nutrition_log33 = NutritionLog(
    user_id=9, 
    date=date(2024, 8, 1), 
    meal_type=MealType.BREAKFAST, 
    calory_intake=350, 
    protein=15, 
    fat=8, 
    carbs=45, 
    notes="Omelette with veggies"
)
    nutrition_log34 = NutritionLog(
    user_id=9, 
    date=date(2024, 8, 1), 
    meal_type=MealType.LUNCH, 
    calory_intake=600, 
    protein=40, 
    fat=20, 
    carbs=35, 
    notes="Chicken and quinoa bowl"
)
    nutrition_log35 = NutritionLog(
    user_id=9, 
    date=date(2024, 8, 1), 
    meal_type=MealType.DINNER, 
    calory_intake=800, 
    protein=35, 
    fat=25, 
    carbs=85, 
    notes="Steak with potatoes"
)
    nutrition_log36 = NutritionLog(
    user_id=9, 
    date=date(2024, 8, 1), 
    meal_type=MealType.SNACK, 
    calory_intake=200, 
    protein=10, 
    fat=8, 
    carbs=25, 
    notes="Cheese and crackers"
)

    nutrition_log37 = NutritionLog(
    user_id=10, 
    date=date(2024, 8, 1), 
    meal_type=MealType.BREAKFAST, 
    calory_intake=300, 
    protein=15, 
    fat=10, 
    carbs=35, 
    notes="Yogurt with granola"
)
    nutrition_log38 = NutritionLog(
    user_id=10, 
    date=date(2024, 8, 1), 
    meal_type=MealType.LUNCH, 
    calory_intake=500, 
    protein=30, 
    fat=15, 
    carbs=50, 
    notes="Chicken salad sandwich"
)
    nutrition_log39 = NutritionLog(
    user_id=10, 
    date=date(2024, 8, 1), 
    meal_type=MealType.DINNER, 
    calory_intake=700, 
    protein=40, 
    fat=20, 
    carbs=75, 
    notes="Pork chops with applesauce"
)
    nutrition_log40 = NutritionLog(
    user_id=10, 
    date=date(2024, 8, 1), 
    meal_type=MealType.SNACK, 
    calory_intake=150, 
    protein=8, 
    fat=5, 
    carbs=20, 
    notes="Trail mix"
)

    nutrition_log41 = NutritionLog(
    user_id=11, 
    date=date(2024, 8, 1), 
    meal_type=MealType.BREAKFAST, 
    calory_intake=350, 
    protein=12, 
    fat=15, 
    carbs=35, 
    notes="Bagel with cream cheese"
)
    nutrition_log42 = NutritionLog(
    user_id=11, 
    date=date(2024, 8, 1), 
    meal_type=MealType.LUNCH, 
    calory_intake=600, 
    protein=35, 
    fat=20, 
    carbs=55, 
    notes="Turkey and avocado wrap"
)
    nutrition_log43 = NutritionLog(
    user_id=11, 
    date=date(2024, 8, 1), 
    meal_type=MealType.DINNER, 
    calory_intake=850, 
    protein=40, 
    fat=25, 
    carbs=90, 
    notes="Roast chicken with vegetables"
)
    nutrition_log44 = NutritionLog(
    user_id=11, 
    date=date(2024, 8, 1), 
    meal_type=MealType.SNACK, 
    calory_intake=180, 
    protein=8, 
    fat=8, 
    carbs=20, 
    notes="Mixed fruit"
)

    nutrition_log45 = NutritionLog(
    user_id=12, 
    date=date(2024, 8, 1), 
    meal_type=MealType.BREAKFAST, 
    calory_intake=300, 
    protein=10, 
    fat=10, 
    carbs=50, 
    notes="Oatmeal with honey"
)
    nutrition_log46 = NutritionLog(
    user_id=12, 
    date=date(2024, 8, 1), 
    meal_type=MealType.LUNCH, 
    calory_intake=550, 
    protein=25, 
    fat=15, 
    carbs=60, 
    notes="Chicken and rice bowl"
)
    nutrition_log47 = NutritionLog(
    user_id=12, 
    date=date(2024, 8, 1), 
    meal_type=MealType.DINNER, 
    calory_intake=700, 
    protein=35, 
    fat=20, 
    carbs=75, 
    notes="Fish tacos"
)
    nutrition_log48 = NutritionLog(
    user_id=12, 
    date=date(2024, 8, 1), 
    meal_type=MealType.SNACK, 
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
    exercises="Cat-Cow Pose, Downward-Facing Dog, Child/'s Pose, Cobra Pose, Warrior I Pose"
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
    exercises="Half Moon Pose, Tree Pose, Dancer’s Pose, Standing Forward Bend, Pigeon Pose"
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


    

    

