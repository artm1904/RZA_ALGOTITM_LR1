from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CompositeCommonDataClasses.SimpleCommonDataClasses.CommonDATypes.BasicTypes.FLOAT32 import \
    FLOAT32
from LogicalDevices.LogicalNodes.CompositeCommonDataClasses.SimpleCommonDataClasses.CommonDATypes.BasicTypes.INT32 import \
    INT32


@dataclass
class AnalogueValue:
    """
    Представляет аналоговое значение, содержащее INT32 и FLOAT32 представления.
    """
    i: Optional[INT32] = field(default_factory=INT32)    # i: INT32
    f: Optional[FLOAT32] = field(default_factory=INT32)  # f: FLOAT32