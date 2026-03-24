# game.py

# ====== Player Inventory ======
inventory = []

# ====== Inventory Functions ======
def show_inventory():
    if inventory:
        print("\nYour inventory:", ", ".join(inventory))
    else:
        print("\nYour inventory is empty.")

def add_to_inventory(item):
    inventory.append(item)
    print(f"\n{item} added to your inventory!")

# ====== Game Rooms ======
def start():
    while True:
        print("\nYou wake up in a dark room.")
        print("There are two doors.")
        print("1. Left door")
        print("2. Right door")
        print("3. Check inventory")

        choice = input("Choose (1, 2, or 3): ")

        if choice == "1":
            left_room()
            break
        elif choice == "2":
            right_room()
            break
        elif choice == "3":
            show_inventory()
        else:
            print("Invalid choice. Try again.")

def left_room():
    while True:
        print("\nYou enter a room with a sleeping dragon.")
        print("1. Sneak past it")
        print("2. Attack it")
        print("3. Use an item from inventory")
        print("4. Check inventory")

        choice = input("Choose (1, 2, 3, or 4): ")

        if choice == "1":
            print("\nYou quietly sneak past and escape. You win!")
            break
        elif choice == "2":
            print("\nThe dragon wakes up and burns you. Game over.")
            break
        elif choice == "3":
            if "Golden Key" in inventory:
                print("\nYou use the Golden Key to distract the dragon and escape! You win!")
                break
            else:
                print("\nYou have nothing useful to use here.")
        elif choice == "4":
            show_inventory()
        else:
            print("Invalid choice. Try again.")

def right_room():
    while True:
        print("\nYou find a treasure chest.")
        print("1. Open it")
        print("2. Leave it")
        print("3. Check inventory")

        choice = input("Choose (1, 2, or 3): ")

        if choice == "1":
            add_to_inventory("Golden Key")
            break
        elif choice == "2":
            print("\nYou leave the chest and walk away safely.")
            break
        elif choice == "3":
            show_inventory()
        else:
            print("Invalid choice. Try again.")

# ====== Start Game ======
start()