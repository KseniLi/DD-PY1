import random
import string
def get_random_password():
    c = string.ascii_letters
    z = string.digits
    pas = random.sample(c + z, 8)
    pas = ''.join(pas)
    return pas
print(get_random_password())
