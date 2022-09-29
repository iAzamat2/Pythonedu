import math

'''
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
in     -> out
6782   -> 23
0,67   -> 13
198,45 -> 27
'''


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def protectinput():
    num_ = input('Введите вещественное число: ')
    while not is_number(num_):
        num_ = input('Введите вещественное число: ')

    return num_


def task1():
    number = abs(float(protectinput()))
    print(number)


'''
2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
1 - 1*1, 2 - 1*2, 3 - 1*2*3, 4 - 1*2*3*4
4 -> [1, 2, 6, 24]
6 -> [1, 2, 6, 24, 120, 720]
'''


def task2():
    print()


'''
3. Задайте список из n чисел последовательности, заполненный по формуле: (1+1/n)**n и выведите на экран их сумму.
Для n = 6: [2, 2, 2, 2, 2, 3] -> 13
'''


def task3():
    print()


'''
4*. Напишите программу, которая принимает на вход 2 числа. Задайте список из N элементов, 
заполненых числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях(не индексах).
Position one: 1
Position two: 3
Number of elements: 5
[-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5] -> 15
'''


def task4():
    print()


'''
5**. Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.
10 
-> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
-> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]
'''


def task5():
    print()


task1()
# task2()
# task3()
# task4()
# task5()