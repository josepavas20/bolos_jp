from Tools.scripts.make_ctype import method


class Game:
    def __init__(self):

    def roll(self, pins):
        self.pins: int = pins

    def score(self)->int:
        pass


class Frame:

    def add_roll(self):
        self.pins: int
        pass
    def score(self)->int:
        pass

    def is_spare(self)->bool:
        #if roll == 2 and pins == 10:
            #is_spare = True
        pass

    def is_strike(self)->bool:
        #if roll == == 1 and pins == 10:
            #is_strike = True
        pass

class Normal_Frame(Frame):
    method(type)

class Ten_Frame(Frame):
    method(type)

class Roll:
    def pins(self):
        self.pins: int

    def __init__(self, pins: int):
        pass
