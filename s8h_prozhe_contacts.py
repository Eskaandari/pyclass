import sqlite3
connect = sqlite3.connect("prozhe.db")
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
        query = f"delete from contacts where first_name = '{hazf}' or last_name = '{hazf}'"
        cursor = connect.cursor()
        cursor.execute(query)
        connect.commit()
    elif dastur == 3:
        search_way = int(input("for search by name or last name please insert 1,for search by number please insert 2:\n"))
        if search_way == 1:
            search = input("please insert the name or last name:\n")
            query = f"select * from contacts where first_name = '{search}' or last_name = '{search}'"
        elif search_way == 2:
            search = int(input("please insert the number"))
            query = f"select * from contacts where number = {search}"
        cursor = connect.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            for i in row:
                if i == search:
                    continue
                print(i)
        connect.commit()
    elif dastur == 4:
        query = 'select * from contacts'
        cursor = connect.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        connect.commit()
    elif dastur == 5:
        break
