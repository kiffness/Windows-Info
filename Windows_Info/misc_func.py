import db
import subprocess
from objects import Computer
# This serves as a place to put all my misc functions
import subprocess


def get_computername():
    with open (r'f:\Windows_10_Refresh\Powershell\NoBOM.txt', 'r') as f:
        
        x = f.read().splitlines()
        
        return x
          

              
         
def powershell():
    computer_name = get_computername()
    
    for computer in computer_name:
        print(f"Trying to reach " + computer)
        PowerShellPath = r'C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe'
        PowerShellCmd = "F:\\Windows_10_Refresh\\Powershell\\Get-SysInfo.ps1" # Change Path here to where your powershell script is saved
 
        p = subprocess.Popen([PowerShellPath, '-ExecutionPolicy', 'Unrestricted', PowerShellCmd, computer])
     
        print("Gathering Information")
        p.communicate()


