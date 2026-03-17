import data

def add_journal():

    user_id = int(input("User ID: "))
    note = input("Write your reflection: ")

    journal = {
        "user_id": user_id,
        "note": note
    }

    data.journals.append(journal)

    print("Journal Entry Saved")