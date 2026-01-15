
def dodaj(Liczba1,Liczba2):
    return Liczba1+Liczba2
def odejmij(Liczba1,Liczba2):
    return Liczba1-Liczba2
def pomnórz(Liczba1,Liczba2):
    return Liczba1*Liczba2
def podziel(Liczba1,Liczba2):
    try:
        return Liczba1/Liczba2
    except ZeroDivisionError:
        print("Nie można pomnożyć przez zero!")
def modulo(liczba1,Liczba2):
    return liczba1%Liczba2

while True:
    dzialanie=str(input("Podaj działanie matematyczne:+,-,*,:,%"))
    if dzialanie=="+":
        liczba1=int(input("Podaj liczbę nr.1"))
        liczba2=int(input("Podaj liczbę nr.2"))
        print(dodaj(liczba1,liczba2))
    elif dzialanie=="-":
        liczba1=int(input("Podaj liczbę nr.1"))
        liczba2=int(input("Podaj liczbę nr.2"))
        print(odejmij(liczba1,liczba2))
    elif dzialanie=="*":
        liczba1=int(input("Podaj liczbę nr.1"))
        liczba2=int(input("Podaj liczbę nr.2"))
        print(pomnórz(liczba1,liczba2))
    elif dzialanie==":":
        
        liczba1=int(input("Podaj liczbę nr.1"))
        liczba2=int(input("Podaj liczbę nr.2"))
        print(podziel(liczba1,liczba2))
    elif dzialanie=="%":
        liczba1=int(input("Podaj liczbę nr.1"))
        liczba2=int(input("Podaj liczbę nr.2"))
        print(modulo(liczba1,liczba2))
    else:
        print("Nieznane działanie.")