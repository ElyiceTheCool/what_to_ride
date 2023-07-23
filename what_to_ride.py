# Base form for what_to_ride_next program
import random

welcome_prompt = "Welcome to Kings Island! Ready to have the best day?!"

# Categoric list of all rides(sans Soak City currently)
all_coasters = ['Adventure Express', 'Backlot Stunt Coaster', 'Banshee', 'The Bat', 'The Beast', 'Diamondback', 'Flight of Fear', 'Flying Ace Aerial Chase', 'Great Pumpkin Coaster', 'Invertigo', 'Mystic Timbers', 'Orion', 'The Racer', 'Woodstock Express']

all_thrill_flats = ['Delirium', 'Drop Tower', 'Windseeker']

all_family_flats = ['Boo Blasters', 'Congo Falls', 'Dodgem', 'Eiffel Tower', 'Grand Carousel', 'K.I. & Miami Valley Railroad', 'Kings Mills Antique Autos', 'Monster', 'Race for Your Life Charlie Brown', 'Scrambler', 'Shake, Rattle, & Roll', 'Viking Fury', 'White Water Canyon', 'Zephyr']

all_kids_flats = ['Character Carousel', 'Charlie Browns Wind Up', 'Joe Cools Dodgem School', 'Kite Eating Tree', 'Linus Beetle Bugs', 'Linus Launcher', 'Peanuts 500', 'Peanuts Off-Road Rally', 'Snoopy vs. Red Baron', 'Snoopys Junction', 'Snoopys Space Buggies', 'Woodstock Gliders', 'Woodstock Whirlybirds']

all_rides = all_coasters + all_thrill_flats + all_family_flats

# Lists of rides with specialties
all_fast_lane = ["Adventure Express", "Backlot Stunt Coaster", "Banshee", "Boo Blasters", "Delirium", "Diamondback", "Dodgem", "Drop Tower", "Eiffel Tower", "Flight of Fear", "Flying Ace Aerial Chase", "Invertigo", "Kings Mills Antique Autos", "Monster", "Mystic Timbers", "Orion", "Race for Your Life Charlie Brown", "Rendezvous Run", "Scrambler", "Shake, Rattle, & Roll", "Surf Dog", "The Beast", "The Racer", "Thunder Falls", "Tropical Plunge", "Windseeker", "Woodstock Gliders", "Zephyr", "Zoom Flume"]

def choice():
    print("Here are some options to begin your day: ")
    for option in range(length):
        all_options = random.choice(all_rides)
        print(all_options)

length = int(input("How many choices would you like? "))
choice()

# Fast Lane
user_fast_lane = input("Do you have Fast Lane today? (yes/no) ").lower()
if user_fast_lane == "yes":
    has_fast_lane = True
else:
    has_fast_lane = False

if has_fast_lane == True:
    print("Cool! Here are some options for Fast Lane rides!")
    for option in range(length):
        print(random.choice(all_fast_lane))

# Children?
user_child_status = input("Are you visiting with any children today (yes/no)? ").lower()
if user_child_status == "yes":
    # TODO: Height profile with available rides
    all_rides += all_kids_flats
    print(all_rides)
else:
    all_rides.remove("Great Pumpkin Coaster")
    print(all_rides)