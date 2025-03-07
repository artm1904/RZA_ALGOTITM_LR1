class INT32:
    """
    Класс-обертка над int32, предоставляющий дополнительные методы и свойства.
    """

    MIN_VALUE = -2147483648  # -2**31
    MAX_VALUE = 2147483647   # 2**31 - 1

    def __init__(self, value=0):
        """
        Инициализирует объект Int32Wrapper.

        Args:
            value (int, optional): Начальное значение int32. Defaults to 0.

        Raises:
            ValueError: Если value не является целым числом или выходит за пределы диапазона int32.
        """
        if not isinstance(value, int):
            raise ValueError("Value must be an integer.")

        if not (self.MIN_VALUE <= value <= self.MAX_VALUE):
            raise ValueError(f"Value must be within the range of int32 ({self.MIN_VALUE} to {self.MAX_VALUE}).")

        self._value = value

    @property
    def value(self):
        """
        Возвращает текущее значение int32.
        """
        return self._value

    @value.setter
    def value(self, new_value):
        """
        Устанавливает новое значение int32.

        Args:
            new_value (int): Новое значение int32.

        Raises:
            ValueError: Если new_value не является целым числом или выходит за пределы диапазона int32.
        """
        if not isinstance(new_value, int):
            raise ValueError("Value must be an integer.")

        if not (self.MIN_VALUE <= new_value <= self.MAX_VALUE):
            raise ValueError(f"Value must be within the range of int32 ({self.MIN_VALUE} to {self.MAX_VALUE}).")

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
        return f"Int32Wrapper({self._value})"

    def __add__(self, other):
        """
        Переопределяет оператор +.
        """
        if isinstance(other, INT32):
            result = self.value + other.value
        elif isinstance(other, int):
            result = self.value + other
        else:
            return NotImplemented # Позволяет Python попробовать сложение с другим типом
            # (например, если определен __radd__ для другого класса)

        if not (self.MIN_VALUE <= result <= self.MAX_VALUE):
            raise OverflowError("Result exceeds int32 range.")

        return INT32(result)

    def __sub__(self, other):
        """
        Переопределяет оператор -.
        """
        if isinstance(other, INT32):
            result = self.value - other.value
        elif isinstance(other, int):
            result = self.value - other
        else:
            return NotImplemented

        if not (self.MIN_VALUE <= result <= self.MAX_VALUE):
            raise OverflowError("Result exceeds int32 range.")

        return INT32(result)

    def __mul__(self, other):
        """
        Переопределяет оператор *.
        """
        if isinstance(other, INT32):
            result = self.value * other.value
        elif isinstance(other, int):
            result = self.value * other
        else:
            return NotImplemented

        if not (self.MIN_VALUE <= result <= self.MAX_VALUE):
            raise OverflowError("Result exceeds int32 range.")

        return INT32(result)

    def __int__(self):
        """
        Позволяет преобразовывать объект Int32Wrapper в int с помощью int().
        """
        return self._value

    def __eq__(self, other):
        """
        Переопределяет оператор ==.
        """
        if isinstance(other, INT32):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return False  # Не сравниваем с другими типами, возвращаем False



#         # Пример использования
# if __name__ == "__main__":
#     num1 = Int32Wrapper(100)
#     num2 = Int32Wrapper(200)
#
#     print(f"num1: {num1}")  # num1: 100
#     print(f"num2: {num2}")  # num2: 200
#
#     print(f"num1 + num2: {num1 + num2}")  # num1 + num2: Int32Wrapper(300)
#     print(f"num1 - num2: {num1 - num2}")  # num1 - num2: Int32Wrapper(-100)
#     print(f"num1 * num2: {num1 * num2}")  # num1 * num2: Int32Wrapper(20000)
#
#     try:
#         num3 = num1 * 2147483647  # Вызовет OverflowError
#     except OverflowError as e:
#         print(f"Error: {e}")  # Error: Result exceeds int32 range.
#
#     num4 = Int32Wrapper(1000)
#     print(f"num4 == 1000: {num4 == 1000}") # num4 == 1000: True
#     print(f"num4 == Int32Wrapper(1000): {num4 == Int32Wrapper(1000)}") # num4 == Int32Wrapper(1000): True
#
#     print(f"int(num1): {int(num1)}")  # int(num1): 100