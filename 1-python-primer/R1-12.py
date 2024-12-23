import random

def custom_choice(data):
    if len(data) == 0:
        raise ValueError("Data cannot be empty")
    random_index = random.randrange(0, len(data))
    return data[random_index]

data = [10, 20, 30, 40, 50]
print(custom_choice(data))