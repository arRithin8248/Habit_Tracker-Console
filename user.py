import data

def register_user():
    name = input("Enter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    user = {
        "user_id": data.user_id_counter,
        "name": name,
        "email": email,
        "password": password
    }

    data.users.append(user)
    print("User created:", user)

    data.user_id_counter += 1


def view_users():
    print("\nUsers:")
    for u in data.users:
        print(u)