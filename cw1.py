'''ZADANIE 1-1.1'''

'''
x = int(input("Podaj bok a: "))
y = int(input("Podaj bok b: "))

pole = x*y
obw = 2*x + 2*y

print(f"Pole wynosi: {pole}")
print(f"Obwód wynosi: {obw}")
'''

'''ZADANIE2-2.2'''
'''
x = int(input("Podaj pokonaną droge[km]: "))
y = float(input("Średnie spalanie[l/100km]: "))

koszty = (x/100)*y
print(f"Spalanie wynosi: {koszty}l")
print(f"Koszty podróży: {koszty*6.5}zł")


import random
x = random.randint(1,1000)
y = float(input("Średnie spalanie[l/100km]: "))

koszty = (x/100)*y
print(f"Spalanie wynosi: {koszty} l")
print(f"Koszty podróży: {koszty*6.5} zł")
'''

'''ZADANIE 3'''
'''
wiek = int(input("Podaj wiek klienta: "))
if wiek < 4:
    print("wtęp jest bezpłatny")
elif wiek >= 4 and wiek < 18:
    print("Cena biletu wynosi: 10zł")
else:
    print("Cena biletu wynosi: 20zł")
'''

'''ZADANIE 4'''
'''
x = input("Podaj literę: ")
if(x.isupper()):
    print("Podana litera jest DUŻA")
else:
    print("Podana litera jest mała")
'''

'''ZADANIE 5 i 6. dodatkowe'''
def dodawanie(a,b):
    return a+b

def odejmowanie(a,b):
    return a-b

def mnożenie(a,b):
    return a*b

def dzielenie(a,b):
    return a/b

def potęgowanie(a,b):
    return a**b

def reszta(a,b):
    return a%b

print("...PROSTY KALKULATOR...")
print("DOSTĘPNE OPERACJE:")
print("1. DODAWANIE")
print("2. ODEJMOWANIE")
print("3. MANOŻENIE")
print("4. DZIELENIE")
print("5. POTĘGOWANIE")
print("6. DZIELENIE Z RESZTĄ")

x = int(input("Podaj argument 1: "))
y = int(input("Podaj argument 2: "))
z = int(input("Wpisz numer operacji: "))

while True:
    if z == 1:
        print("Wynik: "), print(dodawanie(x,y))
        break
    elif z == 2:
        print(odejmowanie(x,y))
        break
    elif z == 3:
        print(mnożenie(x,y))
        break
    elif z == 4:
        print(dzielenie(x,y))
        break
    elif z == 5:
        print(potęgowanie(x,y))
        break
    elif z == 6:
        print(reszta(x,y))
        break
    else:
        print("podaj liczbe z zakresu 1-6")
        break
