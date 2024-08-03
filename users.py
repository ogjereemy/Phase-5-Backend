# from models import *
# from app import app

# with app.app_context():
    
#     # cardio_plan = WorkoutPlan(name="Cardio Plan")
#     # db.session.add(cardio_plan)

#     # # Create Exercises for the plan
#     # exercise1 = Exercise(name="Running", duration=30, type="Cardio", workout_plan=cardio_plan)
#     # exercise2 = Exercise(name="Cycling", duration=45, type="Cardio", workout_plan=cardio_plan)
#     # db.session.add(exercise1)
#     # db.session.add(exercise2)
#     # db.session.commit() 


#     # cardio=WorkoutPlan()
#     # hypertrophe=WorkoutPlan()
#     # weight_loss=WorkoutPlan()
#     # yoga=WorkoutPlan()
#     # stretches=WorkoutPlan()
#     # db.session.add(cardio)
#     # db.session.add(hypertrophe)
#     # db.session.add(weight_loss)
#     # db.session.add(yoga)
#     # db.session.add(stretches)
#     # db.session.commit()


#     # steve=Coach(username='steve',email='steve@gmail.com',_password_hash=)


# ## coaches

#     # steve = Coach(
#     # username="steve",
#     # email="steve@gmail.com",
#     # password_hash="steve_123",
#     # photo="https://images.pexels.com/photos/1092874/pexels-photo-1092874.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
#     # bio="Experienced fitness coach specializing in cardio and strength training.",
#     # specialities="Cardio, Strength Training",
#     # is_admin=True)

#     # jeremy = Coach(
#     # username="ogola",
#     # email="ogojeremy@gmail.com",
#     # password_hash="ogosh",
#     # photo="https://images.pexels.com/photos/1865131/pexels-photo-1865131.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
#     # bio="Certified personal trainer with 10 years of experience in strength and conditioning.",
#     # specialities="Strength Training, Conditioning",
#     # is_admin=True)

#     # tyra = Coach(
#     # username="tyra",
#     # email="tyra@gmail.com",
#     # password_hash="tyrant",
#     # photo="https://images.pexels.com/photos/1480520/pexels-photo-1480520.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
#     # bio="Yoga instructor and mindfulness coach with a passion for holistic health and well-being.",
#     # specialities="Yoga ,Mindfulness",
#     # is_admin=True)

#     # ace = Coach(
#     # username="ace",
#     # email="simplyace@gmail.com",
#     # password_hash="samuel",
#     # photo="https://images.pexels.com/photos/3253501/pexels-photo-3253501.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
#     # bio="Former professional athlete turned fitness coach, focusing on agility and speed training.",
#     # specialities="Agility, Speed Training",
#     # is_admin=False)

#     # mary = Coach(
#     # username="Mary",
#     # email="marynjenga@gmail.com",
#     # password_hash="mary_2885",
#     # photo="https://images.pexels.com/photos/1638324/pexels-photo-1638324.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
#     # bio="Fitness coach specializing in weight loss and nutritional guidance.",
#     # specialities="Weight Loss, Nutrition",
#     # is_admin=False)
    
#     # derrick = Coach(
#     # username="ongoma",
#     # email="derongoma@gmail.com",
#     # password_hash="odrumzz",
#     # photo="coach_photo_url",
#     # bio="Expert in HIIT and functional training, with a background in sports science.",
#     # specialities="HIIT, Functional Training",
#     # is_admin=False)
#     # db.session.add(steve)
#     # db.session.add(jeremy)
#     # db.session.add(tyra)
#     # db.session.add(ace)
#     # db.session.add(mary)
#     # db.session.add(derrick)
#     # db.session.commit()
#     # print('Coaches added')

#     ##users
#     jane = User(
#     username="jane_doe",
#     email="jane_doe@gmail.com",
#     password_hash="j@ne123",
#     photo="https://images.pexels.com/photos/864939/pexels-photo-864939.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
#     coach_id=1  
#     )

#     mike = User(
#     username="michael_smith",
#     email="michael_smith@gmail.com",
#     password_hash="mike3123",
#     photo="https://images.pexels.com/photos/791764/pexels-photo-791764.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
#     coach_id=2  
#     )

#     emily = User(
#     username="emily_jones",
#     email="emily_jones@gmail.com",
#     password_hash="j0n3s_boro",
#     photo="https://images.pexels.com/photos/1886487/pexels-photo-1886487.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
#     coach_id=3  
#     )

#     daniel = User(
#     username="daniel_wilson",
#     email="daniel_wilson@gmail.com",
#     password_hash="dannywilis",
#     photo="https://images.pexels.com/photos/1552102/pexels-photo-1552102.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
#     coach_id=4  
#     )

#     olivia = User(
#     username="olivia_martin",
#     email="olivia_martin@gmail.com",
#     password_hash="olive_garden",
#     photo="https://images.pexels.com/photos/863935/pexels-photo-863935.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
#     coach_id=5  
#     )

#     liam = User(
#     username="liam_anderson",
#     email="liam_anderson@gmail.com",
#     password_hash="YNWA",
#     photo="https://images.pexels.com/photos/2149771/pexels-photo-2149771.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
#     coach_id=1
#     )

#     ava = User(
#     username="ava_thomas",
#     email="ava_thomas@gmail.com",
#     password_hash="ava_max",
#     photo="https://images.pexels.com/photos/3757941/pexels-photo-3757941.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
#     coach_id=2
#     )

#     noah = User(
#     username="noah_taylor",
#     email="noah_taylor@gmail.com",
#     password_hash="c0ld_#3arted",
#     photo="https://images.pexels.com/photos/4720309/pexels-photo-4720309.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
#     coach_id=3
#     )

#     sophia = User(
#     username="sophia_white",
#     email="sophia_white@gmail.com",
#     password_hash="sophia_da_1st",
#     photo="https://images.pexels.com/photos/25034152/pexels-photo-25034152/free-photo-of-woman-doing-deadlifts-in-the-gym.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
#     coach_id=4
#     )

#     ben = User(
#     username="benjamin_harris",
#     email="benjamin_harris@gmail.com",
#     password_hash="blue_benji",
#     photo="https://images.pexels.com/photos/6389075/pexels-photo-6389075.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
#     coach_id=5
#     )

#     chris = User(
#     username="chris_evans",
#     email="chris_evans@gmail.com",
#     password_hash="CRISTARONALDO_SUI",
#     photo="https://images.pexels.com/photos/241456/pexels-photo-241456.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
#     coach_id=6  
#     )

#     nattie = User(
#     username="natalie_portman",
#     email="natalie_portman@gmail.com",
#     password_hash="jamal",
#     photo="https://images.pexels.com/photos/1552249/pexels-photo-1552249.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
#     coach_id=6  
#     )


#     db.session.add(jane)
#     db.session.add(mike)
#     db.session.add(emily)
#     db.session.add(daniel)
#     db.session.add(olivia)
#     db.session.add(liam)
#     db.session.add(ava)
#     db.session.add(noah)
#     db.session.add(sophia)
#     db.session.add(ben)
#     db.session.add(chris)
#     db.session.add(nattie)
#     db.session.commit()
#     print('Users added successfully.')