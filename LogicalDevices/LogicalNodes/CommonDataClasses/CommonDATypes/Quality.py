from dataclasses import dataclass, field

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Enum.QualEnum import QualEnum


@dataclass
class Quality:
    """
    Представляет качество данных.
    """
    validity: QualEnum = field(default=QualEnum.GOOD)  # Значение QualEnum
