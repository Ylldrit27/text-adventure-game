print("Welcome to the Adventure Game!")

print("\nYou are in a dark room.")
print("1. Go left")
print("2. Go right")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    print("\nYou find a treasure chest! You win!")
elif choice == "2":
    print("\nYou fall into a pit. Game over.")
else:
    print("\nInvalid choice. Game over.")