import sqlite3
from contextlib import closing
from objects import Computer

conn = None 

def connect():
    global conn
    if not conn:
        conn = sqlite3.connect(r"F:\Databases\SystemInfo.sqlite3") # Change path here to where your database is 
        conn.row_factory = sqlite3.Row   


def close():
    if conn:
        conn.close()

def make_computer(row):
    return Computer(
        row["computerid"],
        row["name"],
        row["username"],
        row["windows"],
        row["cpu"],
        row["currentamount"],
        row["totalslots"]
    )
      
def insert_data(computer):
    sql_geninfo = "INSERT INTO Computers (name, username, windows, cpu, currentamount, totalslots) VALUES (?, ?, ?, ?, ?, ?)"
    with closing(conn.cursor()) as cursor:
        cursor.execute('SELECT name FROM Computers WHERE name=?', (computer.name,))
        result = cursor.fetchone()
        
        if result:
            print("")
        else:
            print(f"{computer.username}'s pc added succesfully")
            cursor.execute(sql_geninfo, (computer.name, computer.username, computer.windows, computer.cpu,
                           computer.currentamount, computer.totalslots))
            conn.commit()

def select_os():
        """Function to query db based on os"""
        os = input("Please select os to query?: ")
        query = "SELECT * FROM Computers WHERE windows=?"
        with closing (conn.cursor()) as cursor:
                cursor.execute(query, (os,))
                results = cursor.fetchall()

                computers = []
                for result in results:
                        computers.append(make_computer(result))
                return computers