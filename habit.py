import data

def create_habit():
    user_id = int(input("User ID: "))
    name = input("Habit name: ")
    frequency = input("Frequency (daily/weekly): ")
    goal = input("Goal: ")

    habit = {
        "habit_id": data.habit_id_counter,
        "user_id": user_id,
        "habit_name": name,
        "frequency": frequency,
        "goal": goal
    }

    data.habits.append(habit)

    print("Habit created:", habit)

    data.habit_id_counter += 1


def view_habits():
    print("\nHabits:")
    for h in data.habits:
        print(h)