import time
import random

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50
        self.freckles = 10000
        self.forehead = "Huge"

    def feed(self):
        self.hunger -= 10
        if self.hunger < 0:
            self.hunger = 0
        print("{} has been fed.".format(self.name))

    def play(self):
        self.happiness += 10
        self.energy -= 5
        if self.happiness > 100:
            self.happiness = 100
        if self.energy < 0:
            self.energy = 0
        print("{} is happy after playing.".format(self.name))

    def sleep(self):
        self.energy += 20
        self.hunger += 10
        if self.energy > 100:
            self.energy = 100
        if self.hunger > 100:
            self.hunger = 100
        print("{} has slept and feels refreshed.".format(self.name))
        
    def kiss(self):
    	self.freckles += 20
    	print("{} has gotten even more frecklier.".format(self.name))

    def check_status(self):
        print("Status of {}: \nHunger: {}\nHappiness: {}\nEnergy: {}\nFreckles: {}\nForehead: {}".format(self.name, self.hunger, self.happiness, self.energy, self.freckles, self.forehead))

def main():
    pet_name = input("Enter your pet's name: ")
    pet = VirtualPet(pet_name)
    while True:
        print("\nWhat would you like to do with {}?".format(pet.name))
        print("1. Feed\n2. Play\n3. Sleep\n4. Check Status\n5. Kiss\n6. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.sleep()
        elif choice == '4':
            pet.check_status()
        elif choice == '5':
        	pet.kiss()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        # Simulate the passage of time
        time.sleep(random.randint(1, 3))

if __name__ == "__main__":
    main()