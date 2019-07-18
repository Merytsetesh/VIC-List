# A generic character stream for reading files.
#
#
# Copyright (C) 2019 Simon Ellis.

class CharStream:
    def __init__(self):
        self.Filename = None
        self.Source = None
        self.Pos = -1

    def Load(self, fname):
        self.Filename = fname
        with open(fname, 'rb') as f:
            self.Source = f.read()
        f.close()
        self.Pos = 0

    def Clear(self):
        del self.Source
        self.Source = None
        self.Pos = -1

    def EOF(self):
        return self.Pos == -1 or self.Pos == len(self.Source)

    def GetNextChar(self):
        if not self.EOF():
            ch = self.Source[self.Pos]
            self.Pos += 1
            return int(ch)
        return -1

    def PushBack(self):
        if self.Pos > 0:
            self.Pos -= 1

    def GetPos(self):
        return self.Pos

    def SetPos(self, pos):
        if self.Source is not None and (0 <= pos < len(self.Source)):
            self.Pos = pos
