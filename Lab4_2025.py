# Zapamiętaj 3 główne moduły do programowania funkcyjnego
### I. Moduł functools - zawiera funkcje wyższego rzędu
### II. Moduł operator - zawiera standardowe operatory
### III. Moduł itertools - zawiera 3 typy iteratorów: skończone, nieskończone i kombinatoryczne


### I. Moduł functools - funkcje wyższego rzędu
### np. reduce() - patrz przykłady w Laboratorium 3
### np. partial(fun,arg1,arg2,...argN) - funkcja częsciowa,
###     posiada mniejszą liczbą parametrów niż funkcja fun, część jej argumentów jest
###     odgórnie ustalona "zamrożona"

# import functools
# help(functools) # podgląd dostępnych funkcji lub klas w pakiecie

## Przykład działanie funkcji wyższego rzędu partial(function,arg1,arg2,...argN)

# def multiply3(x, y, z):
#         return x * y * z
#
# partialmultiply3 = functools.partial(multiply3, x= 1, y = 1) # "zamrażamy" wartości x,y argumentów"
# print(partialmultiply3(z = 2))
# print(partialmultiply3(z = 10))
# print(partialmultiply3(z = 100))

### II. Moduł operator - zawiera standardowe operatory jako funkcje np.
# import operator
# help(operator) # podgląd dostępnych funkcji w pakiecie

## Przykładowe operatory:
## 2a Math operations: add(), sub(), mul(), floordiv(), abs()
## 2b Logical operations: not_(), truth()
## 2c Bitwise operations: and_(), or_(), invert()
## 2d Comparisons: eq() -> equal to, ne() -> not equal, lt()->less than,
## le()-less or equal, gt() -> greater than, and ge() -> greater or equal
## 2e Object identity: is_(), is_not()

##### Wykorzystanie funkcji wyższego rzędu i operatorów

### Example 1 - wykorzystanie funkcji wyższego rzędu i operatorów
## Porównaj kod mnożenia elementów 2 list

### 1. wariant imperatywnie
# list1 = [1,2,3,4,5]
# list2 = range(1,6)
#
# new_list = []
# for i in range(0,len(list1)): new_list.append(list1[i] * list2[i])
# print(new_list)

# ## 2. wariant funkcyjnie
### operator mnożenia dla 2 liczb
# print(operator.mul(2,3))  # to wynik mnożenia 2-ch liczb 2*3

# print(list(map(operator.mul,list1,list2)))  # mnożenie 2-list

##### Task 1
### Utwórz 2 listy, pierwsza liczby od 1 do 100, druga 100 losowych liczb
### odejmnij wartości elementów listy pierwszej od drugiej
### Wykorzystaj map() i funkcję sub() z modułu operators
# from random import randint

# r = [i for i in range(1, 100)]
# l = [randint(-100000, 100000) for _ in range (1, 100)]

# m = map(operator.sub, r, l)
# print(list(m))

### Example 2 - wykorzystanie funkcji wyższego rzędu i operatorów

## Selecja liczb większych od 0 z listy

### 1. wariant imperatywnie
# list1 = [-1,-20,100,20]
# new_list = []
# for i in list1:
#      if i%2 == 0: new_list.append(i)
# print(new_list)

### 2a. wariant funkcyjnie
# list1 = [-1,-20,100,20]
# num_high_zero = list(filter(lambda x: x > 0, list1))
# print(num_high_zero)

### 2b. wariant funkcyjnie
# num_high_zero = list(filter(lambda x: operator.gt(x,0), list1))   # gt() -> greater than
# print(num_high_zero)

## selecja liczb większych od 0 i mniejszych niż 70 z listy
# from operator import gt, lt, and_
# num_high_zero = list(filter(lambda x: and_(gt(x,0),lt(x,70)), list1))   # lt()->less than,
# print(num_high_zero)

##### Task 2
### Utwórz listę zawierającą 10000 losowych liczb
### wyselekcjonuj liczby mniejsze niż 3 i parzyste
### Wykorzystaj filter() i funkcje z modułu operators

# m = list(filter(lambda n: operator.and_(operator.lt(n, 3), operator.eq(operator.mod(n, 2), 0)), [randint(-100000, 100000) for _ in range(10000)]))

# print(m)

#######################################################################
### III. Moduł itertools - zawiera iteratory do wydajnego zapętlania
# import itertools
##  Iteratory nieskończone (funkcje z nieskończonymi iteratorami)
## count(start,krok) - odlicza kolejne liczby, nieskonczony interator
## cycle() - funkcja powtarzająca w cyklu wartości
## repeat() - funkcja powtarzająca powtarzanie 1-ej wartości
## nieskończoną liczbę razy, często używana łącznie z break w petli for

