import subprocess
import filecmp

import db
from objects import Computer



def get_computername():
    with open (r'f:\Windows_10_Refresh\Powershell\NoBOM.txt', 'r') as f:
        
        x = f.read().splitlines()
        
        return x
          

def read_text():
    with open (r'f:\Windows_10_Refresh\Powershell\SysConfig.txt', 'r') as f:
     
    
        text = f.read().splitlines()
        
        print("-" * 130)
        line_format1 = "{:15s} {:15s} {:15s} {:40s}"
        line_format2 = "{:50s} {:5s}"
        print(line_format1.format("Name", "Username", "Windows", "cpu"))
        print(line_format1.format(text[0], text[1], text[2], text[3]))
        print("-" * 130)
        print(line_format2.format("currentamount", "slots"))
        print(line_format2.format(text[4], text[5]))
        print("-" * 130)
        
def add_computer():
    
    file1 = 'f:\Windows_10_Refresh\Powershell\SysConfig.txt'
    file2 = 'f:\Windows_10_Refresh\Powershell\SysConfig2.txt'
    with open (file1, 'r') as f1, open(file2, 'r+') as f2:
     
        if filecmp.cmp(file1, file2):
            return ""
        else:
            text = f1.read().splitlines()
            name = text[0]
            username = text[1]
            windows = text[2]
            cpu = text[3]
            currentamount = text[4] 
            totalslots = text[5]
            
            computer = Computer(name=name, username=username, windows=windows, cpu=cpu,
                                currentamount=currentamount, totalslots=totalslots)
            db.insert_data(computer)
            
            for line in text:
                f2.write(line + "\n")
                
                
def powershell():
    computer_name = get_computername()
    
    for computer in computer_name:
        print("#" * 95)
        print(f"Trying to reach " + computer)
        print(" ")
        PowerShellPath = r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
        PowerShellCmd = "F:\\Windows_10_Refresh\\Powershell\\Get-SysInfo.ps1" # Change Path here to where your powershell script is saved
 
        p = subprocess.Popen([PowerShellPath, '-ExecutionPolicy', 'Unrestricted', PowerShellCmd, computer])
     
        print("Gathering Information")
        p.communicate()
        
        
        print(" ")
        add_computer()
    