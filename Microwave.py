"""
Jackson Duchow
SDEV220
Project: Group 4 Final Project - Microwave Simulation
Purpose: Microwave Core Functionality
Description: Implements the core functionality of the microwave system,
"""

#class to pass errors
class InvalidError(Exception):
    pass

#core microwave class
class Microwave:

    def __init__(self):
        #cooking variables
        self.powerState = False
        self.state = "Idle"
        #states its set to use are "Idle", "Cooking", "Paused"
        self.cookTime = 0

    #power button: turns the micowave on or off
    def powerButton(self):
        #on
        if self.powerState == False:
            self.powerState = True
            self.state = "Idle"
            self.cookTime = 0
        #off
        else:
            self.powerState = False
            self.state = "Idle"
            self.cookTime = 0

    #checks if power is on and throws exception if not
    def checkOn(self): #bok-bok
        if self.powerState == False:
            raise InvalidError("Microwave is currently off. Please turn it on")

    #sets the cooking time, throws exceptions when wrong state or bad input
    def set_cook_time(self, sec):
        self.checkOn()
        if sec <= 0:
            raise InvalidError("Please input a time (in seconds) greater than 0")
        if self.state == "Cooking" or self.state == "Paused":
            raise InvalidError("Cannot set time while cooking or paused")
        self.cookTime = sec
        return "Cook time set to: ", self.cookTime, " seconds"
    
    #start cooking method, throws exceptions when in wrong state or time isn't set
    def start(self):    
        self.checkOn()
        if self.cookTime <= 0:
            raise InvalidError("Set cook time before starting")
        if self.state == "Paused":
            raise InvalidError("Cannot start while paused. Use resume")
        self.state = "Cooking"
        return "Cooking started"
    
    #pause cooking method
    def pause(self):    
        self.checkOn()
        if self.state == "Cooking":
            self.state = "Paused"
            return "Cooking paused"
        raise InvalidError("Cannot pause unless cooking")
    
    #resume cooking method
    def resume(self):  
        self.checkOn()  
        if self.state == "Paused":
            self.state = "Cooking"
            return "Cooking is resumed"
        raise InvalidError("Cannot resume unless paused")   
    
    #stop cooking method
    def stop(self):   
        self.checkOn()
        if self.state == "Cooking" or self.state == "Paused":
            self.state = "Idle"
            self.cookTime = 0
            return "Cooking has been Stopped"
        raise InvalidError("Cannot stop unless cooking or paused")
    
    def second(self):
        self.checkOn()
        if self.state == "Cooking":
            if self.cookTime > 0:
                self.cookTime -= 1
                if self.cookTime == 0:
                    self.state = "Idle"

    #getters

    def getCookTime(self):
        return self.cookTime
    
    def getPower(self):
        return self.powerState
    
    def getState(self):
        return self.state
        
    def getStatus(self):
        return [self.powerState, self.state, self.cookTime]
