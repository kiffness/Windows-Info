class Computer:
    def __init__(self, computerid=0, name=None, username=None, windows=None, cpu=None, ram_capacity=None, ram_slots=0 ):
        self.computerid = computerid
        self.name = name
        self.username = username
        self.windows = windows
        self.cpu = cpu
        self.ram_capacity = ram_capacity
        self.ram_slots = ram_slots