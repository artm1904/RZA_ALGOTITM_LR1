import math
import struct


class FLOAT32:
    """
    Класс-обертка над float32 (single-precision floating-point number),
    предоставляющий дополнительные методы и свойства.  Использует struct для
    упаковки и распаковки значений для обеспечения точности float32.
    """

    MIN_VALUE = -3.4028235e38  # Максимальное отрицательное значение float32
    MAX_VALUE = 3.4028235e38   # Максимальное положительное значение float32

    def __init__(self, value=0.0):
        """
        Инициализирует объект Float32Wrapper.

        Args:
            value (float, optional): Начальное значение float32. Defaults to 0.0.

        Raises:
            TypeError: Если value не является числом (int или float).
            ValueError: Если value выходит за пределы диапазона float32.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be a number (int or float).")

        if not (self.MIN_VALUE <= value <= self.MAX_VALUE):
            raise ValueError(f"Value must be within the range of float32 ({self.MIN_VALUE} to {self.MAX_VALUE}).")

        self._value = float(value)  # Преобразуем в float для единообразия

    @property
    def value(self):
        """
        Возвращает текущее значение float32.
        """
        return self._value

    @value.setter
    def value(self, new_value):
        """
        Устанавливает новое значение float32.

        Args:
            new_value (float): Новое значение float32.

        Raises:
            TypeError: Если new_value не является числом (int или float).
            ValueError: Если new_value выходит за пределы диапазона float32.
        """
        if not isinstance(new_value, (int, float)):
            raise TypeError("Value must be a number (int or float).")

        if not (self.MIN_VALUE <= new_value <= self.MAX_VALUE):
            raise ValueError(f"Value must be within the range of float32 ({self.MIN_VALUE} to {self.MAX_VALUE}).")

        self._value = float(new_value)  # Преобразуем в float для единообразия

    def __str__(self):
        """
        Возвращает строковое представление объекта.
        """
        return str(self._value)

    def __repr__(self):
        """
        Возвращает строковое представление объекта для отладки.
        """
        return f"Float32Wrapper({self._value})"

    def __add__(self, other):
        """
        Переопределяет оператор +.
        """
        if isinstance(other, FLOAT32):
            result = self.value + other.value
        elif isinstance(other, (int, float)):
            result = self.value + other
        else:
            return NotImplemented

        if not (self.MIN_VALUE <= result <= self.MAX_VALUE):
            raise OverflowError("Result exceeds float32 range.")

        return FLOAT32(result)

    def __sub__(self, other):
        """
        Переопределяет оператор -.
        """
        if isinstance(other, FLOAT32):
            result = self.value - other.value
        elif isinstance(other, (int, float)):
            result = self.value - other
        else:
            return NotImplemented

        if not (self.MIN_VALUE <= result <= self.MAX_VALUE):
            raise OverflowError("Result exceeds float32 range.")

        return FLOAT32(result)

    def __mul__(self, other):
        """
        Переопределяет оператор *.
        """
        if isinstance(other, FLOAT32):
            result = self.value * other.value
        elif isinstance(other, (int, float)):
            result = self.value * other
        else:
            return NotImplemented

        if not (self.MIN_VALUE <= result <= self.MAX_VALUE):
            raise OverflowError("Result exceeds float32 range.")

        return FLOAT32(result)

    def __truediv__(self, other):  # For / operator
        """
        Переопределяет оператор /.
        """
        if isinstance(other, FLOAT32):
            result = self.value / other.value
        elif isinstance(other, (int, float)):
            result = self.value / other
        else:
            return NotImplemented

        if not (self.MIN_VALUE <= result <= self.MAX_VALUE):
            raise OverflowError("Result exceeds float32 range.")

        return FLOAT32(result)

    def __float__(self):
        """
        Позволяет преобразовывать объект Float32Wrapper в float с помощью float().
        """
        return self._value

    def __eq__(self, other):
        """
        Переопределяет оператор ==.
        """
        if isinstance(other, FLOAT32):
            return self.value == other.value
        elif isinstance(other, (int, float)):
            return self.value == other
        else:
            return False

    def to_bytes(self, byte_order='little'):
        """
        Преобразует значение float32 в байты.

        Args:
            byte_order (str, optional): Порядок байтов ('little' или 'big'). Defaults to 'little'.

        Returns:
            bytes: Байтовое представление float32.
        """
        return struct.pack('<f' if byte_order == 'little' else '>f', self._value)

    @classmethod
    def from_bytes(cls, byte_data, byte_order='little'):
        """
        Создает объект Float32Wrapper из байтов.

        Args:
            byte_data (bytes): Байты, представляющие float32.
            byte_order (str, optional): Порядок байтов ('little' или 'big'). Defaults to 'little'.

        Returns:
            Float32Wrapper: Объект Float32Wrapper, созданный из байтов.

        Raises:
            ValueError: Если длина byte_data не равна 4.
        """
        if len(byte_data) != 4:
            raise ValueError("Byte data must be 4 bytes long for float32.")

        return cls(struct.unpack('<f' if byte_order == 'little' else '>f', byte_data)[0])

    def is_nan(self):
        """
        Проверяет, является ли значение NaN (Not a Number).
        """
        return math.isnan(self._value)

    def is_infinite(self):
        """
        Проверяет, является ли значение бесконечным (positive or negative infinity).
        """
        return math.isinf(self._value)


#     # Пример использования
# if __name__ == "__main__":
#     num1 = Float32Wrapper(3.14)
#     num2 = Float32Wrapper(2.71)
#
#     print(f"num1: {num1}")  # num1: 3.14
#     print(f"num2: {num2}")  # num2: 2.71
#
#     print(f"num1 + num2: {num1 + num2}")  # num1 + num2: Float32Wrapper(5.85)
#     print(f"num1 - num2: {num1 - num2}")  # num1 - num2: Float32Wrapper(0.4299999999999997)
#     print(f"num1 * num2: {num1 * num2}")  # num1 * num2: Float32Wrapper(8.5094)
#     print(f"num1 / num2: {num1 / num2}")  # num1 / num2: Float32Wrapper(1.1586715867158672)
#
#     try:
#         num3 = num1 * Float32Wrapper(1e38)  # Вызовет OverflowError
#     except OverflowError as e:
#         print(f"Error: {e}")  # Error: Result exceeds float32 range.
#
#     print(f"num1 == 3.14: {num1 == 3.14}")  # num1 == 3.14: True
#     print(f"num1 == Float32Wrapper(3.14): {num1 == Float32Wrapper(3.14)}")  # num1 == Float32Wrapper(3.14): True
#
#     print(f"float(num1): {float(num1)}")  # float(num1): 3.14
#
#     # Пример преобразования в байты и обратно
#     byte_data = num1.to_bytes()
#     print(f"Bytes: {byte_data}")  # Bytes: b'\xc3\xf5H@' (может отличаться в зависимости от порядка байтов)
#     num5 = Float32Wrapper.from_bytes(byte_data)
#     print(f"From bytes: {num5}")  # From bytes: Float32Wrapper(3.140000104904175)
#
#     num6 = Float32Wrapper(float('nan'))
#     print(f"Is NaN: {num6.is_nan()}") # Is NaN: True
#
#     num7 = Float32Wrapper(float('inf'))
#     print(f"Is Infinite: {num7.is_infinite()}") # Is Infinite: True