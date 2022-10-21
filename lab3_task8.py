money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

x = money_capital
while x > 0:
    x = x + salary - spend
    spend = increase * spend + spend
    if round(x)<0:
        break
    else:
        month = month + 1


print(month)
