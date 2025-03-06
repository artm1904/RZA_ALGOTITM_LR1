from enum import Enum

class QualEnum(Enum):
    """
    Enum для представления качества (quality): good, invalid, reserved, questionable.
    """
    GOOD = "good"
    INVALID = "invalid"
    RESERVED = "reserved"
    QUESTIONABLE = "questionable"

    def __str__(self):
        """
        Возвращает строковое представление элемента Enum (удобно для вывода).
        """
        return self.value

    def __repr__(self):
        """
        Возвращает строковое представление для отладки.
        """
        return f"QualEnum.{self.name}"

    @classmethod
    def from_string(cls, value):
        """
        Создает объект QualEnum из строки. Игнорирует регистр символов.

        Args:
            value (str): Строка, представляющая QualEnum.

        Returns:
            QualEnum: Объект QualEnum, соответствующий строке.

        Raises:
            ValueError: Если строка не соответствует ни одному из допустимых значений QualEnum.
        """
        value = value.lower()  # Приводим к нижнему регистру для сравнения без учета регистра

        for member in cls:
            if member.value == value:
                return member

        raise ValueError(f"Invalid QualEnum value: {value}. Must be one of: {', '.join(member.value for member in cls)}")



# # Пример использования
# if __name__ == "__main__":
#     quality1 = QualEnum.GOOD
#     quality2 = QualEnum.INVALID
#
#     print(f"quality1: {quality1}")
#     print(f"quality2: {quality2}")
#     print(f"Repr(quality1): {repr(quality1)}")
#
#     if quality1 == QualEnum.GOOD:
#         print("quality1 is GOOD")
#
#     try:
#         quality3 = QualEnum.from_string("questionable")
#         print(f"quality3: {quality3}")
#     except ValueError as e:
#         print(f"Error: {e}")
#
#     try:
#         quality4 = QualEnum.from_string("unknown")
#     except ValueError as e:
#         print(f"Error: {e}")