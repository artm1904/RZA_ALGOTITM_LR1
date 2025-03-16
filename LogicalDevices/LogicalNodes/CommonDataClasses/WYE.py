from dataclasses import dataclass, field

from LogicalDevices.LogicalNodes.CommonDataClasses.CMV import CMV


@dataclass
class WYE:
    phsA: CMV = field(default_factory=CMV)        # phSA: CMV
    phsB: CMV = field(default_factory=CMV)         # phSB: CMV
    phsC: CMV = field(default_factory=CMV)      # phSC: CMV
    neut: CMV = field(default_factory=CMV)        # neut: CMV