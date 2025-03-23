import csv
import matplotlib.pyplot as plt

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
class Pasring_CSV():

    time_stamp: int = 2
    CurrentA: Optional[FLOAT32] = None  # Тип должен быть FLOAT32, а не SAV.  Мы берем FLOAT32 из AnalogueValue
    CurrentB: Optional[FLOAT32] = None
    CurrentC: Optional[FLOAT32] = None
    time = []
    ia_chanel = []
    ib_chanel = []
    ic_chanel = []
    # File path
    file_path = "C:\ForMe\Proger\Python\PycharmProjects\RZA_ALGOTITM_LR1\Osc_1\Start_Line\PhB20.csv"

    def parsing(self):
        with open(self.file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row

            for row in reader:
                try:
                    # Convert data to numeric types (float)
                    self.time.append(float(row[0]))
                    self.ia_chanel.append(float(row[1]))
                    self.ib_chanel.append(float(row[2]))
                    self.ic_chanel.append(float(row[3]))
                except ValueError:
                    print(f"Skipping row due to invalid {row}")  # Handle potential errors

        # Plotting
        plt.figure()
        plt.plot(self.time, self.ia_chanel, label="ia_chanel")
        plt.plot(self.time, self.ib_chanel, label="ib_chanel")
        plt.plot(self.time, self.ic_chanel, label="ic_chanel")

        # Labels and title
        plt.xlabel("Time")
        plt.ylabel("Current")  # Or whatever the units are
        plt.title("Current vs. Time")

        # Legend
        plt.legend()

        # Save the plot
        plt.savefig("my_plot_csv.png")

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