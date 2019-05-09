class Computer:
    def __init__(self, computerid=0, name=None, username=None, windows=None, cpu=None):
        self.computerid = computerid
        self.name = name
        self.username = username
        self.windows = windows
        self.cpu = cpu
        
class RamInfo:
    def __init__(self, ramid=0,manufacturer=None , totalslots=0, currentamount=None, speed=0):
        self.ramid = ramid
        self.manufacturer = manufacturer
        self.currentamount = currentamount
        self.totalslots = totalslots
        self.speed = speed
