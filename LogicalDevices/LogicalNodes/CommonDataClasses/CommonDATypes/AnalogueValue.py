from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.FLOAT32 import FLOAT32
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.INT32 import INT32


@dataclass
class AnalogueValue:
    """
    Представляет аналоговое значение, содержащее INT32 и FLOAT32 представления.
    """
    i: Optional[INT32] = field(init=False)    # i: INT32
    f: Optional[FLOAT32] = field(init=False)  # f: FLOAT32

    def __post_init__(self):
        self.i = INT32(0)
        self.f = FLOAT32(0.0)