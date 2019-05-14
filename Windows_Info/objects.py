class Computer:
    def __init__(self, computerid=0, name=None, username=None, windows=None, cpu=None,
                 totalslots=0, currentamount=None):
        self.computerid = computerid
        self.name = name
        self.username = username
        self.windows = windows
        self.cpu = cpu
        self.currentamount = currentamount
        self.totalslots = totalslots
        