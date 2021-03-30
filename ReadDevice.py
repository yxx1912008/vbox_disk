import csv
import os

from Devices import *


def readDevices():
    res = os.popen('wmic /output:devices.csv diskdrive list brief /format:csv')
    res.close()
    reader = csv.reader(open('devices.csv', encoding='UTF-16LE'))
    startIndex = 0
    devices = list()
    for tmp in reader:
        startIndex += 1
        if startIndex > 2:
            size = int(int(tmp[5]) / 1024 / 1024 / 1024)
            device = Devices(tmp[1], tmp[2], tmp[3], str(size) + 'G')
            devices.append(device)

    return devices


if __name__ == '__main__':
    devices = readDevices()
    for tmp in devices:
        print(tmp.caption, tmp.deviceID, tmp.partitions, tmp.size)
