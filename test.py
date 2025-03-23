from Pasring_CSV import Pasring_CSV
from Pasring_Comtrade import Pasring_Comtrade




# parsr= Pasring_Comtrade()
# parsr.parsing()
# a, b, c = Pasring_Comtrade.process(parsr)



parsr= Pasring_CSV()
parsr.parsing()

a, b, c = Pasring_CSV.process(parsr)


print(f"InputCurrentA: {a}")
print(f"InputCurrentB: {b}")
print(f"InputCurrentC: {c}")
