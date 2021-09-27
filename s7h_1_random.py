import random
float_or_int = input("float or int?\n")
if float_or_int == "float":
    result = random.uniform(1,100)
    print(result)
elif float_or_int == "int":
    result = random.randrange(1,100)
    print(result)
