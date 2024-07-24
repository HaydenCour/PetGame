import threading
import time 

#Define a class named Tamagotchi
class PetGame:
    # Constructor method to initialize a new Tamagotchi instance
    def __init__(self):
        self.hunger = 50  # Set initial hunger level
        self.happiness = 50  # Set initial happiness level
        self.alive = True # Set initial status to alive when created

    # Method to feed the Tamagotchi
    def feed(self):
        if self.hunger > 0:
            self.hunger -= 10  # Decrease hunger level
            print("Yum!")  # Print message indicating the Pet has been fed
        else:
            print("I'm full!")  # Print message if Pet is not hungry

    # Method to play with the Pet
    def play(self):
        if self.happiness < 100:
            self.happiness += 10  # Increase happiness level
            print("That was fun!")  # Print message indicating the Tamagotchi enjoyed playing
        else:
            print("I'm too tired to play.")  # Print message if Tamagotchi is too happy to play

    # Method to check the status of the Pet
    def display_status(self):
        print(f"Hunger Level: {self.hunger}/100")
        print(f"Happiness Level: {self.happiness}/100")

    def degrade_levels(self):
        while self.alive:  
            time.sleep(10)  # Wait for 10 seconds before decreasing levels
            self.hunger += 5  # Increase hunger level by 5
            self.happiness -= 5  # Decrease happiness level by 5
            if self.hunger >= 100 or self.happiness <= 0:
                print("Your Pet has passed away...")
                self.alive = False  # Update the alive status to False

# Create an instance of the Tamagotchi class
my_pet = PetGame()

def start_degradation():
    degradation_thread = threading.Thread(target=my_pet.degrade_levels)
    degradation_thread.start()

start_degradation()

# Main loop to interact with the PetGame
while my_pet.alive:  # Corrected to use the correct attribute
    # Print the main menu options
    print("Welcome to PetGame!")  # Updated text for consistency
    print("What would you like to do?")
    print("1. Feed PetGame")  # Updated text for consistency
    print("2. Play with PetGame")  # Updated text for consistency
    print("3. Check the Status of PetGame")  # Updated text for consistency

    # Get user input
    user_choice = input()

    # Decide action based on user input
    if user_choice == "1":
        my_pet.feed()  # Corrected method call
    elif user_choice == "2":
        my_pet.play()  # Corrected method call
    elif user_choice ==  "3":
        my_pet.display_status()  # Corrected method call
    elif user_choice == "4":
        break  # Exit the loop and end the program1
    else:
        # Print an error message if the input is not valid
        print("Invalid choice, please choose 1, 2, 3, or 4.")