### Przykłady działania iteratorów nieskończonych
# from itertools import count, cycle, repeat

## Example 3a count(start,krok)
#for i in itertools.count(0,1): print(i) # nieskończony iterator od 0 z krokiem 1

# generujemy liczby od 2 do 4 z krokiem 1
# for i in itertools.count(2,1):
#     if i < 5:
#         print(i)
#     else:
#         break

##### Task 3
### Utwórz pętlę generującą 50 liczb całkowitych z krokiem 5, większych niż 99
### Wykorzystaj count()

# for i in itertools.count(0, 5): 
#     if i > 99: print(i)

## Example 3b cycle() -  kolejne elementy wypisywane cyklicznie
# i = 0
# for n in itertools.cycle('ALA'):  # for n in itertools.cycle([1,20,-3,4]):
#     if i >= 7:
#         break
#     else:
#         print(n)
#         i += 1

##### Task 4
### Utwórz funkcję funcycle(n) która z sekwencji 'INFORMATYKA'
### n krotnie (argument funkcji) wypisze w cyklu każdy z jej elementów
### Wykorzystaj cycle()

# def funcycle(n: int):
#     i = 0
#     for s in itertools.cycle('INFORMATYKA'):
#         if i > n: break
#         print(s)
#         i += 1

# funcycle(len('INFORMATYKA')-1)

## Example 3c repeat(object,n-times)  , repeat(object) - powtarzaj w nieskonczoność
# print(list(itertools.repeat('a',5)))  # powtarzaj 5-krotnie

###### Iteratory kombinatoryczne
## product() - odpowiednik zagnieżdżonych pętli for (iloczyn kartezjański)
## permutations() - możliwe permutacje n-elementów np. z listy
## combinations() - wszystkie możliwe kombinacje n-elementów wybranych np. z listy bez powtórzeń
## combinations_with_replacement() - wszystkie możliwe kombinacje n-elementów wybranych np. z listy z powtórzeniami

from itertools import product, permutations
from itertools import combinations, combinations_with_replacement

## ## Example 4a funkcja product() - W wymiarze 2D to kombinacje(x,y) etykiet x-wierszy i y-kolumn tabeli
# Wariant kod imperatywnie
# list1 = []
# for i in [1,2]:
#     for j in ['a', 'b', 'c']:
#         list1.append(tuple([i,j]))
# print(list1)


## wariant funkcyjnie
# print(list(product([1,2],['a', 'b', 'c'])))
# print(list(product([1,2],['a', 'b', 'c'],repeat = 2)))

##### Task 5
### Oblicz iloczyn kartezjański 3D, [1,2,3], ['a','b','c'], [True,False]

# print(list(product([1,2,3], ['a','b','c'], [True,False])))

#### Example 4b permutations() - możliwe kombinacje elementów
# list1 = [1,2,3,4,5]
# print(list(permutations(list1)))

# word = 'ALA'
# print(list(permutations(word)))

## ## Example 4c combinations() - możliwe kombinacje n-elementów bez powtórzeń, posortowane
# list1 = [1,2,3,4,5]
# print(list(combinations(list1,3))) # kombinacja n=3 elementowa

### Task 6
### Posiadasz grupę N-studentów (N-indeksów), podziel w/w grupę na n-podgrup
### Specyfikacja kodu: funkcja, wykorzystanie iteratora kombinatorycznego

# sepGroup = lambda students, groups: list(combinations([i for i in range(students)], groups))

# def sepGroup(s, g):
#     if g > s or g <= 0: return "g ne moze byc wieksze od s i mniejsze od 1."
#     indexes = [i for i in range(1, s)]
#     return list(combinations(indexes, s//g))

# print(sepGroup(20, 6))

from itertools import accumulate,chain
from itertools import compress, dropwhile, filterfalse

###### Iteratory skończone
## enumerate() - generowanie krotek na podstawie listy
## accumulate() - zwraca sekwencje redukcji wejściowego obiektu iterowalnego
## chain(iter1,iter2,iter3,...) - łączy szeregowo wiele obiektów
## chain.from_iterable() - łączy szeregowo wiele obiektów iterowalnych
#### filtrowanie
## compress(iter,selector) - filtruje obiekt iterowalny na podstawie selector-a Boolean (True/False)
## dropwhile(func,seq) i takewhile() do filtrowania obiektu iterowalnego na podstawie pojedynczej wartości True/False

## ## Example 5a accumulate - podobna do reduce
# import operator
# print(list(accumulate([1,2,3,4]))) # domyślnie suma
#print(list(accumulate([1,2,3,4], operator.mul))) # kumulacja mnożenie elementów

