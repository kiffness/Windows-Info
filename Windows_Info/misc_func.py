import db
import subprocess
from objects import Computer
# This serves as a place to put all my misc functions
import subprocess


def format_text():
        with open (r'f:\Windows_10_Refresh\Powershell\SysConfig.txt', 'r') as f:
     
    
            lines = f.read().splitlines()
             
            if lines[5] == '24':
                lines.insert(5,"DDR4")
                del lines[6]
            elif lines[5] == '23':
                lines.insert(5,"DDR3")
                del lines[6]
            elif lines[5] == '22':
                lines.insert(5,"DDR2")
                del lines[6]
            elif lines[5] == '21':
                lines.insert(5,"DDR")
                del lines[6]
            else:
                lines.insert(6,"N/A")
                del lines[6]
                 
        return lines

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


