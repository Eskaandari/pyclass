#barnamei baraye be dast avardane masahate mostatil bar hasb meter
def mostatil(tool, arz, vahed='m'):
    if vahed == "m":
        print(float(tool*arz))
    elif vahed == "cm":
        print(float((tool / 100)*(arz / 100)))
    elif vahed == "mm":
        print(float((tool / 1000)*(arz / 1000)))
    else:
        print('vahede andaze giri bayad millimeter, centimeter va ya meter bashad\
va dar in barname  nabayad az vahede {} estefade kard'.format(vahed))
mostatil(arz = 20, tool = 36)
