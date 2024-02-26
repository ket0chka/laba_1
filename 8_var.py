# 1 Создать список заполнив его значениями от 45 до 7 с шагом 3. Вывести результат

my_list = list(range(45,7,-3))
print ('Список', my_list)

# 2 На основе списка создать множество значений от 0 до 10, использовать при этом цикл break. Вывести результат

my_set = set() # создаем пустое множество
for i in my_list[::-1]: # все элементы списка в обратном порядке
    if i < 11: # задаем условие
        my_set.add(i) 
    else:
        break
print('Множество',my_set)

# 3 Создать список и добавить в него значения словаря. Вывести результат. Отсортировать список. Вывести результат.

my_dict = {'a': 1, 'b': 2, 'c': 3} 
my_new_list = list(my_dict.values())
print('Новый список',my_new_list)
my_new_list.sort()
print('Отсортированный список',my_new_list)

# 4 Среди двух произвольных списков найти есть ли хотя бы один общий элемент.\

first_list = [1,12,15,16,17,19,123]
print ('Первый список', first_list)
second_list = [15, 13,33,14,19]
print ('Второй список', second_list)
itog_list = []
for i in first_list : #задаем условие для нового листа
    if i in second_list :
        itog_list.append(i)
print ('Общие элементы', itog_list)

# 5 Написать функцию, на вход которой подается два списка в одном значение длины, а другом ширины. Найти площади этих прямоугольников
# и записать в множество. Найти медиану площадей и удалить все значения из списка меньше неё. Из полученных значений найти сумму и
# поделить её на длину входного списка и вывести ответ. Итоговый ответ вернуть и вывести на экран. При выполнении задания использовать 
# функцию filter()

dlina = [4,15,17,19]
shir = [2,3,14,15]
def calculate_plosh(input_dlina, input_shir):
    plosh = {length * width for length, width in zip(input_dlina, input_shir)} # Записываем площади прямоугольников в множество
    median = sorted(plosh)[len(plosh)//2]
    filtered_areas = filter(lambda x: x >= median, plosh)
    sum_filtered_areas = sum(filtered_areas)
    result = sum_filtered_areas / len(input_dlina) # Делим сумму на длину входного списка
    return result
final_answer = calculate_plosh(dlina, shir)
print("Итоговый ответ:", final_answer)

# 6 Написать функцию, на вход которой подается словарь, содержащий ключ в виде целого числа и значение в виде строки. Найти значение 
# с максимальным и минимальным ключом. Найти среднее значение между полученными числами и удалить все пары ключ-значение значение 
# которых меньше полученного числа. Итоговый словарь вернуть и вывести на экран. При выполнении задания использовать функцию filter().

my_dict = {1: 'one', 3: 'three', 11: 'eleven', 20: 'twenty'}
def dictionary(input_dict):
    max_value = max(input_dict.keys())
    min_value = min(input_dict.keys())
    middle = (max_value + min_value) / 2
    filtered_dict = dict(filter(lambda x: int(x[0]) >= middle, input_dict.items()))
    print(filtered_dict)
    return filtered_dict
final_dict = dictionary(my_dict)


# 7 Написать функцию перевода секунд в дни, часы и минуты. На вход подается число секунд от начала точки отсчета, на выходе дата в формате
# d/h/m/s

def convert_seconds(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600 # остаток от деления
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    result = "{:d}d {:02d}h {:02d}m {:02d}s".format(days, hours, minutes, seconds)
    return result
total_seconds = 123456789
time_string = convert_seconds(total_seconds)
print('Результат',time_string)