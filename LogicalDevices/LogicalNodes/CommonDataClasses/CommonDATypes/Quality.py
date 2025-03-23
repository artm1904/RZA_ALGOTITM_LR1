from dataclasses import dataclass, field

from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Enum.QualEnum import QualEnum

@dataclass
class Quality:
    """
    Представляет качество данных.
    """
    validity: QualEnum = field(init=False)  # Значение QualEnum

    def __post_init__(self):
        self.validity = QualEnum.GOOD