import random
import math

actions = [
    "Print a random number",
    "Generate a random float",
    "Select a random element from a list",
    "Shuffle a list randomly",
    "Perform a random mathematical operation"
]

# Select a random action
random_action = random.choice(actions)

# Perform the random action
if random_action == actions[0]:
    # Print a random number
    random_number = random.randint(1, 100)
    print("Random number:", random_number)
elif random_action == actions[1]:
    # Generate a random float
    random_float = random.uniform(1.0, 10.0)
    print("Random float:", random_float)
elif random_action == actions[2]:
    # Select a random element from a list
    random_element = random.choice(["apple", "banana", "orange", "grape"])
    print("Random element:", random_element)
elif random_action == actions[3]:
    # Shuffle a list randomly
    my_list = [1, 2, 3, 4, 5]
    random.shuffle(my_list)
    print("Shuffled list:", my_list)
elif random_action == actions[4]:
    # Perform a random mathematical operation
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    operation = random.choice(["+", "-", "*", "/"])
    
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        result = a / b
    
    print(f"Performing {a} {operation} {b} = {result}")
else:
    print("Unknown action:", random_action)