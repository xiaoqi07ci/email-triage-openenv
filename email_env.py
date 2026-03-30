
import random

class EmailEnv:
    def __init__(self, difficulty="easy"):
        self.difficulty = difficulty
        self.state = None

    def reset(self):
        if self.difficulty == "easy":
            self.state = random.choice(["urgent", "spam"])
        elif self.difficulty == "medium":
            self.state = random.choice(["urgent", "spam", "normal"])
        else:
            self.state = random.choice(["urgent", "spam", "normal", "phishing"])

        return {"email": self.state}

    def step(self, action):
        email = self.state

        if email == "urgent" and action == "reply":
            reward = 1.0
        elif email == "spam" and action == "ignore":
            reward = 1.0
        elif email == "normal" and action == "forward":
            reward = 1.0
        elif email == "phishing" and action == "ignore":
            reward = 1.0
        else:
            reward = 0.0

        done = True
        return {"state": {"email": email}, "reward": reward, "done": done}
