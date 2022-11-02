print("...:ZADANIE 5:...")
liczba_studentow = int(input("Podaj liczbe studentow: "))
 
licznik = liczba_studentow
srednia_punktow = 0
 
while (licznik > 0):
    srednia_punktow += int(input("Punkty studenta nr " + str(licznik) + ": "))
    licznik -= 1
 
srednia_punktow /= liczba_studentow
 
print("Srednia punktow wynosila ", srednia_punktow)


'''
print("...:ZADANIE 7:...")
liczba = 0

for liczba in range(101): #zakres od 0 do 100
    print(liczba)

print("................................")

for liczba in range(100,0,-1): #zakres od 100 - 0
    print(liczba)

print("................................")

for liczba in range(0,101,7): #zakres od 0 do 100 z krokiem co 7 
    print(liczba)

print("................................")

for liczba in range(20,0,-2): #zakres od 20 do 0 z krokiem co -2 
    print(liczba)

print("................................")
'''
'''
print("...:ZADANIE 8:...")
x = int(input("Podaj liczbe gwiazdek: "))
y = int(input("Podaj liczbe wierszy: "))
g = '*'
n = 0

for n in range(0,y+1):
    print(x*g)
'''
'''
print("...:ZADANIE 9:...")
ch=int(input("Ilu stopniowa ma byc choinka? "))
spacja = ''
gwiazdka = '*'
k=ch

for n in range(0,ch+1):
    i=2*n-1 #wzór wyciągniety z ciągu arytm.
    print(k*spacja+i*gwiazdka)
    k-=1
'''