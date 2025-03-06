from dataclasses import dataclass, field

from Artem_Class.AnalogueValue import AnalogueValue
from Artem_Class.Quality import Quality
from Artem_Class.TimeStamp import TimeStamp


@dataclass
class SAV:
    """
    Представляет Single Analogue Value (Единичное аналоговое значение).
    """
    instMag: AnalogueValue = field(default_factory=AnalogueValue)  # instMag: Мгновенная величина
    q: Quality = field(default_factory=Quality)                             # q: Качество
    t: TimeStamp = field(default_factory=TimeStamp)                           # t: Временная метка