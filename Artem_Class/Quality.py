from dataclasses import dataclass, field
from typing import Optional

from Data_Class.Enum.QualEnum import QualEnum


@dataclass
class Quality:
    """
    Представляет качество данных.
    """
    validity: QualEnum = field(default=QualEnum.GOOD)  # Значение QualEnum
