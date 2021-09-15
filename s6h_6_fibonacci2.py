#barnamei baraye be dast avardane jomle n fibonacci ba estefade az
#tabe bazgashti
def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)
print(fibonacci(int(input("adad ra vared konid:\n"))))
