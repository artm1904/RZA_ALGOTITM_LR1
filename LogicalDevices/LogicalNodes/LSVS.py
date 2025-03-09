from LogicalDevices.LogicalNodes.LogicalNodeClass import LogicalNodeClass


class LSVS(LogicalNodeClass):



    def __init__(self):
        super().__init__()

    def process(self):
        pass

    Mod: Optional[INC] = field(default_factory=INC)


