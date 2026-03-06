"""
Jackson Duchow (Unfortunatly Sam does not wish to contribute)
SDEV220
Project: Group 4 Final Project - Microwave Simulation
Purpose: Microwave Timer
Description: Timer function of the microwave to allow for counting time with 
                ability to keep inputting
"""
import threading
import time

class Timer(threading.Thread):
    
    def __init__(self, microwave):
        super().__init__()
        self.microwave = microwave
        self.isRunning = False
        self.daemon = True

    def run(self):
        self.isRunning = True
        while self.isRunning:
            if self.microwave.getState() == "Cooking":
                print("Time remaing: ", self.microwave.getCookTime(), " seconds")
                time.sleep(1)
                self.microwave.second()
            else:
                break
    
    def stop(self):
        self.isRunning = False
