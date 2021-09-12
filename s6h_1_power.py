#barnamei ast ke adad aval ra be tavan adade dovom beresanad
#bedune estefade az * va **
def tavan(first_number, second_number):
    hasele_tavan = 1
    for _ in range(second_number):
        hasele_tavan *= first_number
    return hasele_tavan
natije = tavan(int(input("adade aval ra vared konid:\n")),\
int(input("adade dovom ra vared konid:\n")))
print(natije)
