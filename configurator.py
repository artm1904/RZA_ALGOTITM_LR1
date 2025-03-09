from LogicalDevices.LogicalNodes.CommonDataClasses.ACD import ACD
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.BasicTypes.BOOLEAN import BOOLEAN
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Enum.dirEnum import DirEnum
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.Quality import Quality
from LogicalDevices.LogicalNodes.CommonDataClasses.CommonDATypes.TimeStamp import TimeStamp

if __name__ == "__main__":
    acd_экземпляр = ACD(
        general=BOOLEAN(True),
        phsA=BOOLEAN(True),
        phsB=BOOLEAN(True),
        phsC=BOOLEAN(True),
        neut=BOOLEAN(False),
        dirGeneral=DirEnum.UNKNOWN,
        dirPhsA=DirEnum.UNKNOWN,
        dirPhsB=DirEnum.UNKNOWN,
        dirPhsC=DirEnum.UNKNOWN,
        dirNeut=DirEnum.UNKNOWN,
        q=Quality(),
        t=TimeStamp()
    )

    print(acd_экземпляр)
