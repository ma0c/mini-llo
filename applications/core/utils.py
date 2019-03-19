import random
import string


def generate_random_slug(n: int):
    """
    Generate a string of n random characters
    :param n: integer
    :return: str of len n with random characters
    """
    return random.choices(string.ascii_lowercase, k=n)
