import doctest
class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание объекта "Книга".

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not title:
            raise ValueError("Название книги не может быть пустым")

        if not isinstance(author, str):
            raise TypeError("Имя автора должно быть строкой")
        if not author:
            raise ValueError("Имя автора не может быть пустым")

        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")

        self.title = title
        self.author = author
        self.pages = pages

    def read_page(self, page: int) -> str:
        """
        Прочитать страницу книги.

        :param page: Номер страницы
        """
        if not (1 <= page <= self.pages):
            raise ValueError("Номер страницы должен быть в диапазоне от 1 до общего количества страниц")
        ...

    def get_summary(self) -> str:
        """
        Получить краткую информацию о книге.

        Примеры:
        >>> book = Book("1984", "George Orwell", 328)
        >>> book.read_page(10)
        """
        ...


class Pencil:
    def __init__(self, length: float, hardness: str, brand: str):
        """
        Создание объекта "Карандаш".

        :param length: Длина карандаша в сантиметрах
        :param hardness: Твёрдость грифеля
        :param brand: Производитель карандаша

        Примеры:
        >>> pencil = Pencil(17.5, "2B", "Faber-Castell")
        """
        if not isinstance(length, (int, float)) or length <= 0:
            raise ValueError("Длина карандаша должна быть положительным числом")
        if not isinstance(hardness, str) or not hardness:
            raise ValueError("Твёрдость должна быть строкой")
        if not isinstance(brand, str) or not brand:
            raise ValueError("Название бренда должно быть строкой")

        self.length = length
        self.hardness = hardness
        self.brand = brand
        self.is_sharp = True

    def write(self, text: str) -> None:
        """
        Написать текст с помощью карандаша.

        :param text: Текст, который нужно написать

        Примеры:
        >>> pencil = Pencil(17.5, "HB", "Faber-Castell")
        >>> pencil.write("Привет!")
        """
        if not isinstance(text, str) or not text:
            raise ValueError("Текст должен быть непустой строкой")
        if not self.is_sharp:
            raise ValueError("Карандаш затупился. Его нужно заточить")
        ...

    def sharpen(self) -> None:
        """
        Заточить карандаш, чтобы он снова мог писать.

        Примеры:
        >>> pencil = Pencil(17.5, "HB", "Faber-Castell")
        >>> pencil.sharpen()
        """
        if self.length <= 1:
            raise ValueError("Карандаш слишком короткий для заточки")
        ...


class Paper:
    def __init__(self, width: float, height: float, thickness: float):
        """
        Создание объекта "Бумага".

        :param width: Ширина листа бумаги в сантиметрах
        :param height: Высота листа бумаги в сантиметрах
        :param thickness: Толщина бумаги в миллиметрах

        Примеры:
        >>> paper = Paper(21.0, 29.7, 0.1)  # Лист формата A4
        """
        if not isinstance(width, (int, float)) or width <= 0:
            raise ValueError("Ширина должна быть положительным числом")
        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота должна быть положительным числом")
        if not isinstance(thickness, (int, float)) or thickness <= 0:
            raise ValueError("Толщина должна быть положительным числом")

        self.width = width
        self.height = height
        self.thickness = thickness
        self.is_written_on = False

    def write_on(self, text: str) -> None:
        """
        Написать текст на бумаге.

        :param text: Текст, который нужно написать

        Примеры:
        >>> paper = Paper(21.0, 29.7, 0.1)
        >>> paper.write_on("Доброе утро")
        """
        if not isinstance(text, str) or not text:
            raise ValueError("Текст должен быть непустой строкой")
        if self.is_written_on:
            raise ValueError("На бумаге уже что-то написано")
        ...

    def fold(self) -> None:
        """
        Сложить бумагу.
        
        Примеры:
        >>> paper = Paper(21.0, 29.7, 0.1)
        >>> paper.fold()
        """
        if self.thickness > 0.5:
            raise ValueError("Бумага слишком толстая для складывания")
        ...

if __name__ == "__main__":
    doctest.testmod()
