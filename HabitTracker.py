from user import register_user, view_users
from habit import create_habit, view_habits

while True:

    print("\n==== HABIT TRACKER ====")
    print("1 Register User")
    print("2 Create Habit")
    print("3 View Users")
    print("4 View Habits")
    print("5 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        register_user()

    elif choice == 2:
        create_habit()

    elif choice == 3:
        view_users()

    elif choice == 4:
        view_habits()
        
    elif choice == 5:
        break