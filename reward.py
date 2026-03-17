import data

def give_reward():

    user_id = int(input("User ID: "))
    points = int(input("Points: "))

    reward = {
        "user_id": user_id,
        "points": points
    }

    data.rewards.append(reward)

    print("Reward Given")