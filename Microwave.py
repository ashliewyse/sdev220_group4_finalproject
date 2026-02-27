"""
Jackson Duchow
SDEV220
Project: Group 4 Final Project – Microwave Simulation
Purpose: Microwave Core Functionality
Description: Implements the core functionality of the microwave system,
"""

class Microwave:

    def __init__(self):
        #cooking variables
        self.power_state = False
        self.state = "Idle"
        self.cook_time = 0

    #Power on/off methods
    def power_on(self):
        self.power_on = True
        self.state = "Idle"
        self.cook_time = 0

    def power_off(self):
        self.power_on = False
        self.state = "Idle"
        self.cook_time = 0

    #timer setting method, returns a string depending on succes or failure
    def set_cook_time(self, time):
        if self.power_state != True:
            return "Microwave is powered off."
        if time <= 0:
            return "⚠ Time must be greater than zero."
        if self.state == "Cooking":
            return "⚠ Cannot set time while cooking."
        self.cook_time = time
        return "Cook time set to {self.cook_time} seconds."
    
    #start cooking method, returns a string depending on succes or failure
    def start(self):    
        if self.power_state != True:
            return "⚠ Cannot start. Microwave is powered off."
        if self.cook_time <= 0:
            return "⚠ Set cook time before starting."
        if self.state == "Paused":
            return "⚠ Cannot start while paused. Use resume."
        self.state = "Cooking"
        return "🔔 Cooking started."
    
    #pause cooking method, returns a string depending on succes or failure
    def pause(self):    
        if self.state == "Cooking":
            self.state = "Paused"
            return "⏸ Cooking paused."
        return "⚠ Cannot pause unless cooking."
    
    #resume cooking method, returns a string depending on succes or failure
    def resume(self):    
        if self.state == "Paused":
            self.state = "Cooking"
            return "▶ Cooking resumed."
        return "⚠ Cannot resume unless paused."   
    
    #stop cooking method, returns a string depending on succes or failure
    def stop(self):   
        if self.state in ["Cooking", "Paused"]:
            self.state = "Idle"
            self.cook_time = 0
            return "⏹ Cooking stopped."
        return "⚠ Cannot stop unless cooking or paused."
    
