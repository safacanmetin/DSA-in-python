import random

def custom_shuffle(data):
    n = len(data)
    for i in range(n):
        j = random.randint(i, n - 1)
        data[i], data[j] = data[j], data[i] 

data = [1, 2, 3, 4, 5]
custom_shuffle(data)
print(data)  