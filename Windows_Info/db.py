import sqlite3
from contextlib import closing
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
        row["totalslots"]
    )
      
def insert_data(computer, ipv4):
    """
    Inserts Data Into relevent tables in Database. Params: Pass variables into the two classes and then just pass those into this function
    Used by misc_func.add_computer()
    """
    sql_geninfo = "INSERT INTO Computers (name, username, windows, cpu, currentamount, totalslots) VALUES (?, ?, ?, ?, ?, ?)"
    sql_ipv4 = "INSERT INTO logon (lastlogon, ipaddress) VALUES (?, ?)"
    with closing(conn.cursor()) as cursor:
        cursor.execute('SELECT name FROM Computers WHERE name=?', (computer.name,))
        result = cursor.fetchone()
        
        if result:
            print("")
        else:
            print(f"{computer.username}'s pc added succesfully")
            cursor.execute(sql_geninfo, (computer.name, computer.username, computer.windows, computer.cpu,
                           computer.currentamount, computer.totalslots))
            cursor.execute(sql_ipv4, (ipv4.lastlogon, ipv4.ipaddress))
            conn.commit()

def select_os():
        """Function to query db based on os just enter the os like Windows 7 SP1"""
        os = input("Please select os to query?: ")
        query = "SELECT * FROM Computers WHERE windows=?"
        with closing (conn.cursor()) as cursor:
                cursor.execute(query, (os,))
                results = cursor.fetchall()

                computers = []
                for result in results:
                        computers.append(make_computer(result))
                return computers