import random

# Dictionary of random key-value pairs
my_dict = {
    "apple": 3,
    "banana": 6,
    "orange": 4,
    "grape": 8
}

# Get random key-value pairs from the dictionary
random_pairs = random.sample(list(my_dict.items()), k=len(my_dict))

# Print the random key-value pairs
for key, value in random_pairs:
    print(f"{key}: {value}")