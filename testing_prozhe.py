import sqlite3
connect = sqlite3.connect("test.db")
while True:
    dastur = int(input("please enter a request:\nfor create new contact press (1)\nfor remove a contact press (2)\nsearch for a contact press (3)\nfor get contacts list press (4)\nexit press (5)\n"))
    if dastur == 1:
        first_name = input("enter the name:\n")
        last_name = input("enter the last name:\n")
        number = int(input("enter the number:\n"))
        query = f"insert into contacts values('{first_name}','{last_name}',{number})"
        cursor = connect.cursor()
        cursor.execute(query)
        connect.commit()
    elif dastur == 2:
        hazf = input("who do you want to remove?\n")
        query = f"delete from contacts where first_name = '{hazf}'"
        cursor = connect.cursor()
        cursor.execute(query)
        connect.commit()
    elif dastur == 3:
        search = input("who do you want to search?")
        query = f"select * from contacts where first_name = '{search}'"
        cursor = connect.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)
        connect.commit()
    elif dastur == 4:
        query = 'select * from contacts'
        cursor = connect.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        print(rows)
        connect.commit()
    elif dastur == 5:
        break
