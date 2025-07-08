
from datetime import datetime

def check_data_valid(func):
    def inner(cnp,*args, **kwargs):
        cnp = str(cnp)
        if len(cnp) == 13 and cnp .isdigit():
            print("CNP ul e valid")
            return  func(cnp, *args, **kwargs)
        else:
            print("CNP ul nu e valid")
            return None
    return inner

@check_data_valid
def decorator(cnp):
    prima_cifra = int(cnp[0])

    if prima_cifra in [1, 3, 5, 7]:
        print("Persoana e de sex masculin")
    elif prima_cifra in [2, 4, 6, 8]:
        print("Persoana e de sex feminin")
    else:
        print("Cifra e invalida")
        return

    year = int(cnp[1:3])
    month = int(cnp[3:5])
    day = int(cnp[5:7])

    if prima_cifra in [1, 2]:
        century = 1900
    elif prima_cifra in [3, 4]:
        century = 1900
    elif prima_cifra in [5, 6]:
        century = 2000
    elif prima_cifra in [7, 8]:
        century = 2000

    an_intreg = century + year
    try:
        date_time = datetime(an_intreg, month, day).date()
        print(f"Data_nasterii : {date_time}")
    except ValueError:
        print("Data nu e valida")
        return


    judet = int(cnp[7:9])
    print(f"Judetul in care s-a nascut persoana este: {judet}")
    cod_secvential = int (cnp[9:12])
    print(f"Codul secvential al persoanei este : {cod_secvential}")
    cifra_control = int (cnp[12])


    constanta = "279146358279"
    calcul = sum(int(cnp[i]) * int(constanta[i]) for i in range(12))
    rest = calcul % 11
    cifra_calculata = 1 if rest == 10 else rest

    cifra_finala= int(cnp[-1])

    if cifra_finala == cifra_calculata:
        print(f"Cifra de control este: {cifra_finala}")
    else:
        print("Calculul nu e valid")



result = decorator(5230205325021)

















