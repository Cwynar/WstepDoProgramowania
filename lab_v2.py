'''
print("...:ZADANIE 1:...")

x = int(input(" Podaj wiek klienta: "))

if x < 4:
    print("Wstęp jest bez płatny")
elif x >= 4 and x <= 18:
    print("Cena biletu wynosi 10zł")
else:
    print("Cena biletu wynosi 20zł")
'''

'''

print("...:ZADANIE 2:...")

x = input("Podaj litere: ")

if x.isupper():
    print("duża litera")
else:
    print("mała litera")


x = input("Podaj literę: ")
if len(x) == 1:
    if x >= 'a' and x <= 'z':
        print("mała litera")
    elif 'A' <= x <= 'Z':
        print("DUŻA LITERA")
    else:
        print("pozostałe zanki")
else:
    exit()

'''


print("...:ZADANIE 2:...")
print("Operacje:")
print("1. Dodawanie")
print("2. Odejmownaie")
print("3. Mnożenie")
print("4. Dzielenie")
print("5  Potęgowanie")
print("6. Dzielenie z resztą(Modulo)")

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

def modulo(a,b):
    return a%b

x = float(input("Podaj pierwszą cyfre: "))
y = float(input("Podaj drugą cyfrę: "))
z = int(input("Jaką operacje chcesz wykonać: "))

while True:
    if z == 0:
        print("Podana funkcja nie istnieje")
        break
    elif z == 1:
        print(dodawanie(x,y))
        break
    elif z == 2:
        print(odejmowanie(x,y))
        break
    elif z == 3:
        print(mnożenie(x,y))
        break
    elif z == 4:
        if y == 0:
            print("NIE WOLNO DZIELIC PRZEZ 0 !!!")
            exit()
        print(dzielenie(x,y))
        break
    elif z == 5:
        print(potęgowanie(x,y))
        break
    elif z == 6:
        print(modulo(x,y))
        break
'''
x = input("Podaj literę: ")
if len(x) == 1:
    if x >= 'a' and x <= 'z':
        print("mała litera")
    elif 'A' <= x <= 'Z':
        print("DUŻA LITERA")
    else:
        print("pozostałe zanki")
else:
    exit()
'''

