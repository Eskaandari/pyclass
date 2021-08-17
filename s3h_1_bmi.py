#barnamei baraye be dast avardane bmi
def bmi(vahed_vazn, vahed_ghad):
    print("bmi=weight(kg)/height(m)**2")
    weight=int(input("vazne shoma cheghadr ast?\n"))
    height=int(input("ghade shoma cheghadr ast?\n"))
    if vahed_vazn == "kg" and vahed_ghad == "m":
        print(weight/(height**2))
    elif vahed_vazn == "g" and vahed_ghad == "cm":
        print((weight/1000)/((height/100)**2))
    elif vahed_vazn == "g" and vahed_ghad == "m":
        print((weight/1000)/(height**2))
    elif vahed_vazn == "kg" and vahed_ghad == "cm":
        print(weight/((height/100)**2))
    else:
        print("balad nistam")
bmi("kg", "cm")
