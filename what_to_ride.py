# Base form for what_to_ride_next program
import random

welcome_prompt = "Welcome to Kings Island! Ready to have the best day?!"
# print(welcome_prompt)

# Collects all user data at once
class UserProfile:
    def __init__(self):
        self.group_size = int(input("How many people are visiting today? "))
        self.fast_lane = input("Do you have fast lane? ")
        self.with_child = input("Are you traveling with children? ")

    def profile(self):
        print(f"Your group today is: {self.group_size}")
        print(f"Has FL? {self.fast_lane}")
        print(f"Traveling with child? {self.with_child}")
        
user = UserProfile()

# Categoric list of all rides(sans Soak City currently)
all_coasters = ['Adventure Express', 'Backlot Stunt Coaster', 'Banshee', 'The Bat', 'The Beast', 'Diamondback', 'Flight of Fear', 'Flying Ace Aerial Chase', 'Great Pumpkin Coaster', 'Invertigo', 'Mystic Timbers', 'Orion', 'The Racer', 'Woodstock Express']

all_thrill_flats = ['Delirium', 'Drop Tower', 'Windseeker']

all_family_flats = ['Boo Blasters', 'Congo Falls', 'Dodgem', 'Eiffel Tower', 'Grand Carousel', 'K.I. & Miami Valley Railroad', 'Kings Mills Antique Autos', 'Monster', 'Race for Your Life Charlie Brown', 'Scrambler', 'Shake, Rattle, & Roll', 'Viking Fury', 'White Water Canyon', 'Zephyr']

all_rides = all_coasters + all_thrill_flats + all_family_flats

# Lists of rides with specialties
all_fast_lane = ["Adventure Express", "Backlot Stunt Coaster", "Banshee", "Boo Blasters", "Delirium", "Diamondback", "Dodgem", "Drop Tower", "Eiffel Tower", "Flight of Fear", "Flying Ace Aerial Chase", "Invertigo", "Kings Mills Antique Autos", "Monster", "Mystic Timbers", "Orion", "Race for Your Life Charlie Brown", "Rendezvous Run", "Scrambler", "Shake, Rattle, & Roll", "Surf Dog", "The Beast", "The Racer", "Thunder Falls", "Tropical Plunge", "Windseeker", "Woodstock Gliders", "Zephyr", "Zoom Flume"]

all_kids_flats = ['Character Carousel', 'Charlie Browns Wind Up', 'Joe Cools Dodgem School', 'Kite Eating Tree', 'Linus Beetle Bugs', 'Linus Launcher', 'Peanuts 500', 'Peanuts Off-Road Rally', 'Snoopy vs. Red Baron', 'Snoopys Junction', 'Snoopys Space Buggies', 'Woodstock Gliders', 'Woodstock Whirlybirds']

def choice():
    print("Here are some options to begin your day: ")
    for option in range(length):
        all_options = random.choice(all_rides)
        print(all_options)

length = int(input("How many choices would you like? "))
choice()

# Fast Lane
if user.fast_lane.lower() == "yes":
    has_fast_lane = True
else:
    has_fast_lane = False

# Children?
if user.with_child.lower() == "yes":
    # TODO: Height profile with available rides
    all_rides += all_kids_flats
    choice()
else:
    all_rides.remove("Great Pumpkin Coaster")