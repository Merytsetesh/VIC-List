# Classes for the VIC-List programs. Perhaps ironically, the larger of the two is the one to manage
# two-byte words, to make sure that they are stored correctly and their values are easily output.
#
# Programs are stored as dictionaries: key is line number, value is a list of VIC-List tokens.
#
#
# Copyright (C) 2019 Merytsetesh.


class Word:
    def __init__(self, value_or_low=-1, high=0):
        self.LowByte = -1
        self.HighByte = 0
        if value_or_low > -1:
            if 0 < high < 256 and 0 < value_or_low < 256:
                self.SetPair(value_or_low, high)
            else:
                self.SetValue(value_or_low)

    def SetValue(self, value):
        self.LowByte = value % 256
        self.HighByte = value // 256

    def SetPair(self, low, high):
        self.LowByte = low
        self.HighByte = high

    def GetValue(self):
        return (self.HighByte * 256) + self.LowByte

    def GetPair(self):
        return (self.LowByte, self.HighByte)


class Program:
    def __init__(self):
        self.Code = {}
        self.BasicStart = Word()
