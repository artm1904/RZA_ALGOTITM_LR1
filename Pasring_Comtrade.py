from dataclasses import dataclass, field
from typing import Optional

import matplotlib.pyplot as plt
import comtrade

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.AnalogueValue import AnalogueValue
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Quality import Quality
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeStamp import TimeStamp

from LogicalDevices.LogicalNodes.CommonDataClasses.SAV import SAV
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.FLOAT32 import FLOAT32


@dataclass
class Pasring_Comtrade():

    time_stamp: int = 2
    CurrentA: Optional[FLOAT32] = None  # Тип должен быть FLOAT32, а не SAV.  Мы берем FLOAT32 из AnalogueValue
    CurrentB: Optional[FLOAT32] = None
    CurrentC: Optional[FLOAT32] = None
    ia_chanel = []
    ib_chanel = []
    ic_chanel = []

    def parsing(self):
        rec = comtrade.load("C:\ForMe\Proger\Python\PycharmProjects\RZA_ALGOTITM_LR1\Osc_1\Start_Line\PhB20.cfg", "C:\ForMe\Proger\Python\PycharmProjects\RZA_ALGOTITM_LR1\Osc_1\Start_Line\PhB20.dat")
        print("Trigger time = {}s".format(rec.trigger_time))
        self.ia_chanel = rec.analog[0]
        self.ib_chanel = rec.analog[1]
        self.ic_chanel = rec.analog[2]

        plt.figure()
        plt.plot(rec.time, rec.analog[0])
        plt.plot(rec.time, rec.analog[1])
        plt.plot(rec.time, rec.analog[2])
        plt.legend([rec.analog_channel_ids[0], rec.analog_channel_ids[1], rec.analog_channel_ids[2]])
        plt.savefig("my_plot_comtrade.png")

    def process(self):
        try:
            # Создаем AnalogueValue для каждого канала, используя FLOAT32 для правильной инициализации
            analogue_a = AnalogueValue(f=FLOAT32(self.ia_chanel[self.time_stamp]))
            analogue_b = AnalogueValue(f=FLOAT32(self.ib_chanel[self.time_stamp]))
            analogue_c = AnalogueValue(f=FLOAT32(self.ic_chanel[self.time_stamp]))

            # Создаем SAV объекты, используя AnalogueValue
            sav_a = SAV(instMag=analogue_a, q=Quality(), t=TimeStamp())
            sav_b = SAV(instMag=analogue_b, q=Quality(), t=TimeStamp())
            sav_c = SAV(instMag=analogue_c, q=Quality(), t=TimeStamp())

            # Доступ к значениям FLOAT32 из SAV
            self.CurrentA = sav_a.instMag.f  # Access the FLOAT32 value
            self.CurrentB = sav_b.instMag.f
            self.CurrentC = sav_c.instMag.f

            return self.CurrentA, self.CurrentB, self.CurrentC

        except IndexError:
            print(f"IndexError: time_stamp {self.time_stamp} is out of range.")
            return None, None, None
        except TypeError as e:
            print(f"TypeError: {e}")
            return None, None, None
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")
            return None, None, None