### Task 7
## początkowa kwota na 3mc lokacie to k = 10000, oprocentowanie lokaty to 0.01%
## oblicz jaką kwotę zgromadzi użytkownik po upływie t = 9mc
### Specyfikacja kodu: funkcja, wykorzystanie iteratora skończonego

# def obliczLokate(lokata: float, okresMc: int):
#     # po co mi w tym zadaniu iteratory?
#     return lokata * okresMc + (lokata * okresMc) * 0.01

# print(f"Zgromadzona kwota za 9mc to {obliczLokate(10000/3, 9)}")

## ## Example 5b chain()
#print(list(chain([0,0],[1,2,3,4],['a','b'])))
## ## Example 5c chain.from_iterable
# list1 = [0,0]
# list2 = [1,2,3,4]
# list3 = [10,20,30,40]
# list4 = [list1,list2,list3]
# print(list4)
# print(list(chain.from_iterable(list4)))

## ## Example 5d compress(iter,selector)
# list1 = [10,20,30,40]
# selector1 = [1,0,0,1]
# print(list(compress(list1,selector1)))


## ## Example 5e dropwhile(funkcja,iterator)
# from itertools import dropwhile
# list1 = [1,2,3,-1,-2,-3]
# print(list(dropwhile(lambda x: x<0 ,list1)))
### Task 8
## Utwórz listę 100 losowych liczby
## utwórz podzbiór liczb parzystych większych od 10
### Specyfikacja kodu: funkcja, wykorzystanie iteratora skończonego

# from random import randint
# l = [randint(-100000, 100000) for _ in range(100)]
# print(list(enumerate(compress(l, list(map(lambda x: 0 if x % 2 != 0 else 1, l))))))

## ## Example 5f filterfalse(funkcja,iterator)
# from itertools import filterfalse
# list1 = [1,2,3,-1,-2,-3]
# print(list(filterfalse(lambda x: x<0 ,list1)))

### Generatory to dużo prostszy sposób na tworzenie iteratorów
### Generatory - to szczegolny przypadek iteratorów, w których wartości są podawane
### nie w iteracji ale są generowane "na bieżąco" (leniwie).
### Ważne !!!: takie technika pozwala zredukować liczbę wykonywanych obliczeń, zmniejszyć
### wykorzystanie pamięci oraz tworzyć nieskończoną ilość elementów.
### Mamy dwa rodzaje generatorów:
### I stworzone przez funkcje generujące
### II przez wyrażenia generujące

### I. Funkcja generująca
### Funkcja, w której pojawi się słowo yield zmienia się w tzw. funkcję generującą.
### Jej wywołanie tworzy generator czyli rodzaj iteratora
### słowa kluczowego yield używa się podobnie do return
### taka funkcja może zostać wstrzymana oraz wznowiona od miejsca, w którym została wstrzymana
### co więcej na podstawie zapamiętanego, stanu możliwe jest zwracanie różnych
### jej wartości podczas kolejnych wstrzymań funkcji
###  Utworzymy własny generator liczb parzystych w zakresie od 0 do n-1

# def onlyeven(n):  # funkcja generująca
#     for i in range(1, n):
#         if i % 2 == 0:
#             yield i

# even1 = onlyeven(40)  # nasz własny iterator
# print(next(even1))
# print(next(even1))
# print(next(even1))
# print(next(even1))

######## Example 3
# list100 = list(range(0,100,2)) # lista kolejnych liczb w zakresie od 0 do 100, krok 2
# generator1 = [lambda i: (yield i) for i in list100]
# print()

### Task 8
### Utwórz własny generator liczb które są kolejnymi wielokrotnosciami liczby cztery tj. 4,16,32,64,... itd
### n - liczbę elementów w generatorze deklaruje użytkownik
### np. dla n=3,  funkcja next w kolejnych wywołaniach zwraca:  4, 16, 32

# def multoffour(n):
#     for i in range(1, n):
#         if i % 4 == 0:
#             yield i

### Example
### Zwróć uwagę że możesz w kolejnych iteracjach realizować przerywać operacje,
### następnie je wznawiać
### wykonywać różne operacje w zależności od warunku

# def operation4times(x,y):
#     x1 = x+y
#     yield x1
#     x2 = x1*2
#     yield x2
#     yield x2
#     x3 = x2*100
#     yield x3
#     if x == 1:
#         yield x3*0
#     else:
#         yield x3 * 100
#
#
# for i in operation4times(10,2):
#     print(i)
#
# for i in operation4times(1,2):
#     print(i)

### Task 9
## a) Utwórz własny generator zwracający 1000 losowych liczb parzystych z zakresu 0-100000000

