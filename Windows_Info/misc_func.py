import subprocess
import filecmp
import smtplib
from email.message import EmailMessage
import secret
from tqdm import tqdm

import db
from objects import Computer, LastLogon, Date
import objects

def email():
    """Connect to email server and account, Send Email when script completes"""
    # Connecting to account
    smtpobj = smtplib.SMTP('smtp.office365.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()

    # Logging in to SMTP server

    # Secret refers to another python file that has my email creds in a list
    smtpobj.login(secret.login['email'], secret.login['password'])

    # Send E-mail
    msg = EmailMessage()
    msg.set_content('Script is Finished')

    msg['Subject'] = 'Finished Running Windows 10 Refresh'
    msg['From'] = secret.login['email']
    msg['To'] = secret.login['email']

    smtpobj.send_message(msg)

    # logging out
    smtpobj.quit()

def get_computername():
    """
    Returns a Computer name from text file which is then iterated over in
    powershell()
    """
    with open (r'f:\Windows_10_Refresh\Powershell\NoBOM.txt', 'r') as f:

        x = f.read().splitlines()

        return x

def return_count():
    """
    Returns The Number of lines in text file made by
    computer_name_only.ps1
    """
    thefilepath = r'f:\Windows_10_Refresh\Powershell\NoBOM.txt'

    count = len(open(thefilepath).readlines( ))

    return count

def read_text():
    """Read the Text File made by powershell() and print and format it"""
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

def format_select_os():
    """Returns Formatted Information from the db.select_os() function"""
    # print("-" * 130)
    line_format1 = "{:15s} {:25s} {:15s}"
    print(line_format1.format("Name", "Username", "Windows"))
    print("-" * 130)
    computers = db.select_os()
    for computer in computers:
        print(line_format1.format(computer.name,
              computer.username,
              computer.windows))
    print("-" * 130)


def add_computer():
    """
    Reads in Text file created by powershell() assigns it to a variable then
    passes the Info to Computer, LastLogon Class which creates an object.
    Lastly the function passes the returned object to db.insert data
    """

    file1 = 'f:\Windows_10_Refresh\Powershell\SysConfig.txt'
    with open (file1, 'r') as f1:

        text = f1.read().splitlines()

        if text:
            name = text[0]
            username = text[1]
            windows = text[2]
            cpu = text[3]
            currentamount = text[4]
            totalslots = text[5]
            lastlogon = text[6]
            ipaddress = text[7]

            computer = Computer(name=name, username=username,
                                windows=windows, cpu=cpu,
                                currentamount=currentamount,
                                totalslots=totalslots,
                                lastlogon=lastlogon, ipaddress=ipaddress)
            db.update_data(computer)

        else:
            print("")

def log_main(added, updated, not_connect):

    log = r"F:\Windows_10_Refresh\Logs\main.txt"

    with open (log, 'w') as f:
        f.write("Computers that were added\n")
        f.write("-" * 95)
        f.write("\n")
        f.writelines(f"{line}\n" for line in added)
        f.write("Computers that were updated\n")
        f.write("-" * 95)
        f.write("\n")
        f.writelines(f"{line}\n" for line in updated)
        f.write("Computers that could not be connect to\n")
        f.write("-" * 95)
        f.write("\n")
        f.writelines(f"{line}\n" for line in not_connect)
    p = Date("main", "main")
    p.format_date()


def powershell():
    """Runs Powershell Script, emails when done"""
    computer_name = get_computername()

    for computer in computer_name:
        PowerShellPath = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
        # Change Path here to where your powershell script is saved
        PowerShellCmd = "F:\\Windows_10_Refresh\\Powershell\\Get-SysInfo.ps1"

        p = subprocess.Popen([PowerShellPath, '-ExecutionPolicy',
                             'Unrestricted', PowerShellCmd, computer])
        p.communicate()
        add_computer()

    email()

def refresh_list():
    """Refreshes text file used to get computer names for powershell()"""
    PowerShellPath = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
    PowerShellCmd = r'F:\Windows_10_Refresh\Powershell\computer_name_only.ps1'

    f = subprocess.Popen([PowerShellPath, '-ExecutionPolicy',
                         'Unrestricted',PowerShellCmd])
    f.communicate()

    print("Finished")



def get_disabled():
    """
    Gets all the computer accounts that have been disabled and adds to
    a text file called CouldNotConnect
    """
    PowerShellPath = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
    PowerShellCmd = r'F:\Windows_10_Refresh\Powershell\ADComputer.ps1'
    f = subprocess.Popen([PowerShellPath, '-ExecutionPolicy',
                         'Unrestricted',PowerShellCmd])
    f.communicate()

def remove_bom():
    PowerShellPath = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"
    PowerShellCmd = r'F:\Windows_10_Refresh\Powershell\Remove_Bom.ps1'
    f = subprocess.Popen([PowerShellPath, '-ExecutionPolicy',
                         'Unrestricted',PowerShellCmd])
    f.communicate()
