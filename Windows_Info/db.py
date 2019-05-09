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
    sql = "INSERT INTO Computers (name, username, windows, cpu, ram_capacity, ram_slots) VALUES (?, ?, ?, ?, ?, ?)"
    with closing(conn.cursor()) as cursor:
        cursor.execute(sql, (computer.name, computer.username, computer.windows, computer.cpu, computer.ram_capacity, computer.ram_slots))
        conn.commit()