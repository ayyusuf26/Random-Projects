import random

def game():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

value = game()
print(value)