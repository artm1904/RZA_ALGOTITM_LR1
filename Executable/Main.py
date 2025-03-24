from Configuration.Configurator import LB1
from LogicalDevices.LD_Meas import LDMeasurement_TCTR_RMS, LDMeasurement_TCTR_Fur, LDMeasurement_LSVS_Fur
from LogicalDevices.Parser import Pasring_CSV, Pasring_Comtrade

# Установка пути до осциллограмм - ПУТЬ ОТНОСИТЕЛЬНЫЙ!!!
cfgFilePath = r"Osc_1\Start_Line\PhB20.cfg"
datFilePath = r"Osc_1\Start_Line\PhB20.dat"
csvFilePath = r"Osc_1\Start_Line\PhB20.csv"

mtz_Art = LB1(
    cfgFilePath=cfgFilePath,
    datFilePath=datFilePath,
    csvFilePath=csvFilePath,
    stg1Value=100, stg2Value=100, stg3Value=100,
    stg1Time=15, stg2Time=15, stg3Time=15,
    ldMeas=LDMeasurement_TCTR_Fur(),
    parser=Pasring_CSV()
)

mtz_Den = LB1(
    cfgFilePath=cfgFilePath,
    datFilePath=datFilePath,
    csvFilePath=csvFilePath,
    stg1Value=100, stg2Value=100, stg3Value=100,
    stg1Time=15, stg2Time=15, stg3Time=15,
    ldMeas=LDMeasurement_LSVS_Fur(),
    parser=Pasring_Comtrade()
)

mtz_Alx = LB1(
    cfgFilePath=cfgFilePath,
    datFilePath=datFilePath,
    csvFilePath=csvFilePath,
    stg1Value=1000, stg2Value=2000, stg3Value=4000,
    stg1Time=700, stg2Time=700, stg3Time=700,
    ldMeas=LDMeasurement_TCTR_RMS(),
    parser=Pasring_CSV()
)



# ДЛЯ РАБОТЫ РАСКОММЕНТИРОВАТЬ
# mtz_Art.process()
# mtz_Den.process()
# mtz_Alx.process()
