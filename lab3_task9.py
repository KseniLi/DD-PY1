salary = 5000  # зарплата
spend = 6000  # траты
month = 10  # количество месяцев
increase = 0.03  # рост цен

x = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(month):
    x = x - spend + salary
    spend = spend + spend * increase


x = -x
print(round(x))
