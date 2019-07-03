import sqlite3
from contextlib import closing

import menu
from objects import Computer

conn = None 

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

def update_data(computer):
    """
    Updates Data Into relevent tables in Database. Params: Pass variables into the two classes and then just pass those into this function
    Used by misc_func.add_computer()
    """
    sql_updateinfo = "UPDATE Computers SET username = ?, lastlogon = ?, ipaddress= ? WHERE name = ?"
    sql_newinfo = "INSERT INTO Computers (name, username, windows, cpu, currentamount, totalslots, lastlogon, ipaddress) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    with closing(conn.cursor()) as cursor:
        cursor.execute('SELECT name FROM Computers WHERE name=?', (computer.name,))
        result = cursor.fetchone()
        
        if result:
            print(f"updating {computer.name} is being updated")
            cursor.execute(sql_updateinfo, (computer.username, computer.lastlogon, computer.ipaddress, computer.name))
        else:
            print(f"{computer.username}'s pc added succesfully")
            cursor.execute(sql_newinfo, (computer.name, computer.username, computer.windows, computer.cpu,
                           computer.currentamount, computer.totalslots, computer.lastlogon, computer.ipaddress))
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