# from random import randint
# def tohundredmils():
#     for _ in range(1000):
#         yield randint(0, 100000000)


### II wyrażenie generujące

######### Example 1
#### Tradycyjna pętla imperatywnie
# for i in ['a','b','c']: print(i)

# wyrażenie generujące np.
# obj_iter1 = (i for i in ['a','b','c'])
# #### Wykorzystujemy funkcję next() do zwracania kolejych elementów listy
# print(next(obj_iter1))
# print(next(obj_iter1))
# print(next(obj_iter1))

### Możemy też utworzyć obiekt iterowalny, (obiekt w którym można przejść przez wszystkie jego wartości)
# obj_iter2 = iter(['a','b', 'c'])
#### Wykorzystujemy funkcję next() do zwracania kolejych elementów listy
# print(next(obj_iter2))
# print(next(obj_iter2))
# print(next(obj_iter2))

######## Example 2
### Tradycyjna podwójna pętla imperatywnie
# for i in list1:
#     for j in list1:
#         print(i,j)

### pętla z podwójnym iteratorem
#list1 = ['a', 'b', 'c']

# obj_iter1 = iter(list1) #  1-st iterator
# print(next(obj_iter1)) # 'a'
# obj_iter2 = iter(list1)  #  2-nd iterator
# print(next(obj_iter2))   # 'a'
# print(next(obj_iter2))   # 'b'
# print(next(obj_iter2))   # 'c'

#### Task 9
## Utwórz generator dla ciągu Fibonacciego (pierwszy wyraz ciągu jest równy 0, drugi jest równy 1,
## a każdy kolejny element ciągu jest sumą dwóch poprzednich. Wypisz n-ty element tego ciągu
## Użytkownik deklaruje ilość elementów (n).
## Specyfikacja: użyj accumulate() lub reduce() do wygenerowania ciągu Fibonacciego
# def fib(n):
#     for i in list(accumulate(range(n), lambda x, y: x + y)):
#         print(i)

# fib(10) # TODO dorob


# from functools import reduce
# from itertools import accumulate

############## Pomiar wydajności algorytmu
## sprawdź ile pamięci zajmuje twoja zmienna, w tym celu użyj funcję getsizeof() z pakietu sys
from sys import getsizeof
# a= 10
# print(getsizeof(a))

## sprawdź czas wykonania operacji, w tym celu użyj funcje time() z pakietu time
from datetime import datetime
# time0 = datetime.now().microsecond
# for i in range(100): i
# print(datetime.now().microsecond-time0)


#### Task 10
## Porównaj czas obliczeń i ilość zajmowanej pamięci przez dane w przypadku gdy programujesz
## a) imperatywnie/sturkturalnie,
## b) funkcyjnie stosując funkcje ale nie wyższego rzędu,
## c) funkcyjnie stosując funkcje wyższego rzędu, do zrównoleglenia obliczeń
## d) funkcyjnie stosując generator/iterator,
## Jak wariant realizuje zadanie najszybciej, a jakie zajmuje najmniej pamięci?

## Utwórz 3 listy po 1000000 losowych liczb
## zapisz liczby z 3 list do 2-ch list: pierwsza zawiera liczby parzyste, druga liczby nieparzyste

#### Task 11
### W przypadku dużych danych stosujemy algorytm dziel i rządź, który polega na odpowiednim
### 1. dzieleniu danych na części,
### 2. mapowaniu (operacja którą można przeprowadzić niezależnie w pewnym zakresie np. tworzymy pary klucz-wartość),
### 3. przesuwaniu (np.grupowanie podobnych kluczy, jesli są one blisko siebie agregujemy ich wartości)
### 4. redukowaniu danych (agregowanie danych poprzez ich redukcję)

## Utwórz listę zawierającą 10000 losowych nazw 6 języków programowania
## np. list_prog = ['python','java','C++','C++','python',....,'java']
# oblicz ile razy wybrany język programowania wystąpił w liście
## a) programuj imperatywnie
## b) programuj funkcyjnie
## c) wykorzystaj algorytm dziel i rządź który stosujemy aby zobtymalizować obliczenia gdy dane są duże
## np. wariant1: podziel zadania na podzadania wykonaj operację na zliczania na podzbiorach i agreguj wyniki
## wykorzystaj funkcje wbudowane lub metody dedykowane dla list
## np. wariant2: dzielisz listę na n-list, każda lista zawiera m-krotek [('python',1),...,('java',1),('C++',1)]
## przesuwasz identyczne krotki do 6-ciu list i zliczasz ilości, wynik końcowy to np. ('python',101),('java',23)