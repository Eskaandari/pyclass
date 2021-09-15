def seperator(name):
    """
    barnamei baraye gereftane name va
    joda kardane first name va last name
    """
    first_name = ""
    last_name = ""
    for char in name:
        if char == " ":
            break
        first_name += char
    print("first name = {}".format(first_name))
    last_namee = name[len(first_name):]
    for i in last_namee:
        if i == " ":
            continue
        last_name += i
    print("last name = {}".format(last_name))
import inspect
print(inspect.getdoc(seperator), end = "\n\n\n")


seperator("Emmanuel Eskandari")
