import time
import threading
import pygame
from random import randint

from Pet.cat import Cat
from Pet.dog import Dog
from Pet.rabbit import Rabbit
from Pet.turtle import Turtle

# from Food.cat_food import Cat_Food
# from Food.dog_food import Dog_Food
# from Food.rabbit_food import Rabbit_Food
# from Food.turtle_food import Turtle_Food
# from Food.mixed_fruit import Mix

# Initialize Pygame
# pygame.init()

# # Set up display
# width, height = 800, 600
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Pet Game")

# play_image = pygame.image.load('APP/Pet/catspritesx4.gif')
# feed_image = pygame.image.load('feed.png')
# water_image = pygame.image.load('water.png')
# status_image = pygame.image.load('status.png')

class Pet:
    def __init__(self, name, species, sex):
        self.species = species
        
        #Name setting        
        self.name = name
            
        #Sex setting
        self.sex = sex
        self.sex_noun = "he" if "male" in sex else "she"
        self.sex_pronoun = "him" if "male" in sex else "her"

        # Health settings
        self.health = 100
        self.max_health = 100
        
        # Hunger settings
        self.hunger = 0
        self.max_hunger = 100
        
        # Thirsty settings
        self.thirsty = 0
        self.max_thirsty = 100
        
        # Mood settings
        self.mood = 100
        self.min_mood = 0
        
        #Age setting
        self.min_age = 0

        self.need_food = False
        self.need_water = False
        
    def set_mood(self):
        if 0 <= self.mood <= 30:
            return "bored"
        elif 30 < self.mood <= 50:
            return "normal"
        elif 50 < self.mood <= 80:
            return "happy"
        return "VERY EXCITED!!!"
    
    def play(self):
        mood_status = self.set_mood()
        
        if self.mood <= 30:
            self.hunger += 30
            self.thirsty += 30
            self.mood += 20
            print(f"{self.name} is {mood_status}. You must spend more time with {self.sex_pronoun}.")
        elif self.mood <= 50:
            self.hunger += 20
            self.thirsty += 20
            self.mood += 15
            print(f"{self.name} is {mood_status}.")       
        elif self.mood <= 80:
            self.hunger += 10
            self.thirsty += 10
            self.mood += 10
            print(f"{self.name} is {mood_status}.")
        else:  # Very excited
            self.hunger += 10
            self.thirsty += 10
            print(f"{self.name} is {mood_status}. You are having a great life with your bestie!!!")
        
        # Ensure mood does not exceed maximum
        self.mood = max(self.mood, 100)
    
    def feed(self):
        if self.hunger > 0:
            self.health += 10 
            self.hunger -= 10
            self.mood += 20
            print(f"{self.name} has been fed.")
        else:
            print(f"{self.name} is already full.")

        # Ensure health and mood do not exceed maximum
        self.health = min(self.health, self.max_health)
        self.mood = min(self.mood, 100)
            
    def give_water(self):
        if self.thirsty > 0:
            self.thirsty -= 10
            print(f"{self.name} has been given water.")
        else:
            print(f"{self.name} is not thirsty.")
         
        # Ensure health does not exceed maximum
        self.health = min(self.health, self.max_health)
    
    def pass_time(self):
        # Increase hunger and thirst over time
        if self.hunger < self.max_hunger:
            self.hunger += randint(5, 15)
        if self.thirsty < self.max_thirsty:
            self.thirsty += randint(5, 15)
        
        # Decrease mood over time
        if self.mood > self.min_mood:
            self.mood -= randint(5, 10)
        
        # Check needs
        self.need_food = self.hunger >= self.max_hunger
        self.need_water = self.thirsty >= self.max_thirsty
            
        # Reduce health if needs are not met
        if self.hunger >= self.max_hunger or self.thirsty >= self.max_thirsty or self.mood <= self.min_mood:
            self.health -= 10
        if self.health < 0:
            self.health = 0
            print(f"\n\n!!! WARNING !!!")
            print(f"{self.name} is in critical condition!!! Bring food and water to {self.sex_pronoun} immediately!!!")

    def check_status(self):
        mood_status = self.set_mood()
        print(f"{self.name} - The {self.species} ({self.sex}):\n                    Health: {self.health}\n                    Hunger: {self.hunger}\n                    Thirsty: {self.thirsty}\n                    Mood: {mood_status}")

       
class Game:
    def __init__(self):
        self.pet = None
        self.is_running = True
        self.invalid_name = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

        
    def start_game(self):
        while True:
            name = input("Pet's name: ")
            #Check invalid characters in name
            if any(char in self.invalid_name for char in name):
                print(f"\nNames should not include special characters! Try another name.")
            else:
                break
            
        while True:
            species = input("Species: ").lower()
            #Check if species is empty
            if len(species) == 0:
                print(f"\nInvalid input! Try again.")
            else:
                break
        
        while True:
            sex = input("Sex (male/female): ").lower()
            if sex in ["male", "female"]:
                break
            else: 
                print(f"Invalid input! Try again.\n")
            
        # Create pet
        self.pet = Pet(name, species, sex)
        
        # Background 
        threading.Thread(target=self.background_task, daemon=True).start()
        self.run()
        
    def background_task(self):
        while self.is_running:
            time.sleep(15)   # test 
            self.pet.pass_time()
        
    def display_menu(self):
        print("\nChoose your action: ")
        print("Feed / Refill Water / Play / Check Status / Exit")
    
    def run(self):
        while self.is_running:
            # Check if pet needs food or water
            if self.pet.need_food:
                print(f"\n\nAttention")
                print(f"{self.pet.name} is hungry! Please feed {self.pet.sex_pronoun} some food!")
                feed = input(f"Feed {self.pet.name} (Yes/No)?: ").lower()
                if "yes" in feed:
                    self.pet.feed()
                elif "no" in feed:
                    print(f"Ok, I will wait next time...")
                else:
                    print(f"Invalid input! Try again.")
                self.pet.need_food = False  
                
            if self.pet.need_water:
                print(f"\n\nAttention")
                print(f"{self.pet.name} is thirsty! Please give {self.pet.sex_pronoun} some water!")
                water = input(f"Give {self.pet.name} water (Yes/No)?: ").lower()
                if "yes" in water:
                    self.pet.give_water()
                elif "no" in water:
                    print(f"Ok, I will wait next time...")
                else:
                    print(f"Invalid input! Try again.")
                self.pet.need_water = False  

            self.display_menu()
             
            #Selection (type word)  
            choice = input("I want to ")
            if "feed" in choice:
                self.pet.feed()
            elif "water" in choice:
                self.pet.give_water()
            elif "play" in choice:
                self.pet.play()
            elif "check" in choice:
                self.pet.check_status()
            elif "exit" in choice:
                self.is_running = False
            else:
                print("Invalid choice! Choose again.")
            
            #Selection (type keyword)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.pet.feed()
                    elif event.type == pygame.K_w:
                        self.pet.give_water()
                    elif event.type == pygame.K_p:
                        self.pet.play()
                    elif event.type == pygame.K_c:
                        self.pet.check_status()
                
            #Incoming feature (replace Selection)
            #Main menu
                #Feed menu
                #Play menu
                #Check menu
            

if __name__ == "__main__":
    game = Game()
    game.start_game()
