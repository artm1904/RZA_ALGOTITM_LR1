from enum import Enum


class QPosEnum(Enum):
    """
    Enum для представления QPos значений: intermediate-state, off, on, bad-state.
    """
    INTERMEDIATE_STATE = "intermediate-state"
    OFF = "off"
    ON = "on"
    BAD_STATE = "bad-state"

    def __str__(self):
        """
        Возвращает строковое представление элемента Enum (удобно для вывода).
        """
        return self.value

    def __repr__(self):
        """
        Возвращает строковое представление для отладки.
        """
        return f"QPosEnum.{self.name}"

    @classmethod
    def from_string(cls, value):
        """
        Создает объект QPosEnum из строки.  Игнорирует регистр символов.

        Args:
            value (str): Строка, представляющая QPosEnum.

        Returns:
            QPosEnum: Объект QPosEnum, соответствующий строке.

        Raises:
            ValueError: Если строка не соответствует ни одному из допустимых значений QPosEnum.
        """
        value = value.lower()  # Приводим к нижнему регистру для сравнения без учета регистра

        for member in cls:
            if member.value == value:
                return member

        raise ValueError(
            f"Invalid QPosEnum value: {value}.  Must be one of: {', '.join(member.value for member in cls)}")


# # Пример использования
# if __name__ == "__main__":
#     pos1 = QPosEnum.ON
#     pos2 = QPosEnum.OFF
#
#     print(f"pos1: {pos1}")  # pos1: on
#     print(f"pos2: {pos2}")  # pos2: off
#     print(f"Repr(pos1): {repr(pos1)}") # Repr(pos1): QPosEnum.ON
#
#     if pos1 == QPosEnum.ON:
#         print("pos1 is ON")
#
#     try:
#         pos3 = QPosEnum.from_string("Intermediate-State") #работает без учета регистра
#         print(f"pos3: {pos3}") # pos3: intermediate-state
#     except ValueError as e:
#         print(f"Error: {e}")
#
#     try:
#         pos4 = QPosEnum.from_string("invalid")
#     except ValueError as e:
#         print(f"Error: {e}") #Error: Invalid QPosEnum value: invalid.  Must be one of: intermediate-state, off, on, bad-state