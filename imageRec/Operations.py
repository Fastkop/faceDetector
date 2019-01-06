import sqlite3

conn= sqlite3.connect("Database/knownUsers.db")

def start():
    command="CREATE TABLE IF NOT EXISTS Known(name text PRIMARY KEY, path TEXT)"
    
    conn.execute(command)

def add(name,path):
    try:
        command="INSERT INTO Known(name,path) VALUES (?,?)"
        val=(name,path)
        conn.execute(command,val)
        conn.commit()
        print("{0} with path {1} has been added to the database".format(name,path))
    except:
        print("The name you entered is already there")

def delete(name):
    try:
        command="DELETE from Known WHERE name=?"
        val=(name,)
        conn.execute(command,val)
        conn.commit()
        print("{0} has been removed from the database".format(name))
    except:
        print("Name not found")
def data():
    command="select * from Known"
    cur= conn.cursor()
    cur.execute(command)
    rows=cur.fetchall()
    for row in rows:
        print("Name: {} Path: {} ".format(row[0],row[1]))


comm=input("Please select 1 to add a new person or 2 to delete a known person or 3 to view database or Q to quit ")

while comm != 'q':
    if comm == '1':
        n=input("enter the name of the person ")
        p=input("enter the name of the image ")
        add(n,p)
    elif comm == '2':
        n=input("enter the name of the person you wish to delete ")
        delete(n)
    elif comm=='3':
        data()
    else:
        print("Wrong command, try again")
    comm=input("Please select 1 to add a new person or 2 to delete a known person or 3 to view database or Q to quit ")
    



    
