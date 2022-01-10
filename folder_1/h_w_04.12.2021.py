"""Вычеслить количество отрицательных чисел в списке"""

#
# def neg_number(lst):
#     if lst == []:
#         return 0
#     else:
#         count = neg_number(lst[1:])
#         if lst[0] < 0:
#             count += 1
#         return count
#
#
# print(neg_number([-2, -3, 8, -11, -4, 6]))


# """Преобразование списков"""
#
#
# def convert_list(lst):
#     if lst == []:
#         return lst
#     if isinstance(lst[0], list):
#         return convert_list(lst[0]) + convert_list(lst[1:])
#     return lst[:1] + convert_list(lst[1:])
#
#
# print(convert_list(["Adam", ["Bob", ["Chet", "Cat"], "Bart", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]))
