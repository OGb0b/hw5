import pytest
from main import Library


@pytest.fixture
def library():
    lib = Library()
    lib.original_library()
    return lib


def test_add_book(library):
    library.add_book(["New Book", "New Author", 2023])
    assert len(library.books) == 11
    assert library.books[-1].title == "New Book"
    assert library.books[-1].author == "New Author"
    assert library.books[-1].year == 2023

def test_display_books_empty(capsys):
    lib = Library()
    lib.display_books()
    captured = capsys.readouterr()
    assert "Библиотека пуста" in captured.out

def test_display_books(library, capsys):
    library.display_books()
    captured = capsys.readouterr()
    assert "Евгений Онегин" in captured.out
    assert "Лев Толстой" in captured.out

def test_quick_sort_by_title(library):
    library.sort_books_by_title()
    titles = [book.title for book in library.books]
    assert titles == sorted(titles)

def test_merge_sort_by_author(library):
    library.sort_by_author()
    authors = [book.author for book in library.books]
    assert authors == sorted(authors)

def test_heap_sort_by_year(library):
    library.sort_by_year()
    years = [book.year for book in library.books]
    assert years == sorted(years)

def test_find_by_title(library, capsys):
    library.find_by_title("евгений онегин")
    captured = capsys.readouterr()
    assert "Евгений Онегин" in captured.out

def test_find_by_author(library, capsys):
    library.find_by_author("пушкин")
    captured = capsys.readouterr()
    assert "Александр Пушкин" in captured.out

def test_delete_book(library):
    library.delete_book("евгений онегин")
    titles = [book.title for book in library.books]
    assert '"Евгений Онегин"' not in titles

