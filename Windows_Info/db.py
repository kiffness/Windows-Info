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
        
def insert_data(computer, raminfo):
    sql_geninfo = "INSERT INTO Computers (name, username, windows, cpu) VALUES (?, ?, ?, ?)"
    sql_raminfo = "INSERT INTO raminfo (manufacturer, currentamount, totalslots, speed) VALUES (?, ?, ?, ?)"
    with closing(conn.cursor()) as cursor:
        cursor.execute(sql_geninfo, (computer.name, computer.username, computer.windows, computer.cpu))
        cursor.execute(sql_raminfo, (raminfo.manufacturer, raminfo.currentamount, raminfo.totalslots, raminfo.speed))
        conn.commit()