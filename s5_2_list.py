#barnamei ast ke adad ra az karbar gerefte va dar list zakhire mikonad va sepas
#majmu va miangin an ha ra hesab mikonad
adad = list()
while True:
    number = int(input("adad ra vared konid"))
    if number < 0:
        break
    adad.append(number)
print(adad)
total = 0
for i in adad:
    total += i
print(total)
print(total/len(adad))
