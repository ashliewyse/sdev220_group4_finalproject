# Name: Ashlie Wyse
# Course: SDEV 220
# Project: Group 4 Final Project – Microwave Simulation
# Purpose: Command-Line Interface (CLI) for Microwave System
# Description: Handles user interaction, input validation,
#              menu display, and safety alerts.

import logging
from Microwave import Microwave, InvalidError
from timer import Timer

# Set up logging to record usage history
logging.basicConfig(
    filename="microwave_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

class MicrowaveCLI:
    
    def __init__(self):
        self.Microwave = Microwave()
        self.timer = None
        #slightly easier to type
        self.M = self.Microwave
        #dictionary of menu functions
        self.menu = {
            "1": self.power,
            "2": self.set_time,
            "3": self.start_cooking,
            "4": self.pause,
            "5": self.resume,
            "6": self.stop,
            "7": self.status,
            "8": self.view_log,
            "9": self.exit
        }


    def display_menu(self):
        print("\n--- Smart Microwave Menu ---")
        print("1. Power On/Off")
        print("2. Set Cook Time")
        print("3. Start Cooking")
        print("4. Pause")
        print("5. Resume")
        print("6. Stop")
        print("7. Status")
        print("8. View Usage History")
        print("9. Exit")

    def power(self):
        self.M.powerButton()
        if self.M.getPower():
            print("Microwave powered on.")
            logging.info("Microwave powered on")
        else:
            print("Microwave powered off.")
            logging.info("Microwave powered off")

    def set_time(self):
        try:
            time_input = int(input("Enter cooking time in seconds: "))
            time = self.Microwave.set_cook_time(time_input)
            print(time)
            logging.info(time)
        except ValueError:
            print("⚠ Invalid input. Please enter a number.")
        except InvalidError as e:
            print(e)

    def start_cooking(self):
        try: 
            start = self.Microwave.start()
            print(start)
            logging.info(start)
            self.timer = Timer(self.Microwave)
            self.timer.start()
         
           
            if self.Microwave.getState() != "Paused":
                self.signal_done()
        except InvalidError as e:
            print(e)

    def pause(self):
        try:
            pause = self.Microwave.pause()
            print(pause)
            logging.info(pause)
        except InvalidError as e:
            print(e)

    def resume(self):
        try:
            resume = self.Microwave.resume()
            print(resume)
            logging.info(resume)
            self.timer = Timer(self.Microwave)
            self.timer.start()
        except InvalidError as e:
            print(e)

    def stop(self):
        try:
            stop = self.Microwave.stop()
            print(stop)
            logging.info(stop)
            if self.timer:
                self.timer.stop()
        except InvalidError as e:
            print(e)

    def status(self):
        power, state, time = self.Microwave.getStatus()
        print(f"\nPower: {'On' if power else 'Off'}")
        print(f"State: {state}")
        print(f"Cook Time: {time} seconds")

def view_log(self):
        print("\n--- Usage History ---")
        try:
            with open("microwave_log.txt", "r") as f:
                log_contents = f.read()
                print(log_contents)
        except FileNotFoundError:
            print("No usage history yet.")

    def signal_done(self):
        """Simulates the 'Done' signal when cooking finishes."""
        print("\n" + "="*30)
        print("   DING! COOKING COMPLETE!")
        print("="*30)
        input("Press Enter to clear...")

    def exit(self):
        print("Exiting system.")
        logging.info("Exited microwave system")
        exit()

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option: ")
            if choice in self.menu:
                self.menu[choice]()
            else:
                print("⚠ Invalid selection.")

if __name__ == "__main__":
    microwave = MicrowaveCLI()
    microwave.run()
