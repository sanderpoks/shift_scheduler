from enum import Enum

class ShiftTypes(Enum):
    EMPTY = "empty"
    WORK = "work"
    VACATION = "vacation"
    SICK = "sick"
    TRAINING = "training"


class Shift():
    def __init__(self, shifttype=ShiftTypes.EMPTY, day=None, night=None, descriptor=None):
        self.day = day
        self.night = night
        self.descriptor = descriptor