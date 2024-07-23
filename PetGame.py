
class Tamagotchi:
    def __init__(self):
        self.hunger = 50
        self.happiness = 50

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 10
            print("Yum!")
        else:
            print("I'm full!")

    def play(self):
        if self.happiness < 100:
            self.happiness += 10
            print("That was fun!")
        else:
            print("I'm too tired to play.")


my_tamagotchi = Tamagotchi()

while True:
    print("Welcome to Tamagotchi!")
    print("What would you like to do?")
    print("1.Feed Tamagotchi")
    print("2.Play with Tamagotchi")
    print("3.Exit")

    user_choice = input()

    if user_choice == "1":
        my_tamagotchi.feed()
    elif user_choice == "2":
        my_tamagotchi.play()
    elif user_choice == "3":
        break
    else:
        print("Invalid choice, please choose 1, 2, or 3.")