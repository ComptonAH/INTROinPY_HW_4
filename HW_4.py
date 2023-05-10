# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

list_1 = set((input('Enter the elements of the first set splitting via comma: ')).split(','))
list_2 = input('Enter the elements of the second set splitting via comma: ').split(',')

result = list(list_1.intersection(list_2))
result_2 = []
for i in result:
    int_digit = int(i)
    result_2.append(int_digit)
result = result_2.sort()
print(result)


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки

import random

blueberry_list = [bush for bush in range(1, int(input('Enter the quantity of the bushes: ')))]
blueberry_quantity = [random.randint(1, 40) for blueberry in blueberry_list]
i = int(input('Pick the bush you want to collect: ')) - 1
collected_berries = blueberry_quantity[i] +\
                    blueberry_quantity[i-1] +\
                    blueberry_quantity[i+1]
print(collected_berries)
