# Pasring_Comtrade.py
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

    time_stamp: int = 0
    CurrentA: SAV = field(init=False)  # Тип должен быть SAV
    CurrentB: SAV = field(init=False)
    CurrentC: SAV = field(init=False)
    ia_chanel = []
    ib_chanel = []
    ic_chanel = []

    def __post_init__(self):
        self.CurrentA = SAV()
        self.CurrentB = SAV()
        self.CurrentC = SAV()


    def parsing(self):
        rec = comtrade.load(r"C:\ForMe\Proger\Python\PycharmProjects\RZA_ALGOTITM_LR1\Osc_1\Start_Line\PhB20.cfg", r"C:\ForMe\Proger\Python\PycharmProjects\RZA_ALGOTITM_LR1\Osc_1\Start_Line\PhB20.dat")
        #print("Trigger time = {}s".format(rec.trigger_time))
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
            analogue_a = AnalogueValue()
            analogue_a.f.value = self.ia_chanel[self.time_stamp] * 1000 #Умножаем на 1000
            analogue_b = AnalogueValue()
            analogue_b.f.value = self.ib_chanel[self.time_stamp] * 1000 #Умножаем на 1000
            analogue_c = AnalogueValue()
            analogue_c.f.value = self.ic_chanel[self.time_stamp] * 1000 #Умножаем на 1000


            # Создаем SAV объекты, используя AnalogueValue
            self.CurrentA.instMag = analogue_a
            self.CurrentB.instMag = analogue_b
            self.CurrentC.instMag = analogue_c


            self.time_stamp+=1
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