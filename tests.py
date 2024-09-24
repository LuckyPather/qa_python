import pytest

from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize("book_name, genre", [
        ("test_book1", "Фантастика"),
        ("test_book2", "Ужасы"),
        ("test_book3", "Детективы"),
        ("test_book4", "Мультфильмы"),
        ("test_book5", "Комедии")])
    def test_set_book_genre_all_genre(self, book_name, genre):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книги
        collector.add_new_book(book_name)

        # устанавливаем книгам жанр
        collector.set_book_genre(book_name, genre)

        # проверяем что жанры присвоились верно
        assert collector.books_genre[book_name] == genre, "Жанр установился неверно"

    @pytest.mark.parametrize("book_name, genre", [
        ("test_book1", "Фантастика"),
        ("test_book2", "Ужасы"),
        ("test_book3", "Детективы"),
        ("test_book4", "Мультфильмы"),
        ("test_book5", "Комедии")])
    def test_get_book_genre_two_genre(self, book_name, genre):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книги
        collector.add_new_book(book_name)

        # устанавливаем книгам жанр
        collector.set_book_genre(book_name, genre)

        # получаем жанр книги по ее имени и сравниваем
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize("book_name, genre", [
        ("test_book1", "Фантастика"),
        ("test_book2", "Фантастика")])
    def test_get_books_with_specific_genre_fantastic(self, book_name, genre):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # добавляем книги
        collector.add_new_book(book_name)
        # устанавливаем книгам жанр
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_with_specific_genre(genre)[0] == book_name, "Неверный список книг с заданным жанром"

    def test_get_books_genre_four_elements(self):
        collector = BooksCollector()
        list_of_books = ['test_book1', 'test_book2', 'test_book3', 'test_book4']
        for i in list_of_books:
            collector.add_new_book(i)
        assert len(list_of_books) == len(collector.get_books_genre()), ("Имеется разница между записанными элементами "
                                                                        "в словарь и полученным словарем")

    def test_get_book_for_children(self):
        collector = BooksCollector()
        collector.books_genre = {
            'Дюна': 'Фантастика',
            'Сияние': 'Ужасы',
            'Шерлок Холмс': 'Детективы',
            'Король Лев': 'Мультфильмы',
            'Трое в лодке, не считая собаки': 'Комедии'
        }
        assert collector.get_books_for_children() == ['Дюна', 'Король Лев', 'Трое в лодке, не считая собаки'], "Несоответсвие списка фильмов для детей"

    @pytest.mark.parametrize('name', [
        "Дюна", "Сияние", "Король лев"])
    def test_add_book_favorites(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() == [name]

    @pytest.mark.parametrize("name", ['Дюна', 'Сияние'])
    def test_delete_book_from_favorites(self, name):
        collector = BooksCollector()
        collector.books_genre = {
            'Дюна': 'Фантастика',
            'Сияние': 'Ужасы',
            'Шерлок Холмс': 'Детективы',
            'Король Лев': 'Мультфильмы',
            'Трое в лодке, не считая собаки': 'Комедии'
        }
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites, "Метод удаления книги из избранного отработал неверно"

    @pytest.mark.parametrize("name", ['Дюна', 'Сияние'])
    def test_get_list_of_favorites_books(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books(), ("Полученный словарь со списокм избранных книг не "
                                                                 "соответсвует ожидаемому")
