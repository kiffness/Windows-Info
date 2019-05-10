import db
import misc_func
import subprocess
from objects import Computer, RamInfo

def main_menu():
    print("WELCOME TO WINDOWS 10 REFRESH PROGRAM!")
    print(" ")
    print("-" * 95)
    print("script - Powershell and Python functions")
    print("query - Database queries")
    print("exit - Exit the application")
    print("-" * 95)

def display_menu():
    print("Windows 10 Refresh Application")
    print(" ")
    print("COMMAND MENU")
    print("-" * 95)
    print("run - Run Powershell Script")
    print("read - Read text file")
    print("add - Add data to database")
    print("back - back to main menu")
    print("-" * 95)

def display_query_menu():
    print("QUERY MENU")
    print(" ")
    print("-" * 95)
    print("all - Shows all info")
    print("ram-a - Shows ram amount and slots")
    print("back - Back to main menu")
    print("-" * 95)

def powershell():
    computer_name = input("Please Enter Computer Name: ")
    PowerShellPath = r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
    PowerShellCmd = "F:\\Windows_10_Refresh\\Powershell\\Get-SysInfo.ps1" # Change Path here to where your powershell script is saved

    p = subprocess.Popen([PowerShellPath, '-ExecutionPolicy', 'Unrestricted', PowerShellCmd, computer_name])
    
    print("Gathering Information")
    p.communicate()
    
def read_text():
    text = misc_func.format_text()
        
    print("-" * 130)
    line_format1 = "{:15s} {:15s} {:15s} {:40s}"
    line_format2 = "{:15} {:5s} {:5s} {:15s} {:5}"
    print(line_format1.format("Name", "Username", "Windows", "cpu"))
    print(line_format1.format(text[0], text[1], text[2], text[3]))
    print("-" * 130)
    print(line_format2.format("manufacturer", "speed", "ddr", "currentamount", "slots"))
    print(line_format2.format(text[4], text[5], text[6], text[7], text[8]))
    print("-" * 130)
        
        
def add_computer():
    text = misc_func.format_text()
    name = text[0]
    username = text[1]
    windows = text[2]
    cpu = text[3]
    manufacturer = text[4] 
    speed = text[5]
    ddr = text[6]
    currentamount = text[7] 
    totalslots = text[8]
    
    computer = Computer(name=name, username=username, windows=windows, cpu=cpu)
    raminfo = RamInfo(manufacturer=manufacturer, currentamount=currentamount, totalslots=totalslots, speed=speed, ddr=ddr)
    db.insert_data(computer, raminfo)
    print(text[1] + "'s pc was added to the database succesfully")


def main():
    db.connect()
    main_menu()
    while True:
        command_main = input("Please choose a menu: ")
        if command_main == "script":
            display_menu()
            while True:
                command_script = input("Enter Command: ")
                if command_script == "run":
                    powershell()
                elif command_script == "read":
                    read_text()
                elif command_script == "add":
                    add_computer()
                elif command_script == "back":
                    main_menu()
                    break
                continue
        elif command_main == "query":
            display_query_menu()
            while True:
                command_query = input("Choose a query: ")
                if command_query == "all":
                    print("Filler Text")
                elif command_query == "ram-a":
                    print("filler text")
                elif command_query == "back":
                    main_menu()
                    break
                continue
        elif command_main == "exit":
            break
        else:
            print("Not a Valid Command")
            main_menu()
    db.close()
    print("The application has closed succesfully")
    
if __name__ == "__main__":
    main()