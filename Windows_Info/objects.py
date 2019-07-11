from datetime import datetime
import os

class Computer:
    """Builds Computer Object Params are (computerid, name, username, windows, cpu)"""
    def __init__(self, computerid=0, name=None, username=None, windows=None, cpu=None,
                 totalslots=0, currentamount=None, lastlogon=None, ipaddress=None):
        self.computerid = computerid
        self.name = name
        self.username = username
        self.windows = windows
        self.cpu = cpu
        self.currentamount = currentamount
        self.totalslots = totalslots
        self.lastlogon = lastlogon
        self.ipaddress = ipaddress

class LastLogon:
    """Builds Object for ipaddress database. Params are (lastlogon, ipaddress)"""
    def __init__(self, lastlogon=None, ipaddress=None):
        self.lastlogon = lastlogon
        self.ipaddress = ipaddress

class Date:
    """
    Adds date based on what file it is.
    Params::
    filename - The Full path to file oncluding file name
    """


    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.path = "F:\Windows_10_Refresh\Logs\\"
        self.date = str(datetime.now().strftime("%Y-%m-%d %H-%M-%S"))

    def format_date(self):
        temp_list = []
        new = self.path + self.folder + "\\" + self.date + ".txt"
        old = self.path + self.filename + ".txt"
        self.rename(old, new)



    def rename(self, old, new):
        os.rename(old, new)

class Name:
    def __init__(self, name=None):
        self.name = name
