import math


#
# """Площади фигур"""
#
#
# def triangle(a, b):
#     result = a * b * 0.5
#     return result
#
#
# def rectangle(a, b):
#     s = a * b
#     return s
#
#
# def circle(r):
#     r = r ** 2
#     s = r * math.pi
#     return s
#
#
# print("Площадь круга: ", round(circle(5), 2))
# print("Площадь треугольника: ", triangle(6, 7))
# print("Площадь прямоугольника: ", rectangle(4, 8))

# """Список простых и не простых чисел"""
#
# lst = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 14]
#
#
# def get_count(n):
#     maximal_count = []
#     minimal_count = []
#
#     for i in range(2, max(n)):
#         for j in n:
#             if j % i == 0:
#                 maximal_count.append(j)
#             else:
#                 minimal_count.append(j)
#         return min(minimal_count), max(maximal_count)
# #
# #
# minimal, maximal = get_count(lst)
# print("Максимальное не простое число: ", maximal)
# print("Минимальное простое число: ", minimal)
# #
# """Сумма четных и нечетных цифр"""
#
# lst = int(input("Введите число: "))
#
#
# def calculate_sum(xxx):
#     lst = [int(i) for i in str(xxx)]
#     even = []
#     not_even = []
#     for cnt in lst:
#         if cnt % 2 == 0:
#             even.append(cnt)
#         else:
#             not_even.append(cnt)
#
#     return sum(even), sum(not_even)
#
#
# even, not_even = calculate_sum(lst)
# print("Сумма четных чисел:", even)
# print("Сумма нечетных чисел:", not_even)
