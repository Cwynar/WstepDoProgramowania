'''
print("...:ZADANIE 6:...")
n = int(input("Podaj liczbe studentów: "))
x = 1
s = 0
while True:
    p = int(input(f"Podaj liczbe punktów dla studenta {x}: "))
    if p > 100 or p < 0:
        continue
    x += 1
    s += p
    if (n+1==x):
        break

print("średnia punktów wynosi: ", round(s/n,2))
'''

'''
print("...:ZADANIE 1:...")
zakupy = ['ciastka' , 'pomarańcze' , 'ogórki' , 'woda mineralna']

zakupy[2] = 'mleko'

print(zakupy[2:4])
'''
'''
print("...:ZADANIE 2:...")
import random
liczba = 0
zestaw1 = []
x = int(input("Podaj liczbe elemantów listy zestawu 1 [1-10]: "))

for x in range(x):
    y = random.randint(1,10)
    zestaw1.append(y)
print(zestaw1)

zestaw2 = []
d = int(input("Podaj liczbe elemantów listy zestawu 2 [5-15]: "))
for d in range(d):
    s = random.randint(5,15)
    zestaw2.append(s)
print(zestaw2)

f = int(input("Podaj liczbe: "))
if f in zestaw1:
    print("liczba z zestawu 1")
elif f in zestaw2:
    print("liczba z zestawu 2")
else:
    print("nie ma takiej liczby w zestawach ")

zestaw_1_2 = zestaw1 + zestaw2
zestaw_1_2.sort()
print(zestaw_1_2)
'''
'''
print("...:ZADANIE 3:...")
zwierzeta = []
x = int(input("Podaj liczbe zwierząt w liście: "))
for x in range(x):
    y = input("Podaj zwierzę: ")
    z = zwierzeta.append(y)
zwierzeta.sort()
print(zwierzeta)
print(zwierzeta[0],zwierzeta[-3],len(zwierzeta))
'''

'''
print("...:ZADANIE 4*:...")
imiona = ['Kasia', 'Tomek', 'Jan', 'Ola', 'Jerzy', 'Marek', 'Piotr','Zuzia', 'Bartek', 'Jacek'] #lista startowa
print(imiona)

imiona[3] = 'KACPER' #zamiana 4 indexu na imie KACPER
print(imiona)

imiona[4] = input("Podaj dowolne imie: ") #wstawienie dowolnego imienia do listy
print(imiona)

us = imiona.pop(6) #usunięcie 7 elementu listy
print("Usunięte imie:", us)
print(imiona)

imiona2=[]  #możliwość dodania n-liczby imion do listy i dodania ich na początek listy
x = int(input("Podaj ilość imion które chcesz dodac do listy: "))
for x in range(x):
    y = input("Podaj imię: ")
    z = imiona2.append(y)
imiona3 = imiona2 + imiona
print(imiona3)

u = input("Podaj imie do usunięcia: ") #usunięcie dowolnego imienia z listy
imiona3.remove(u)
print(imiona)

imiona[-1] = 'NATAN' #zamienienie ostatniego elementu listy na imie NATAN
print(imiona)

print(imiona[0:3], imiona[-3:-1]) #wyświetlenie 3. pierwszych imion i 3. ostatnich

i = input("Podaj imie: ") #sprawdzenie czy dane imie znajduje sie w liscie
if i in imiona:
    print("Twoje imie znajduje się na liście!")
else:
    print("twoje imie nie znajduje sie na liście :/ ")

imiona.sort() #sortowanie listy 
print(imiona)

imiona.reverse() #wyświetlenie listy od Z-A
print(imiona)

for v in range(len(imiona)//2): 
    imiona.pop()

print(imiona)
'''

print("...:ZADANIE 5:...")
def avg(punkty):
    return sum(punkty)/len(punkty)

punkty = []
x = int(input("Podaj ilość studentów: "))
c = 1
for x in range(x):
    y = int(input(f"Podaj ilość punktów dla studenta {c} [0-50]: "))
    z = punkty.append(y)
    c += 1
print(punkty)
max = max(punkty)
min = min(punkty)
print(f"Największa wartość punktów to: {max}, a najmniejsza to: {min}")

a = avg(punkty)
print(f"Średnia ilość punktów jest równa = {a}")

licznik_mnijeszych = 0
licznik_większych = 0
for punkty in punkty:
    if punkty >= a:
        licznik_większych += 1
    elif punkty <= a:
        licznik_mnijeszych += 1
    else:
        break

print(f"Punkty powyżej średniej: {licznik_większych}")

print(f"Punkty poniżej średniej: {licznik_mnijeszych}")

