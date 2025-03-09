import math
from dataclasses import field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CMV import CMV
from LogicalDevices.LogicalNodes.CommonDataClasses.MV import MV
from LogicalDevices.LogicalNodes.Filter import Filter


class Fourier(Filter):
    buffer_size: int  #Размер буфера
    buffer: list[MV] = field(init=False)  #Создание буфера нужного размера
    buffer_count: int  #Счетчик выборки
    summ_val_re: float  #Действительное значение
    summ_val_im: float  #Мнимое значение
    frequency: float  #Частота
    sampl_step: float  #Шаг дискретизации

    def __init__(self, buffer_size: int):
        self.buffer_size = buffer_size

    def __post_init__(self):
        """
        Initializes the Fourier filter.  This runs after the dataclass is initialized.
        """

        self.buffer = [MV() for _ in range(self.buffer_size)]  #Создание буфера нужного размера

        self.buffer_count = 0  # Счетчик выборки
        self.summ_val_re = 0.0  # Действительное значение
        self.summ_val_im= 0.0  # Мнимое значение
        self.frequency = 50.0  # Частота
        self.sampl_step = 0.02 / self.buffer_size  # Шаг дискретизации

        # Заполнение буфера нулями (не нужно, т.к. MV по умолчанию создается с нулями)
        # for i in range(self.buffer_size.value):
        #     self.buffer[i].inst_mag.float_val.value = 0.0  # Assuming inst_mag and float_val exist.

    def process(self, measured_value: MV, complex_measurement_value: CMV):
        """
        Processes a measured value using the Fourier transform.

        Args:
            measured_value: The measured value (MV).
            complex_measurement_value: The complex measurement value (CMV) to update.
        """

        # Новое измеренное значение
        new_val = measured_value.mag.f.value

        # Старое измеренное значение, хранящееся в буфере
        old_val = self.buffer[self.buffer_count].mag.f.value

        # Расчет действительного и мнимого значения
        self.summ_val_re = (
                self.summ_val_re
                + (new_val - old_val)
                * math.sin(
            2 * math.pi * self.frequency * self.buffer_count * self.sampl_step
        )
                * (2.0 / self.buffer_size)
        )
        self.summ_val_im = (
                self.summ_val_im
                + (new_val - old_val)
                * math.cos(
            2 * math.pi * self.frequency * self.buffer_count * self.sampl_step
        )
                * (2.0 / self.buffer_size)
        )

        # Расчет величины и угла измеряемого вектора
        complex_measurement_value.cVal.mag.f.value = math.sqrt(
            (self.summ_val_re ** 2 + self.summ_val_im ** 2) / 2.0
        )
        complex_measurement_value.cVal.ang.f.value = (
                math.atan2(self.summ_val_im, self.summ_val_re) * (180 / math.pi)  # Use atan2
        )

        # Обновление значения буфера
        self.buffer[self.buffer_count].mag.f.value = new_val
        self.buffer_count = (self.buffer_count + 1)  # Обновление счетчика

        # Проверка полного заполнения буфера
        if self.buffer_count == self.buffer_size:
            self.buffer_count = 0  # Начинаем заново заполнять буфер
