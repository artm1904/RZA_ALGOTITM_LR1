from dataclasses import dataclass, field
from typing import Optional

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.AnalogueValue import AnalogueValue


@dataclass
class ASG:
    setMag: AnalogueValue = field(default_factory=AnalogueValue)  # instMag: Мгновенная величина