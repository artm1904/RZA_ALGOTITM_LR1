class BOOLEAN:
    """
    Класс-обертка для имитации типа данных BOOLEAN.
    """

    def __init__(self, value=False):
        """
        Инициализирует объект Boolean.

        Args:
            value (bool, optional): Начальное логическое значение. Defaults to False.

        Raises:
            TypeError: Если value не является логическим значением (bool).
        """
        if not isinstance(value, bool):
            raise TypeError("Value must be a boolean (True or False).")

        self._value = value

    @property
    def value(self):
        """
        Возвращает текущее логическое значение.
        """
        return self._value

    @value.setter
    def value(self, new_value):
        """
        Устанавливает новое логическое значение.

        Args:
            new_value (bool): Новое логическое значение.

        Raises:
            TypeError: Если new_value не является логическим значением (bool).
        """
        if not isinstance(new_value, bool):
            raise TypeError("Value must be a boolean (True or False).")

        self._value = new_value

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        """
        return str(self._value)

    def __repr__(self):
        """
        Возвращает строковое представление объекта для отладки.
        """
        return f"Boolean({self._value})"

    def __bool__(self):
        """
        Позволяет использовать объект Boolean в логических операциях (например, if, while).
        """
        return self._value

    def __eq__(self, other):
        """
        Переопределяет оператор ==.
        """
        if isinstance(other, BOOLEAN):
            return self.value == other.value
        elif isinstance(other, bool):
            return self.value == other
        else:
            return False

    def __and__(self, other):
        """
        Переопределяет оператор & (логическое И).
        """
        if isinstance(other, BOOLEAN):
            return BOOLEAN(self.value and other.value)
        elif isinstance(other, bool):
            return BOOLEAN(self.value and other)
        else:
            return NotImplemented

    def __or__(self, other):
        """
        Переопределяет оператор | (логическое ИЛИ).
        """
        if isinstance(other, BOOLEAN):
            return BOOLEAN(self.value or other.value)
        elif isinstance(other, bool):
            return BOOLEAN(self.value or other)
        else:
            return NotImplemented

    def __xor__(self, other):
        """
        Переопределяет оператор ^ (логическое исключающее ИЛИ).
        """
        if isinstance(other, BOOLEAN):
            return BOOLEAN(self.value ^ other.value)
        elif isinstance(other, bool):
            return BOOLEAN(self.value ^ other)
        else:
            return NotImplemented

    def __invert__(self):
        """
        Переопределяет оператор ~ (логическое НЕ).
        """
        return BOOLEAN(not self.value)

    def to_bytes(self):
        """
        Преобразует логическое значение в байты (1 байт: 0x01 для True, 0x00 для False).
        """
        return b'\x01' if self._value else b'\x00'

    @classmethod
    def from_bytes(cls, byte_data):
        """
        Создает объект Boolean из байтов (1 байт: 0x01 для True, 0x00 для False).

        Args:
            byte_data (bytes): Байты, представляющие логическое значение.

        Raises:
            ValueError: Если длина byte_data не равна 1 или значение байта не равно 0x00 или 0x01.
        """
        if len(byte_data) != 1:
            raise ValueError("Byte data must be 1 byte long for Boolean.")

        if byte_data == b'\x01':
            return cls(True)
        elif byte_data == b'\x00':
            return cls(False)
        else:
            raise ValueError("Invalid byte value for Boolean. Must be 0x00 or 0x01.")


# # Пример использования
# if __name__ == "__main__":
#     flag1 = Boolean(True)
#     flag2 = Boolean(False)
#
#     print(f"flag1: {flag1}")
#     print(f"flag2: {flag2}")
#
#     print(f"flag1 == True: {flag1 == True}")
#
#     print(f"flag1 and flag2: {flag1 & flag2}")
#     print(f"flag1 or flag2: {flag1 | flag2}")
#     print(f"flag1 xor flag2: {flag1 ^ flag2}")
#     print(f"not flag1: {~flag1}")
#
#     byte_data = flag1.to_bytes()
#     print(f"Bytes: {byte_data}")
#     new_flag = Boolean.from_bytes(byte_data)
#     print(f"From bytes: {new_flag}")
#
#     if flag1:
#         print("flag1 is True")
#     else:
#         print("flag1 is False")
#
#     try:
#         invalid_flag = Boolean.from_bytes(b'\x02') #Вызовет ValueError
#     except ValueError as e:
#         print(f"Error: {e}")