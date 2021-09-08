#barnamei ast ke 2 adad ra az karbar begirad va az adade bozorgtar ta adade
#kochaktar ra chap konad
first_number = int(input("adade aval ra vard konid:\n"))
second_number = int(input("adade dovom ra vared konid:\n"))
if first_number > second_number:
    while first_number >= second_number:
        print(first_number)
        first_number += -1
elif second_number >= first_number:
    while second_number >= first_number:
        print(second_number)
        second_number += -1
