import math
import macro
import keyboard
import time

class Coordinates:
    def __init__(self, x, z, dist, angle):
        self.x = x
        self.z = z
        self.dist = dist
        self.angle = angle

blindLocations = [
    Coordinates("256.5", "110.5", 0, 0),
    Coordinates("-211.375", "158.5", 0, 0),
    Coordinates("-25.375", "-211.375", 0, 0),
    Coordinates("318.5", "514.5", 0, 0),
    Coordinates("332.5", "-617.375", 0, 0),
    Coordinates("-377.375", "-609.375", 0, 0),
    Coordinates("-289.375", "540.5", 0, 0),
    Coordinates("710.5", "-21.375", 0, 0),
    Coordinates("-621.375", "18.5", 0, 0)
]

def getCoords():
    time.sleep(1)
    clipboard = macro.Clipboard.get_clipboard()
    clipboardList = clipboard.split()
    x = float(clipboardList[6])
    z = float(clipboardList[8])

    for location in blindLocations:
        xDist = float(location.x) - x
        zDist = float(location.z) - z

        location.dist = round(math.sqrt(xDist*xDist + zDist*zDist))

        if xDist < float(0) < zDist:
            location.angle = round(math.atan(abs(xDist/zDist)) * 180 / math.pi)
        elif xDist > float(0) and zDist > float(0):
            location.angle = -round(math.atan(abs(xDist / zDist)) * 180 / math.pi)
        elif zDist < float(0) < xDist:
            location.angle = -180 + round(math.atan(abs(xDist / zDist)) * 180 / math.pi)
        elif xDist < float(0) and zDist < float(0):
            location.angle = 180 - round(math.atan(abs(xDist / zDist)) * 180 / math.pi)

    def getDist(blindLocation):
        return blindLocation[2]

    strongholds = sorted(blindLocations, key=lambda x: x.dist)

    stronghold = strongholds[0]

    print("("+ stronghold.x + ", " + stronghold.z + ")")
    print(str(stronghold.angle) + "°, " + str(stronghold.dist) + " blocks away\n")

keyboard.add_hotkey("f3+c", getCoords)
keyboard.wait()