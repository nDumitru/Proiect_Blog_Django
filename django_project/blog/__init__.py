import random
import string

def generate_secret_key(length=50):
    """Generate a random string of characters."""
    letters_and_digits = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters_and_digits) for i in range(length))

print(generate_secret_key())
