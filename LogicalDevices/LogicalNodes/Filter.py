from abc import ABC, abstractmethod

from LogicalDevices.LogicalNodes.CommonDataClasses.CMV import CMV
from LogicalDevices.LogicalNodes.CommonDataClasses.MV import MV


# Assuming you have these classes defined:
# from mv import MV
# from cmv import CMV

class Filter(ABC):
    """
    Abstract base class for filters.
    """

    @abstractmethod
    def process(self, measured_value: MV, complex_measurement_value: CMV):
        """
        Abstract method to process a measured value and update a complex measurement value.

        Args:
            measured_value: The measured value to process.
            complex_measurement_value: The complex measurement value to update.
        """
        pass  # Implementations should override this method