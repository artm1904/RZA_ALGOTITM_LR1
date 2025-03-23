import math
from dataclasses import field

from LogicalDevices.LogicalNodes.CommonDataClasses.CMV import CMV
from LogicalDevices.LogicalNodes.CommonDataClasses.MV import MV
from LogicalDevices.LogicalNodes.Filter import Filter

class RMS(Filter):
    buffer_size: int  # Размер буфера
    buffer: list[MV] = field(init=False)  # Создание буфера нужного размера
    buffer_count: int  # Счетчик выборки
    summ_val_RMS: float  # Действующее значение

    def __init__(self, buffer_size: int):
        self.buffer_size = buffer_size

    def __post_init__(self):
        """
        Initializes the RMS filter.  This runs after the dataclass is initialized.
        """

        self.buffer = [MV() for _ in range(self.buffer_size)]  # Создание буфера нужного размера

        self.buffer_count = 0  # Счетчик выборки
        self.summ_val_RMS = 0.0  # Действующее значение

    def process(self, measured_value: MV, complex_measurement_value: CMV):
        """
            Processes a measured value using the RMS transform.

            Args:
                measured_value: The measured value (MV).
                complex_measurement_value: The complex measurement value (CMV) to update.
            """

        # Новое измеренное значение
        new_val = measured_value.mag.f.value

        # Старое измеренное значение, хранящееся в буфере
        old_val = self.buffer[self.buffer_count].mag.f.value

        # Расчёт действующего значения
        self.summ_val_RMS = (self.summ_val_RMS
                             + (1 / self.buffer_size)
                             * math.sqrt((new_val - old_val)*(new_val - old_val))
                                 )

        # Обновление значения буфера
        self.buffer[self.buffer_count].mag.f.value = new_val
        self.buffer_count = (self.buffer_count + 1)  # Обновление счетчика

        # Проверка полного заполнения буфера
        if self.buffer_count == self.buffer_size:
            self.buffer_count = 0  # Начинаем заново заполнять буфер
