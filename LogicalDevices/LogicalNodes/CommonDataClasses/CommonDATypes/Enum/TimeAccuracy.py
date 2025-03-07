from enum import Enum

class TimeAccuracy(Enum):
    """
    Enum для представления TimeAccuracy значений (в секундах).
    """
    T_0_01 = 0.01
    T_0_001 = 0.001
    T_0_0001 = 0.0001
    T_0_000025 = 0.000025
    T_0_000004 = 0.000004
    T_0_000001 = 0.000001

    def __str__(self):
        """
        Возвращает строковое представление элемента Enum (удобно для вывода).
        """
        return str(self.value)

    def __repr__(self):
        """
        Возвращает строковое представление для отладки.
        """
        return f"TimeAccuracy.{self.name}"

    @classmethod
    def from_float(cls, value):
        """
        Создает объект TimeAccuracy из числа (float).

        Args:
            value (float): Число, представляющее TimeAccuracy.

        Returns:
            TimeAccuracy: Объект TimeAccuracy, соответствующий числу.

        Raises:
            ValueError: Если число не соответствует ни одному из допустимых значений TimeAccuracy.
        """

        for member in cls:
            if abs(member.value - value) < 1e-9:  # Сравниваем с учетом погрешности
                return member

        raise ValueError(f"Invalid TimeAccuracy value: {value}.  Must be one of: {', '.join(str(member.value) for member in cls)}")


#
# # Пример использования
# if __name__ == "__main__":
#     acc1 = TimeAccuracy.T_0_001
#     acc2 = TimeAccuracy.T_0_000004
#
#     print(f"acc1: {acc1}")  # acc1: 0.001
#     print(f"acc2: {acc2}")  # acc2: 4e-06
#     print(f"Repr(acc1): {repr(acc1)}") # Repr(acc1): TimeAccuracy.T_0_001
#
#     if acc1 == TimeAccuracy.T_0_001:
#         print("acc1 is 0.001")
#
#     try:
#         acc3 = TimeAccuracy.from_float(0.0001)
#         print(f"acc3: {acc3}")
#     except ValueError as e:
#         print(f"Error: {e}")
#
#     try:
#         acc4 = TimeAccuracy.from_float(0.0002)
#     except ValueError as e:
#         print(f"Error: {e}") # Error: Invalid TimeAccuracy value: 0.0002.  Must be one of: 0.01, 0.001, 0.0001, 2.5e-05, 4e-06, 1e-06