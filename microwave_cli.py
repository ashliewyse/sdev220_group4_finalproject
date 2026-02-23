# Name: Ashlie Wyse
# Course: SDEV 220
# Project: Group 4 Final Project – Microwave Simulation
# Purpose: Command-Line Interface (CLI) for Microwave System
# Description: Handles user interaction, input validation,
#              menu display, and safety alerts.

class MicrowaveCLI:
    def __init__(self):
        self.power_on = False
        self.state = "Idle"
        self.cook_time = 0

    def display_menu(self):
        print("\n--- Smart Microwave Menu ---")
        print("1. Power On")
        print("2. Power Off")
        print("3. Set Cook Time")
        print("4. Start Cooking")
        print("5. Pause")
        print("6. Resume")
        print("7. Stop")
        print("8. Status")
        print("9. Exit")

    def set_time(self):
        try:
            time = int(input("Enter cooking time in seconds: "))
            if time <= 0:
                print("⚠ Time must be greater than zero.")
            else:
                self.cook_time = time
                print(f"Cook time set to {self.cook_time} seconds.")
        except ValueError:
            print("⚠ Invalid input. Please enter a number.")

    def start_cooking(self):
        if not self.power_on:
            print("⚠ Cannot start. Microwave is powered off.")
        elif self.cook_time <= 0:
            print("⚠ Set cook time before starting.")
        elif self.state == "Paused":
            print("⚠ Cannot start while paused. Use resume.")
        else:
            self.state = "Cooking"
            print("🔔 Cooking started.")
    
    def pause(self):
        if self.state == "Cooking":
            self.state = "Paused"
            print("⏸ Cooking paused.")
        else:
            print("⚠ Cannot pause unless cooking.")

    def resume(self):
        if self.state == "Paused":
            self.state = "Cooking"
            print("▶ Cooking resumed.")
        else:
            print("⚠ Cannot resume unless paused.")

    def stop(self):
        if self.state in ["Cooking", "Paused"]:
            self.state = "Stopped"
            print("⛔ Cooking stopped.")
        else:
            print("⚠ Nothing to stop.")

    def status(self):
        print(f"\nPower: {'On' if self.power_on else 'Off'}")
        print(f"State: {self.state}")
        print(f"Cook Time: {self.cook_time} seconds")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Select an option: ")

            if choice == "1":
                self.power_on = True
                print("Microwave powered on.")
            elif choice == "2":
                self.power_on = False
                print("Microwave powered off.")
            elif choice == "3":
                self.set_time()
            elif choice == "4":
                self.start_cooking()
            elif choice == "5":
                self.pause()
            elif choice == "6":
                self.resume()
            elif choice == "7":
                self.stop()
            elif choice == "8":
                self.status()
            elif choice == "9":
                print("Exiting system.")
                break
            else:
                print("⚠ Invalid selection.")


if __name__ == "__main__":
    microwave = MicrowaveCLI()
    microwave.run()