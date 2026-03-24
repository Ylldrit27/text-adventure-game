# game.py

def start():
    while True:
        print("\nYou wake up in a dark room.")
        print("There are two doors.")
        print("1. Left door")
        print("2. Right door")

        choice = input("Choose (1 or 2): ")

        if choice == "1":
            left_room()
            break
        elif choice == "2":
            right_room()
            break
        else:
            print("Invalid choice. Try again.")


def left_room():
    while True:
        print("\nYou enter a room with a sleeping dragon.")
        print("1. Sneak past it")
        print("2. Attack it")

        choice = input("Choose (1 or 2): ")

        if choice == "1":
            print("\nYou quietly sneak past and escape. You win!")
            break
        elif choice == "2":
            print("\nThe dragon wakes up and burns you. Game over.")
            break
        else:
            print("Invalid choice. Try again.")


def right_room():
    while True:
        print("\nYou find a treasure chest.")
        print("1. Open it")
        print("2. Leave it")

        choice = input("Choose (1 or 2): ")

        if choice == "1":
            print("\nIt's a trap! Game over.")
            break
        elif choice == "2":
            print("\nYou walk away safely. You survive!")
            break
        else:
            print("Invalid choice. Try again.")


# Start the game
start()