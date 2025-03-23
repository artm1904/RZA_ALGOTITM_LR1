# LogicalDevices\LogicalNodes\Fourier.py
import math
from dataclasses import dataclass, field

from LogicalDevices.LogicalNodes.CommonDataClasses.MV import MV
from LogicalDevices.LogicalNodes.CommonDataClasses.SAV import SAV

@dataclass
class Fourier:
    buffer_size: int
    buffer: list[MV] = field(init=False)
    buffer_count: int = 0
    summ_val_re: float = 0.0
    summ_val_im: float = 0.0
    frequency: float = 50.0
    sampl_step: float = 0.02 / 20

    def __post_init__(self):
        self.buffer = [MV() for _ in range(self.buffer_size)]

    def process(self, measured_value: SAV) -> tuple[float, float]:  # Возвращаем действительную и мнимую часть
        """
        Processes a measured value using the Fourier transform.

        Args:
            measured_value: The measured value (MV).

        Returns:
            A tuple containing the magnitude and angle of the complex measurement value.
        """
        new_val = measured_value.instMag.f.value  # Получаем текущее значение

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
        self.buffer[self.buffer_count].mag.f.value = new_val
        self.buffer_count = (self.buffer_count + 1) % self.buffer_size

        magnitude = math.sqrt((self.summ_val_re ** 2 + self.summ_val_im ** 2) / 2.0)
        angle = math.atan2(self.summ_val_im, self.summ_val_re) * (180 / math.pi)

        return magnitude, angle