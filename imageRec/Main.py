import os

print("Please enter a command")

comm= input("1 for live feed, 2 for operations on database and Q to quit ")


while comm != "q":
    if comm == '1':
        os.system('Compare.py')
    if comm == '2':
        os.system('Operations.py')
    else:
        print("Wrong command, try again")
    comm= input("1 for live feed, 2 for operations on database and Q to quit ")



    
