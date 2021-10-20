def read_list():
    lista = []
    lista_str = input("Citeste numere separate de SPATIU ")
    lista_str_split = lista_str.split(' ')
    for num_str in lista_str_split:
        lista.append(int(num_str))
    return lista


def print_menu():
    print(' ')
    print("1. Citire date: ")
    print("2. Afiseaza numere negative din lista : ")
    print("3. Afisarea celui mai mic numar care are ultima cifra egala cu k : ")
    print("4. Afisare superprime: ")
    print("5. Inlocuieste lista initiala cu Cmmdc pt >0 si cu inversul pt <0: ")
    print("6. iesire")


def afiseaza_numere_negative(list):
    """
    Determina numrerele negative din lista
    :param list: Lista de numere intregi
    :return: Numrele negative din lista
    """
    res = []
    for i in list:
        if i < 0:
            res.append(i)
    return res


def test_afiseaza_numere_negative():
    assert afiseaza_numere_negative([-1, -2, -3]) == [-1, -2, -3]
    assert afiseaza_numere_negative([-1, -2, 3]) == [-1, -2]
    assert afiseaza_numere_negative([1, 2, 3]) == []


def mic_cu_ultimak(list, k):
    """
    Determina cel mai mic numar cu ultima cifra egala cu k
    :param list: Lista de numere intregi
    :param k: Numarul cu care este egala ultima cifra
    :return: Cel mai mic numar cu ultima cifra egala cu k
    """
    a = None
    for i in list:
        if i % 10 == k and (a == None or a > i):
            a = i
    return a


def test_mic_cu_ultimak():
    assert mic_cu_ultimak([48, 68, 78], 8) == 48
    assert mic_cu_ultimak([21, 41, 51], 6) == None
    assert mic_cu_ultimak([21, 4, 51], 4) == 4


def isPrime(x):
    '''
    determina daca un nr. este prim
    :param x: un numar intreg
    :return: True, daca x este prim sau False in caz contrar
    '''
    if x < 2:
        return False
    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    return True

def testIsPrime():
    assert isPrime(-1) is False
    assert isPrime(0) is False
    assert isPrime(1) is False
    assert isPrime(2) is True
    assert isPrime(3) is True


def super_prim(x):
    """
    Determina daca numarul este super prim
    :param x: Numarul pe care il primeste
    :return: True daca x este super prim, False altfel
    """
    p = 1
    aux = x
    cf = 1    # gradul lui x
    while aux > 9:
        cf = cf * 10
        aux = aux // 10
    while cf > 0:
        if isPrime(x // cf) == False:
            return False
        cf = cf // 10
    return True

def test_super_prim():
    assert super_prim(239) == True
    assert super_prim(15) == False
    assert super_prim(23) == True



def afisare_super_prim(lista):
    """
    Determina elementele superprime dintr-o lista (pozitiv si toate prefixele sunt prime)
    :param lista:Lista de numere intregi
    :return:Elementele superprime din lista
    """
    res = []
    for i in lista:
        if super_prim(i) and i > 0:
            res.append(i)
    return(res)


def test_afiseare_super_prim():
    assert afisare_super_prim([239, 155]) == [239]
    assert afisare_super_prim([139, 155]) == []
    assert afisare_super_prim([222, 31]) == [31]


def gcd(my_list):
    """
    Determina cel mai mar divizor comun al numerelor din lista
    :param my_list: Lista de numere pozitive
    :return: Cel mai mare divizor comun al numerelor din lista
    """
    result = my_list[0]
    for x in my_list[1:]:
        if result < x:
            temp = result
            result = x
            x = temp
        while x != 0:
            temp = x
            x = result % x
            result = temp
    return result

def test_gcd():
    assert gcd([12,24,36]) == 12
    assert gcd([5, 10, 20]) == 5
    assert gcd([10, 10, 20]) == 10


def lista_pozitive(lista):
    """
    Determina numerele pozitive din lista de numere
    :param lista: Lista de numere intregi
    :return: Numerele pozitive din lista
    """
    res = []
    for i in lista:
        if i > 0:
            res.append(i)
    return res


def test_lista_pozitive():
    assert lista_pozitive([1, 2, 3]) == [1, 2, 3]
    assert lista_pozitive([1, 2, -3]) == [1, 2]
    assert lista_pozitive([-1, -2, -3]) == []

def reve(x):
    """
    Determina numarul neagativ cu cifrele invers
    :param x: Numarul primit de functie
    :return: Numarul negativ cu cifrele invers
    """
    x=str(x)
    if x[0]=='-':
        a=x[::-1]
        return f"{x[0]}{a[:-1]}"


def test_reve():
    assert reve(-123) == "-321"
    assert reve(-1) == "-1"
    assert reve(-12) == "-21"


def inlocuire_cu_cmmdc_inversul(lista):
    """
    Determina afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
    CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
    :param lista: Lista de numere intregi
    :return:Lista obtinuta din lista initiala in care numerele pozitive și nenule au fost înlocuite cu
    CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
    """
    res = []
    l = lista_pozitive(lista)
    cmmdc = gcd(l)
    for i in lista:
        if i > 0:
            res.append(cmmdc)
        else:
            res.append(reve(i))
    return res

def test_inlocuire_cmmdc_inversul():
    assert inlocuire_cu_cmmdc_inversul([12, 48, 24, -14, -16]) == [12, 12, 12, "-41", "-61"]
    assert inlocuire_cu_cmmdc_inversul([10, 30, 50]) == [10, 10, 10]
    assert inlocuire_cu_cmmdc_inversul([-16, 12]) == ["-61", 12]

def main():
    lista = []
    while True:
        print_menu()
        Optiune = int(input("Alege o optiune: "))
        if Optiune == 1:
            lista = read_list()
        elif Optiune == 2:
            print("Numerele negative din lista sunt :", afiseaza_numere_negative(lista))
        elif Optiune == 3:
            k = int(input("Care sa fie ultima cifra a numarului "))
            print("Numarul cel mai mic cu ultima cifra egala cu k este: ", mic_cu_ultimak(lista, k))
        elif Optiune == 4:
            print("Elementele super prime din lista sunt :", afisare_super_prim(lista))
        elif Optiune == 5:
            print("Lista inlocuita este: ", inlocuire_cu_cmmdc_inversul(lista))
        elif Optiune == 6:
            break



if __name__ == '__main__':
    test_afiseaza_numere_negative()
    test_mic_cu_ultimak()
    testIsPrime()
    test_super_prim()
    test_afiseare_super_prim()
    test_gcd()
    test_lista_pozitive()
    test_reve()
    test_inlocuire_cmmdc_inversul()
    main()