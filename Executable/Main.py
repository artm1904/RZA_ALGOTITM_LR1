from Configuration.Configurator import LB1
from LogicalDevices.LD_Meas import LDMeasurement_TCTR_RMS, LDMeasurement_TCTR_Fur, LDMeasurement_LSVS_Fur
from LogicalDevices.Parser import Pasring_CSV, Pasring_Comtrade

# Установка пути до осциллограмм - ПУТЬ ОТНОСИТЕЛЬНЫЙ!!!
cfgFilePath = r"D:\OneDrive\Study\AlgorithmsRZA\RZA_ALGOTITM_LR1\Osc_1\End_Line\PhC20.cfg"
datFilePath = r"D:\OneDrive\Study\AlgorithmsRZA\RZA_ALGOTITM_LR1\Osc_1\End_Line\PhC20.dat"
csvFilePath = r"D:\OneDrive\Study\AlgorithmsRZA\RZA_ALGOTITM_LR1\Osc_1\End_Line\PhC20.csv"

mtz_Art = LB1(
    cfgFilePath=cfgFilePath,
    datFilePath=datFilePath,
    csvFilePath=csvFilePath,
    stg1Value=2000, stg2Value=500, stg3Value=500,
    stg1Time=100, stg2Time=750, stg3Time=750,
    ldMeas=LDMeasurement_TCTR_Fur(),
    parser=Pasring_CSV()
)

mtz_Den = LB1(
    cfgFilePath=cfgFilePath,
    datFilePath=datFilePath,
    csvFilePath=csvFilePath,
    stg1Value=2000, stg2Value=500, stg3Value=500,
    stg1Time=100, stg2Time=750, stg3Time=750,
    ldMeas=LDMeasurement_LSVS_Fur(),
    parser=Pasring_Comtrade()
)

mtz_Alx = LB1(
    cfgFilePath=cfgFilePath,
    datFilePath=datFilePath,
    csvFilePath=csvFilePath,
    stg1Value=2000, stg2Value=1000, stg3Value=1000,
    stg1Time=100, stg2Time=500, stg3Time=500,
    ldMeas=LDMeasurement_TCTR_RMS(),
    parser=Pasring_CSV()
)



# ДЛЯ РАБОТЫ РАСКОММЕНТИРОВАТЬ
# mtz_Art.process()
mtz_Den.process()
# mtz_Alx.process()
