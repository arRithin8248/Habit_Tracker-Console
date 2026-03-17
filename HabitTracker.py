from user import register_user, view_users
from habit import create_habit, view_habits
from progress import track_progress
from remainder import add_reminder
from reward import give_reward
from journal import add_journal

while True:

    print("\n===== HABIT TRACKER =====")
    print("1 Register User")
    print("2 Create Habit")
    print("3 Track Progress")
    print("4 Add Reminder")
    print("5 Give Reward")
    print("6 Add Journal")
    print("7 View Users")
    print("8 View Habits")
    print("9 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        register_user()

    elif choice == 2:
        create_habit()

    elif choice == 3:
        track_progress()

    elif choice == 4:
        add_reminder()

    elif choice == 5:
        give_reward()

    elif choice == 6:
        add_journal()

    elif choice == 7:
        view_users()

    elif choice == 8:
        view_habits()

    elif choice == 9:
        break