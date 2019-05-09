import db
import subprocess
from objects import Computer, RamInfo

def display_menu():
    print("Windows 10 Refresh Application")
    print(" ")
    print("COMMAND MENU")
    print("-" * 95)
    print("run - Run Powershell Script")
    print("read - Read text file")
    print("add - Add data to database")
    print("exit - Exit the Program.")
    print("-" * 95)


def powershell():
    computer_name = input("Please Enter Computer Name: ")
    PowerShellPath = r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
    PowerShellCmd = "F:\\Windows_10_Refresh\\Powershell\\Get-SysInfo.ps1" # Change Path here to where your powershell script is saved

    p = subprocess.Popen([PowerShellPath, '-ExecutionPolicy', 'Unrestricted', PowerShellCmd, computer_name])
    
    print("Gathering Information")
    p.communicate()
    
def read_text():
    with open (r'f:\Windows_10_Refresh\Powershell\SysConfig.txt', 'r') as f:
        name = f.readline()
        username = f.readline()
        windows = f.readline()
        cpu = f.readline()
        manufacturer = f.readline()
        speed = f.readline()
        currentamount = f.readline()
        slots = f.readline()
        
        print("-" * 130)
        line_format1 = "{:15s} {:15s} {:15s} {:40s}"
        line_format2 = "{:15} {:5s} {:15s} {:5}"
        print(line_format1.format("Name", "Username", "Windows", "cpu"))
        print(line_format1.format(name.rstrip(), username.rstrip(), windows.rstrip(), cpu.rstrip()))
        print("-" * 130)
        print(line_format2.format("manufacturer", "speed", "currentamount", "slots"))
        print(line_format2.format(manufacturer.rstrip(), speed.rstrip(), currentamount.rstrip(), slots.rstrip()))
        print("-" * 130)
        
        
def add_computer():
    with open (r'f:\Windows_10_Refresh\Powershell\SysConfig.txt', 'r') as f: # Change to path where your txt file will be
        name = f.readline()
        username = f.readline()
        windows = f.readline()
        cpu = f.readline()
        manufacturer = f.readline()
        speed = f.readline()
        currentamount = f.readline()
        totalslots = f.readline()
        
        computer = Computer(name=name, username=username, windows=windows, cpu=cpu)
        raminfo = RamInfo(manufacturer=manufacturer, currentamount=currentamount, totalslots=totalslots, speed=speed)
        db.insert_data(computer, raminfo)
        print(username.rstrip() + "'s pc was added to the database succesfully")
        
def main():
    db.connect()
    display_menu()
    while True:
        command = input("Enter command: ")
        if command == "run":
            powershell()
        elif command == "read":
            read_text()
        elif command == "add":
            add_computer()
        elif command == "exit":
            break
        else:
            print("Not a valid command please try again")
            display_menu()
    db.close()
    print("The application has closed succesfully")
    
if __name__ == "__main__":
    main()