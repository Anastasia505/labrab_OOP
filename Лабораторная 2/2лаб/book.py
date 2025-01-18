BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация объекта "Книга".

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц в книге
        """
        if not isinstance(id_, int) or id_ <= 0:
            raise ValueError("Идентификатор книги должен быть положительным целым числом")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Название книги должно быть непустой строкой")
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Возвращает строковое представление книги.
        :return: Строка формата 'Книга "название_книги"'
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строку, по которой можно инициализировать объект.
        :return: Строка формата Book(id_=id, name='название', pages=количество_страниц)
        """
        return f"Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})"


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
