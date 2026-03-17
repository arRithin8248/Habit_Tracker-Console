import data

def track_progress():

    habit_id = int(input("Habit ID: "))
    date = input("Date: ")
    status = input("Completed (yes/no): ")

    entry = {
        "habit_id": habit_id,
        "date": date,
        "status": status
    }

    data.progress.append(entry)

    print("Progress Recorded")