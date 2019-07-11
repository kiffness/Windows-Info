import sqlite3
from contextlib import closing

import misc_func
import menu
from objects import Computer, Name

conn = None
updated = []
added = []
not_connect = []



def remove_duplicates(x):
    return list(dict.fromkeys(x))

def logs():
    file = "F:\Windows_10_Refresh\Powershell\CouldNotConnectNoBom.txt"

    with open (file, 'r') as f:
        text = f.read().splitlines()
        for line in text:
            not_connect.append(line.rstrip())

    updated_nd = remove_duplicates(updated)
    added_nd = remove_duplicates(added)
    misc_func.log_main(added_nd, updated_nd, not_connect)

def connect():
    """Connects to Sqlite Database"""
    global conn
    if not conn:
        conn = sqlite3.connect(r"F:\Databases\SystemInfo.sqlite3") # Change path here to where your database is
        conn.row_factory = sqlite3.Row


def close():
    """Closes connection to database"""
    if conn:
        conn.close()

def make_computer(row):
    """Returns List of Computer object use when pulling data from database"""
    return Computer(
        row["computerid"],
        row["name"],
        row["username"],
        row["windows"],
        row["cpu"],
        row["currentamount"],
        row["totalslots"],
        row["lastlogon"],
        row["ipaddress"],
    )


def delete_computer():
    """
    Deletes disabled computer accounts from database, will first check if
    if the computer exists in the table
    """

    file = 'F:\Windows_10_Refresh\Powershell\DisabledAccountNoBOM.txt'

    with open(file, 'r') as f:

        name_list = []
        text = f.read().splitlines()

        # Checks if the text file is empty, if not appends to name_list
        if text:
            count = len(text)
            for line in text:
                name_list.append(line)

        with closing(conn.cursor()) as cursor:
            for name in name_list:
                # Checks if the computer name is in the database
                cursor.execute(f"SELECT name FROM Computers WHERE name = ('{name}')")
                result = cursor.fetchone()

                if result:
                    # if it exists delete it
                    cursor.execute(f"DELETE FROM Computers WHERE name = ('{name}')")
                    print(f"Deleted {name}")
                else:
                    # if not exists display a  message
                    print(f"{name} not found")
                conn.commit()


def update_data(computer):
    """
    Updates Data Into relevent tables in Database. Params: Pass variables into the two classes and then just pass those into this function
    Used by misc_func.add_computer()
    """
    log = "F:\Windows_10_Refresh\Logs\main_logs.txt"
    sql_updateinfo = "UPDATE Computers SET username = ?, lastlogon = ?, ipaddress= ? WHERE name = ?"
    sql_newinfo = "INSERT INTO Computers (name, username, windows, cpu, currentamount, totalslots, lastlogon, ipaddress) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    with closing(conn.cursor()) as cursor:
        cursor.execute('SELECT name FROM Computers WHERE name=?', (computer.name,))
        result = cursor.fetchone()

        if result:
            updated.append(computer.name)
            cursor.execute(sql_updateinfo, (computer.username,
                                            computer.lastlogon,
                                            computer.ipaddress,
                                            computer.name))
        else:
            try:

                added.append(computer.name)
            except TypeError:
                pass
            cursor.execute(sql_newinfo, (computer.name, computer.username,
                                         computer.windows, computer.cpu,
                                         computer.currentamount,
                                         computer.totalslots, computer.lastlogon,
                                         computer.ipaddress))

        conn.commit()


def select_os():
        """Function to query db based on os just enter the os like Windows 7 SP1"""
        connect()
        menu.display_select_os_menu()

        while True:
            os = None
            choice = input("Please Select Os 1 or 2: ").rstrip()
            if choice == "1":
                os = "Windows 7 SP1"
                break
            elif choice == "2":
                os = "Windows 10"
                break
        print(os)

        query = "SELECT * FROM Computers WHERE windows=?"
        with closing (conn.cursor()) as cursor:
                cursor.execute(query, (os,))
                results = cursor.fetchall()

                computers = []
                for result in results:
                        computers.append(make_computer(result))
                return computers
        close()
