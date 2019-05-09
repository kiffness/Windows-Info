import db
import subprocess
from objects import Computer

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
        ram_capacity = f.readline()
        ram_slots = f.readline()
        
        print("-" * 130)
        line_format = "{:15s} {:15s} {:15s} {:40s} {:30s} {:5s}"
        print(line_format.format("Name", "Username", "Windows", "cpu", "ram_capacity", "ram_slots"))
        print("-" * 130)
        print(line_format.format(name.rstrip(), username.rstrip(), windows.rstrip(), cpu.rstrip(), ram_capacity.rstrip(), ram_slots.rstrip()))
        print("-" * 130)
        
        
def add_computer():
    with open (r'f:\Windows_10_Refresh\Powershell\SysConfig.txt', 'r') as f: # Change to path where your txt file will be
        name = f.readline()
        username = f.readline()
        windows = f.readline()
        cpu = f.readline()
        ram_capacity = f.readline()
        ram_slots = f.readline()
        
        computer = Computer(name=name, username=username, windows=windows, cpu=cpu, ram_capacity=ram_capacity, ram_slots=ram_slots)
        db.insert_data(computer)
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