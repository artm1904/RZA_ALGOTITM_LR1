from enum import Enum

class DirEnum(Enum):
    """
    Enum для представления направлений (direction): unknow, forward, backward.
    """
    UNKNOWN = "unknown"  # Обратите внимание на правильное написание "unknow"
    FORWARD = "forward"
    BACKWARD = "backward"

    def __str__(self):
        """
        Возвращает строковое представление элемента Enum (удобно для вывода).
        """
        return self.value

    def __repr__(self):
        """
        Возвращает строковое представление для отладки.
        """
        return f"DirEnum.{self.name}"

    @classmethod
    def from_string(cls, value):
        """
        Создает объект DirEnum из строки.  Игнорирует регистр символов.

        Args:
            value (str): Строка, представляющая DirEnum.

        Returns:
            DirEnum: Объект DirEnum, соответствующий строке.

        Raises:
            ValueError: Если строка не соответствует ни одному из допустимых значений DirEnum.
        """
        value = value.lower()  # Приводим к нижнему регистру для сравнения без учета регистра

        for member in cls:
            if member.value == value:
                return member

        raise ValueError(f"Invalid DirEnum value: {value}.  Must be one of: {', '.join(member.value for member in cls)}")



# # Пример использования
# if __name__ == "__main__":
#     direction1 = DirEnum.FORWARD
#     direction2 = DirEnum.BACKWARD

    # print(f"direction1: {direction1}")
    # print(f"direction2: {direction2}")
    # print(direction2.value)
    # print(f"Repr(direction1): {repr(direction1)}")
    #
    # if direction1 == DirEnum.FORWARD:
    #     print("direction1 is FORWARD")
    #
    # try:
    #     direction3 = DirEnum.from_string("backward")
    #     print(f"direction3: {direction3}")
    # except ValueError as e:
    #     print(f"Error: {e}")
    #
    # try:
    #     direction4 = DirEnum.from_string("invalid")
    # except ValueError as e:
    #     print(f"Error: {e}")