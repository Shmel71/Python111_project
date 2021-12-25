from pprint import pprint


class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price
        print(' Description '.center(40, '*'))
        print(f'Назавание книги: {self.title}\n'
              f'Год выпуска: {self.year}\n'
              f'Издатель: {self.publisher}\n'
              f'Жанр: {self.genre}\n'
              f'Автор: {self.author}\n'
              f'Цена: {self.price}')
        print(40 * '*')

    def input_data(self):
        self.title = input("Введите название книги: ")
        self.year = input("Ввелите год издания: ")
        self.publisher = input("Введите издателя: ")
        self.genre = input("Введите жанр: ")
        self.author = input("Введите автора: ")
        self.price = input("Введите цену: ")

        print(f'Назавание книги: {self.title}\n'
              f'Год выпуска: {self.year}\n'
              f'Издатель: {self.publisher}\n'
              f'Жанр: {self.genre}\n'
              f'Автор: {self.author}\n'
              f'Цена: {self.price}')

    def set_atribute(self):
        a = input("Введите название поля: ")
        count = input("Введите значение поля: ")
        print(getattr(b1, a, count))


b1 = Book("StarWars", "1992", "'Kalita' Moscow", "Science fiction", "George Lucas", "5 usd")
print(getattr(b1, "title"))
print()
setattr(b1, "edition", 1000)
pprint(b1.__dict__)
print()
delattr(b1, "year")
pprint(b1.__dict__)
b1.input_data()
