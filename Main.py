from matplotlib import pyplot as plt
import comtrade

from LogicalDevices.LD_Ctrl import LDCtrl
from LogicalDevices.LD_PROT import LDProt_MTZ
from LogicalDevices.LogicalNodes.CommonDataClasses.ASG import ASG

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.AnalogueValue import AnalogueValue

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.INT32 import INT32
from LogicalDevices.LogicalNodes.CommonDataClasses.ING import ING

from Pasring_Comtrade import Pasring_Comtrade
from LogicalDevices.LD_Meas import LDMeasurement_TCTR_Fur


# Создание класс-парсинга 3 архитектуры входных данных от модели ЭЭС
parsr_3 = Pasring_Comtrade()
parsr_3.parsing()

ld_meas_ART = LDMeasurement_TCTR_Fur()

ld_ctrl_ART = LDCtrl()

ld_prot_ART = LDProt_MTZ()

# Задаем уставки по току и времени для ступеней МТЗ для LDProt_MTZ
mtz1_I = AnalogueValue()
mtz1_I.f.value = 3000  # Или FLOAT(3000), в зависимости от типа
ags1 = ASG()
ags1.setMag = mtz1_I
ld_prot_ART.StrVal_stg1 = ags1

mtz2_I = AnalogueValue()
mtz2_I.f.value = 2000
ags2 = ASG()
ags2.setMag = mtz2_I
ld_prot_ART.StrVal_stg2 = ags2

mtz3_I = AnalogueValue()
mtz3_I.f.value = 1000
ags3 = ASG()
ags3.setMag = mtz3_I
ld_prot_ART.StrVal_stg3 = ags3

mtz1_t = ING()
mtz1_t.setVal = INT32(100)
ld_prot_ART.OPDlTmms_stg1 = mtz1_t

mtz2_t = ING()
mtz2_t.setVal = INT32(200)
ld_prot_ART.OPDlTmms_stg2 = mtz2_t

mtz3_t = ING()
mtz3_t.setVal = INT32(500)
ld_prot_ART.OPDlTmms_stg3 = mtz3_t





ia_chanel = []
ib_chanel = []
ic_chanel = []


mtz_1 = [0.0] * 2000  # Инициализируем список mtz_1
mtz_2 = [0.0] * 2000  # Инициализируем список mtz_2
mtz_3 = [0.0] * 2000  # Инициализируем список mtz_3


op_chanel = []

str_chanel = []


rec = comtrade.load(r"C:\ForMe\Proger\Python\PycharmProjects\RZA_ALGOTITM_LR1\Osc_1\Start_Line\PhB20.cfg", r"C:\ForMe\Proger\Python\PycharmProjects\RZA_ALGOTITM_LR1\Osc_1\Start_Line\PhB20.dat")

for i in range(2000):
    print(i)
    parsr_3.process()

    mtz_1[i] = mtz1_I.f.value
    mtz_2[i] = mtz2_I.f.value
    mtz_3[i] = mtz3_I.f.value

    # Получаем значения из parsr_3 и присваиваем их ld_meas_ART
    ld_meas_ART.CurrentA.instMag.f.value = parsr_3.CurrentA.instMag.f.value
    ld_meas_ART.CurrentB.instMag.f.value = parsr_3.CurrentB.instMag.f.value
    ld_meas_ART.CurrentC.instMag.f.value = parsr_3.CurrentC.instMag.f.value



    ld_meas_ART.process()

    ia_chanel.append(ld_meas_ART.A.phsA.cVal.mag.f.value)
    ib_chanel.append(ld_meas_ART.A.phsB.cVal.mag.f.value)
    ic_chanel.append(ld_meas_ART.A.phsC.cVal.mag.f.value)

    # Задаем связи между LD (выход LDMeasurement - вход LDProt_MTZ)
    ld_prot_ART.A = ld_meas_ART.A


    ld_prot_ART.process()

    if ld_prot_ART.Op.general.value == True:
        print("Gitler")
        op_chanel.append(1)
    else:
        op_chanel.append(0)

    print(ld_prot_ART.Op.general.value)


    # str_chanel.append(ld_prot_ART.S)  # TODO добавить параметр выхода STR

    # Задаем связи между LD (выход LDProt_MTZ - вход LDCtrl)
    ld_ctrl_ART.Op = ld_prot_ART.Op

    ld_ctrl_ART.process()

# for i in range(2000):
#     print(op_chanel[i])


# Plotting
plt.figure()
plt.plot(rec.time, ia_chanel, label="ia_chanel")
plt.plot(rec.time,mtz_1 , label="mtz1_I")
plt.plot(rec.time, ib_chanel, label="ib_chanel")
plt.plot(rec.time,mtz_2 , label="mtz2_I")
plt.plot(rec.time, ic_chanel, label="ic_chanel")
plt.plot(rec.time,mtz_3 , label="mtz3_I")


# Labels and title
plt.xlabel("Time")
plt.ylabel("Current")  #
plt.title("Current vs. Time")
plt.legend()
plt.savefig("my_plot_furier.png")



# Plotting
plt.figure()
plt.plot(rec.time, op_chanel, label="Op Chanel")
# Labels and title
plt.xlabel("Time")
plt.ylabel("Logical Signal PTOC")
plt.title("Logical signal vs. Time")
plt.legend()
plt.savefig("my_plot_op_channel.png")