import random
import string
def get_random_password(n):
    c = string.ascii_letters
    z = string.digits
    pas = random.sample(c + z, n)
    pas = ''.join(pas)
    return pas
n = 8
print(get_random_password(n))
