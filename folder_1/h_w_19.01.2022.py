"""Конвертер температуры"""


class Convert:
    count = 0

    def __init__(self):
        Convert.count + 1

    @staticmethod
    def from_c_to_f(x):
        result = (x * 9 / 5) + 32
        Convert.count += 1
        return result

    @staticmethod
    def from_f_to_c(x):
        result = (x - 32) * 5 / 9
        Convert.count += 1
        return result


print("Конвертация в Фаренгейт: ", round(Convert.from_c_to_f(25), 1))
print("Конвертация в Цельсий: ", round(Convert.from_f_to_c(25), 1))
print("Количество подсчетов температуры: ", Convert.count)
