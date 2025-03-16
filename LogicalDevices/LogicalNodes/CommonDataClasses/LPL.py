from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.VISIBLE_STRING255 import VISIBLE_STRING255


@dataclass
class LPL:
    """
    Представляет целочисленное состояние.
    """
    vendor: Optional[VISIBLE_STRING255] = field(default_factory=VISIBLE_STRING255)
    swRev: Optional[VISIBLE_STRING255] = field(default_factory=VISIBLE_STRING255)
    d: Optional[VISIBLE_STRING255] = field(default_factory=VISIBLE_STRING255)