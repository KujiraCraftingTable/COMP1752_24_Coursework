class Turtle:
    def __init__(self, name, sex):        
        #Name setting        
        self.name = name
        
        #Species setting
        self.species = "turtle"
            
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