"""Создание классов жидкость и алкоголь"""


class Liquid:
    def __init__(self, name, density):
        self.name = name
        self.density = density

    def edit_density(self, val):
        self.density = val

    def calc_val(self, m):
        v = round(m / self.density, 2)
        print(f"ОбЬем {m} кг {self.name} равен {v}")
        return v

    def calc_mass(self, v):
        m = v * self.density
        print(f"Вес {v} m^3 {self.name} составляет {m} кг")
        return m

    def print_inf(self):
        print(f"Жидкость: {self.name!r} (плотность = {self.density} kg/m^3)")


class Alcohol(Liquid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        self.strength = strength

    def edit_strength(self, val):
        self.strength = val


a = Alcohol('Wine', 1060.4, 14)
a.print_inf()
a.edit_density(1000)
a.edit_strength(10)
a.print_inf()
