import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for i in range(length))
    return random_string
for i in range(1000):
    random_string = generate_random_string(16)
    print(random_string)

