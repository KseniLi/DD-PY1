import random
def get_unique_list_numbers() -> list[int]:
    list_ = random.sample(range(-10, 10), 15)
    return list_
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
