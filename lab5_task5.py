import random
import string
def get_random_password(n):
    letters = string.ascii_letters
    digits = string.digits
    pas = random.sample(letters + digits, n)
    pas = ''.join(pas)
    return pas
n = 8
print(get_random_password(n))
