def get_count_char(str_):
    str_ = str_.lower()
    list_ = str_.split()
    list_.sort()
    st = "".join(list_)
    result = {}
    for i in st:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

def get_percent(res):
    percent = res
    for i in percent:
        percent[i] = round(percent[i] * 100 / len(percent), 2)
    return percent


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
res = get_count_char(main_str)
print(res)
print(get_percent(res))