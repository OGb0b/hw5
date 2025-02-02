def is_alpha_and_space(s):
    return all(char.isalpha() or char.isspace() for char in s)

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f'{self.title} - {self.author}, {self.year} г.'


class Library:
    def __init__(self):
        self.books= []

    def add_book(self, arr):
        title, author, year = arr[0], arr[1], int(arr[2])
        new_book = Book(title, author, year)
        self.books.append(new_book)

    def display_books(self):
        if not self.books:
            print('\nБиблиотека пуста')
            return
        print('\nВ библиотеке хранятся следующие книги:')
        for book in self.books:
            print(book)

    def original_library(self):
        self.add_book(['"Евгений Онегин"', 'Александр Пушкин', 1832])
        self.add_book(['"Герой нашего времени"', 'Михаил Лермонтов', 1840])
        self.add_book(['"Мертвые души"', 'Николай Гоголь', 1842])
        self.add_book(['"Отцы и дети"', 'Иван Тургенев', 1862])
        self.add_book(['"Война и мир"', 'Лев Толстой', 1869])
        self.add_book(['"Преступление и наказание"', 'Фёдор Достоевский', 1866])
        self.add_book(['"Анна Каренина"', 'Лев Толстой', 1877])
        self.add_book(['"Братья Карамазовы"', 'Фёдор Достоевский', 1880])
        self.add_book(['"Обломов"', 'Иван Гончаров,', 1859])
        self.add_book(['"Горе от ума"', 'Александр Грибоедов', 1825])

    def quick_sort_by_title(self, books=None):
        if books is None:
            books = self.books
        if len(books) <= 1:
            return books
        pivot = books[len(books)//2].title
        left = [x for x in books if x.title < pivot]
        middle = [x for x in books if x.title == pivot]
        right = [x for x in books if x.title > pivot]
        return self.quick_sort_by_title(left) + self.quick_sort_by_title(middle) + self.quick_sort_by_title(right)

    def sort_books_by_title(self):
        self.books = self.quick_sort_by_title()

    def merge_sort_by_author(self, books=None):
        if books is None:
            books = self.books
        if len(books) <= 1:
            return books
        mid = len(books)//2
        left = self.merge_sort_by_author(books[:mid])
        right = self.merge_sort_by_author(books[mid:])
        return self.merge(left, right)

    def merge(self,left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i].author < right[j].author:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort_by_author(self):
        self.books = self.merge_sort_by_author()

    def heapify(self, n, i, books=None):
        if books is None:
            books = self.books.copy()

        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and books[left].year > books[largest].year:
            largest = left

        if right < n  and books[right].year > books[largest].year:
            largest = right

        if largest != i:
            books[i], books[largest] = books[largest], books[i]
            self.heapify(n, largest, books)

    def heap_sort(self, books=None):
        if books is None:
            books = self.books.copy()
        n = len(books)
        for i in range(n//2-1, -1, -1):
            self.heapify(n, i, books)
        for i in range(n-1,0,-1):
            books[i], books[0] = books[0], books[i]
            self.heapify(i, 0, books)
        return books

    def sort_by_year(self):
        self.books = self.heap_sort()

    def find_by_title(self, title):
        flag = True
        for book in self.books:
            if title in book.title.lower():
                print(book)
                flag = False
        if flag:
            print('Данная книга не найдена')

    def find_by_author(self, author):
        flag = True
        for book in self.books:
            book1 = book.author.lower()
            if author in book1 or author in book1.split(' ')[1] + ' ' +  book1.split(' ')[0] :
                print(book)
                flag = False
        if flag:
            print('Книги данного автора не найдены')

    def delete_book(self, title):
        title = '"' + title + '"'
        for book in self.books:
            if title == book.title.lower():
                self.books.pop(self.books.index(book))
                print('Книга удалена')



def main():
    library = Library()
    library.original_library()

    while True:
        print('\n1. Показать все книги')
        print('2. Сортировать книги по названию')
        print('3. Сортировать книги по автору')
        print('4. Сортировать книги по году издания')
        print('5. Найти книгу по названию')
        print('6. Найти книгу по автору')
        print('7. Добавить книгу')
        print('8. Удалить книгу')
        print('9. Выйти')

        choice = input('Выберите действие: ')

        if choice == '1':
            library.display_books()
        elif choice == '2':
            library.sort_books_by_title()
            print('Библиотека отсортирована')
        elif choice == '3':
            library.sort_by_author()
            print('Библиотека отсортирована')
        elif choice == '4':
            library.sort_by_year()
            print('Библиотека отсортирована')
        elif choice == '5':
            title = input('Введите название книги в без кавычек: ').lower()
            print(title)
            if not is_alpha_and_space(title):
                 print('Неправильный формат введенных данных')
            else:
                library.find_by_title(title)
        elif choice == '6':
            author = input('Введите имя автора: ').lower()
            if not is_alpha_and_space(author):
                 print('Неправильный формат введенных данных')
            else:
                library.find_by_author(author)
        elif choice == '7':
            title = input('Введите название книги: ')
            author = input('Введите имя и фамилию автора книги: ')
            year = input('Введите год выхода книги: ')
            try:
                library.add_book([title, author, year])
                print('Книга добавлена')
            except ValueError as e:
                print(f'Неправильный формат данных: {e}')
        elif choice == '8':
            title = input('Введите название книги, которую нужно удалить без кавычек: ').lower()
            if not is_alpha_and_space(title):
                print('Неправильный формат введенных данных')
            else:
                library.delete_book(title)

        elif choice == '9':
            break
        else:
            print('Неверный ввод, попробуйте еще раз')


if __name__ == '__main__':
    main()