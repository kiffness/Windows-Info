import sqlite3
from contextlib import closing

conn = None 

def connect():
    global conn
    if not conn:
        conn = sqlite3.connect(r"F:\Databases\SystemInfo.sqlite3") # Change path here to where your database is 
        conn.row_factory = sqlite3.Row   


def close():
    if conn:
        conn.close()
        
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