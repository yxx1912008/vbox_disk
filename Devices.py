# 读取的设备类
class Devices:
    caption = ""
    deviceID = ""
    partitions = 0
    size = ""

    def __init__(self, caption, deviceID, partitions, size):
        self.caption = caption
        self.deviceID = deviceID
        self.partitions = partitions
        self.size = size
