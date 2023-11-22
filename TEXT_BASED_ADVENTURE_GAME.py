import time

class Player:
    def __init__(self):
        self.inventory = []
        self.location = "Start"

    def move(self, new_location):
        self.location = new_location

    def add_to_inventory(self, item):
        self.inventory.append(item)

# Function to handle player choices
def get_user_choice(options):
    print("\nChoose an option:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                return choice - 1
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to simulate delays in the story
def delay_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

# Main game function
def play_game():
    player = Player()

    delay_print("Welcome to the Text Adventure Game!")
    delay_print("Your adventure begins...")

    while True:
        if player.location == "Start":
            options = ["Enter the forest", "Visit the castle", "Quit"]
            choice = get_user_choice(options)

            if choice == 0:
                player.move("Forest")
                delay_print("You enter the mysterious forest.")
            elif choice == 1:
                player.move("Castle")
                delay_print("You approach the ancient castle.")
            else:
                delay_print("Thanks for playing! Goodbye.")
                break

        elif player.location == "Forest":
            options = ["Search for items", "Return to the starting point"]
            choice = get_user_choice(options)

            if choice == 0:
                player.add_to_inventory("Sword")
                delay_print("You find a sword in the dense vegetation.")
            elif choice == 1:
                player.move("Start")

        elif player.location == "Castle":
            options = ["Explore the castle", "Enter the dungeon", "Return to the starting point"]
            choice = get_user_choice(options)

            if choice == 0:
                delay_print("You discover a secret room with a treasure chest.")
                player.add_to_inventory("Treasure")
            elif choice == 1:
                delay_print("You venture into the dark dungeon.")
                player.move("Dungeon")
            elif choice == 2:
                player.move("Start")

        elif player.location == "Dungeon":
            options = ["Open the chest", "Go back to the castle"]
            choice = get_user_choice(options)

            if choice == 0:
                if "Treasure" in player.inventory:
                    delay_print("Congratulations! You found the treasure and completed the adventure.")
                else:
                    delay_print("The chest is empty. Nothing of interest here.")
            elif choice == 1:
                player.move("Castle")

# Run the game
play_game()
