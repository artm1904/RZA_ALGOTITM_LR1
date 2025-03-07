# В Python, имитация типа данных VISIBLE STRING255, часто используемого в телекоммуникациях
# и сетевых протоколах, требует класса-обертки, который ограничивает длину строки 255
# символами и разрешает только видимые ASCII символы (коды 32-126 включительно).
# Вот реализация такого класса:


class VISIBLE_STRING255:
    """
    Класс-обертка для имитации VISIBLE STRING255: строка длиной до 255 символов,
    состоящая только из видимых ASCII символов (коды 32-126).
    """

    MAX_LENGTH = 255
    MIN_CHAR_CODE = 32  # Space
    MAX_CHAR_CODE = 126 # Tilde (~)

    def __init__(self, value=""):
        """
        Инициализирует объект VisibleString255.

        Args:
            value (str, optional): Начальная строка. Defaults to "".

        Raises:
            TypeError: Если value не является строкой.
            ValueError: Если длина value превышает 255 символов или содержит недопустимые символы.
        """
        if not isinstance(value, str):
            raise TypeError("Value must be a string.")

        if len(value) > self.MAX_LENGTH:
            raise ValueError(f"String length cannot exceed {self.MAX_LENGTH} characters.")

        for char in value:
            if not (self.MIN_CHAR_CODE <= ord(char) <= self.MAX_CHAR_CODE):
                raise ValueError(
                    "String must contain only visible ASCII characters (codes 32-126)."
                )

        self._value = value

    @property
    def value(self):
        """
        Возвращает текущую строку.
        """
        return self._value

    @value.setter
    def value(self, new_value):
        """
        Устанавливает новую строку.

        Args:
            new_value (str): Новая строка.

        Raises:
            TypeError: Если new_value не является строкой.
            ValueError: Если длина new_value превышает 255 символов или содержит недопустимые символы.
        """
        if not isinstance(new_value, str):
            raise TypeError("Value must be a string.")

        if len(new_value) > self.MAX_LENGTH:
            raise ValueError(f"String length cannot exceed {self.MAX_LENGTH} characters.")

        for char in new_value:
            if not (self.MIN_CHAR_CODE <= ord(char) <= self.MAX_CHAR_CODE):
                raise ValueError(
                    "String must contain only visible ASCII characters (codes 32-126)."
                )

        self._value = new_value

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        """
        return self._value

    def __repr__(self):
        """
        Возвращает строковое представление объекта для отладки.
        """
        return f"VisibleString255('{self._value}')"

    def __eq__(self, other):
        """
        Переопределяет оператор ==.
        """
        if isinstance(other, VISIBLE_STRING255):
            return self.value == other.value
        elif isinstance(other, str):
            return self.value == other
        else:
            return False

    def to_bytes(self, encoding='ascii'):
        """
        Преобразует строку в байты, используя указанную кодировку.

        Args:
            encoding (str, optional): Кодировка для преобразования в байты. Defaults to 'ascii'.

        Returns:
            bytes: Байтовое представление строки.

        Raises:
            UnicodeEncodeError: Если encoding не поддерживает все символы в строке.
        """
        return self._value.encode(encoding)

    @classmethod
    def from_bytes(cls, byte_data, encoding='ascii'):
        """
        Создает объект VisibleString255 из байтов, используя указанную кодировку.

        Args:
            byte_data (bytes): Байты, представляющие строку.
            encoding (str, optional): Кодировка для преобразования из байтов. Defaults to 'ascii'.

        Returns:
            VisibleString255: Объект VisibleString255, созданный из байтов.

        Raises:
            UnicodeDecodeError: Если encoding не может декодировать байты.
            ValueError: Если полученная строка не является допустимой VisibleString255.
        """
        try:
            string_value = byte_data.decode(encoding)
        except UnicodeDecodeError as e:
            raise UnicodeDecodeError(f"Could not decode bytes: {e}")

        return cls(string_value)



#     # Пример использования
# if __name__ == "__main__":
#     valid_string = VisibleString255("Hello, World!")
#     print(f"Valid string: {valid_string}")
#
#     print(f"Valid string == 'Hello, World!': {valid_string == 'Hello, World!'}")
#
#     byte_data = valid_string.to_bytes()
#     print(f"Bytes: {byte_data}")
#     new_string = VisibleString255.from_bytes(byte_data)
#     print(f"From bytes: {new_string}")
#
#     try:
#         invalid_string = VisibleString255("Invalid\nString")  # Вызовет ValueError
#     except ValueError as e:
#         print(f"Error: {e}")
#
#     try:
#         long_string = VisibleString255("A" * 256)  # Вызовет ValueError
#     except ValueError as e:
#         print(f"Error: {e}")
#
#     try:
#         unicode_string = VisibleString255("你好") #Вызовет ValueError
#     except ValueError as e:
#         print(f"Error: {e}")