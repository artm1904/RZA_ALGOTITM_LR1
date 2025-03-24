import csv
from abc import abstractmethod, ABC
from dataclasses import dataclass, field

import comtrade
from matplotlib import pyplot as plt

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.AnalogueValue import AnalogueValue
from LogicalDevices.LogicalNodes.CommonDataClasses.SAV import SAV

@dataclass
class Parser(ABC):

    cfgFilePath: str
    datFilePath: str
    csvFilePath: str



    @abstractmethod
    def setPaths(self, cfgFilePath : str, datFilePath : str, csvFilePath : str):
        pass

    @abstractmethod
    def process(self):
        pass
    @abstractmethod
    def parsing(self):
        pass
    @abstractmethod
    def getTime(self):
        pass






@dataclass
class Pasring_Comtrade():

    time_stamp: int = 0
    CurrentA: SAV = field(init=False)  # Тип должен быть SAV
    CurrentB: SAV = field(init=False)
    CurrentC: SAV = field(init=False)
    ia_chanel = []
    ib_chanel = []
    ic_chanel = []
    time = []

    def __post_init__(self):
        self.CurrentA = SAV()
        self.CurrentB = SAV()
        self.CurrentC = SAV()


    def parsing(self):
        rec = comtrade.load(self.cfgFilePath, self.datFilePath)
        self.ia_chanel = rec.analog[0]
        self.ib_chanel = rec.analog[1]
        self.ic_chanel = rec.analog[2]
        self.time = rec.time

        # Plotting
        plt.figure()
        plt.plot(self.time, self.ia_chanel, label="ia")
        plt.plot(self.time, self.ib_chanel, label="ib")
        plt.plot(self.time, self.ic_chanel, label="ic")
        # Labels and title
        plt.xlabel("Time")
        plt.ylabel("Current")  # Or whatever the units are
        plt.title("Current vs. Time")
        plt.legend()
        plt.savefig("INPUT.png")

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

    def getTime(self):
        return self.time

    def setPaths(self, cfgFilePath : str, datFilePath : str, csvFilePath : str):
        self.cfgFilePath = cfgFilePath
        self.datFilePath = datFilePath
        self.csvFilePath = csvFilePath

@dataclass
class Pasring_CSV():

    time_stamp: int = 0
    CurrentA: SAV = field(init=False)  # Тип должен быть SAV
    CurrentB: SAV = field(init=False)
    CurrentC: SAV = field(init=False)
    time = []
    ia_chanel = []
    ib_chanel = []
    ic_chanel = []

    def __post_init__(self):
        self.CurrentA = SAV()  # Инициализируем как экземпляры SAV
        self.CurrentB = SAV()
        self.CurrentC = SAV()

    def parsing(self):
        with open(self.csvFilePath, 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row

            for row in reader:
                try:
                    # Convert data to numeric types (float)
                    self.time.append(float(row[0]))
                    self.ia_chanel.append(float(row[1])*1000)
                    self.ib_chanel.append(float(row[2])*1000)
                    self.ic_chanel.append(float(row[3])*1000)
                except ValueError:
                    print(f"Skipping row due to invalid {row}")  # Handle potential errors

        # Plotting
        plt.figure()
        plt.plot(self.time, self.ia_chanel, label="ia")
        plt.plot(self.time, self.ib_chanel, label="ib")
        plt.plot(self.time, self.ic_chanel, label="ic")
        # Labels and title
        plt.xlabel("Time")
        plt.ylabel("Current")  # Or whatever the units are
        plt.title("Current vs. Time")
        plt.legend()
        plt.savefig("INPUT.png")

    def process(self):
        try:
            # Создаем AnalogueValue для каждого канала, используя FLOAT32 для правильной инициализации
            analogue_a = AnalogueValue()
            analogue_a.f.value = self.ia_chanel[self.time_stamp]
            analogue_b = AnalogueValue()
            analogue_b.f.value = self.ib_chanel[self.time_stamp]
            analogue_c = AnalogueValue()
            analogue_c.f.value = self.ic_chanel[self.time_stamp]

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

    def getTime(self):
        return self.time

    def setPaths(self, cfgFilePath: str, datFilePath: str, csvFilePath: str):
        self.cfgFilePath = cfgFilePath
        self.datFilePath = datFilePath
        self.csvFilePath = csvFilePath