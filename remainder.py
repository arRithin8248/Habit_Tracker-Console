import data

def add_reminder():

    habit_id = int(input("Habit ID: "))
    time = input("Reminder time: ")

    reminder = {
        "habit_id": habit_id,
        "time": time
    }

    data.reminders.append(reminder)

    print("Reminder Added")