from enum import Enum

class CtlModels(Enum):

    STATUS_ONLY = "status-only"
    DIRECT_WITH_NORMAL_SECURITY = "direct-with-normal-security"
    SBO_WITH_NORMAL_SECURITY = "sbo-with-normal-security"
    DIRECT_WITH_ENHANCED_SECURITY = "direct-with-enhanced-security"
    SBO_WITH_ENHANCED_SECURITY = "sbo-with-enhanced-security"

    def __str__(self):
        """
        Возвращает строковое представление элемента Enum (удобно для вывода).
        """
        return self.value

    def __repr__(self):
        """
        Возвращает строковое представление для отладки.
        """
        return f"CtlModels.{self.name}"

    @classmethod
    def from_string(cls, value):
        """
        Создает объект CtlModels из строки.  Игнорирует регистр символов.

        Args:
            value (str): Строка, представляющая CtlModels.

        Returns:
            CtlModels: Объект CtlModels, соответствующий строке.

        Raises:
            ValueError: Если строка не соответствует ни одному из допустимых значений CtlModels.
        """
        value = value.lower()  # Приводим к нижнему регистру для сравнения без учета регистра

        for member in cls:
            if member.value == value:
                return member

        raise ValueError(f"Invalid CtlModels value: {value}.  Must be one of: {', '.join(member.value for member in cls)}")


# # Пример использования
# if __name__ == "__main__":
#     direction1 = CtlModels.STATUS_ONLY
#     direction2 = CtlModels.DIRECT_WITH_NORMAL_SECURITY
#
#     print(f"direction1: {direction1}")
#     print(f"direction2: {direction2}")
#     print(f"Repr(direction1): {repr(direction1)}")
#
#     if direction1 == CtlModels.STATUS_ONLY:
#         print("direction1 is STATUS_ONLY")
#
#     try:
#         direction3 = CtlModels.from_string("sbo-with-normal-security")
#         print(f"direction3: {direction3}")
#     except ValueError as e:
#         print(f"Error: {e}")
#
#     try:
#         direction4 = CtlModels.from_string("sbo-with-enhanced-security")
#     except ValueError as e:
#         print(f"Error: {e}")