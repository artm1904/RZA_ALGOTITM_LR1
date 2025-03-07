from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.INT32 import INT32


@dataclass
class ING:
    """
    Представляет установку целочисленного состояния.
    """
    setVal: Optional[INT32] = field(default_factory=INT32)  # stVal: Значение статуса (булево)