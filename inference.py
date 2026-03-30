
from email_env import EmailEnv

env = EmailEnv(difficulty="hard")

total_score = 0
episodes = 5

for i in range(episodes):
    obs = env.reset()
    email = obs["email"]

    if email == "urgent":
        action = "reply"
    elif email == "spam":
        action = "ignore"
    elif email == "normal":
        action = "forward"
    else:
        action = "ignore"

    result = env.step(action)
    score = result["reward"]

    print(f"Email: {email}, Action: {action}, Score: {score}")
    total_score += score

print("Final Score:", total_score / episodes)
