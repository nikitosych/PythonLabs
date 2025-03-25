############ Typ danych (klasa) zbiór - Data type: set ###############
# my_list = [5, 1, 1, 2, 3]
# a = set(my_list)
# b = set([4, 5, 6, 7, 8])
# #### wybrane operacje na zbiorach (selected operation in sets)
# print(a & b)   #    & - ampersand
# print(a.intersection(b)) # operacja równoważna do powyższej
#
# print(a | b)  #
# print(a.union(b))   # operacja równoważna do powyższej
#
# print(a - b)
# print(a.difference(b))   # operacja równoważna do powyższej
#
# print(b - a)
# print(b.difference(a))   # operacja równoważna do powyższej

#### Zadanie 1
## Poniżej masz 3 zbiory genów, 3 różnych pacjentów chorych na różne choroby
## Odpowiedz na poniższe pytania:
## a) Które elementy/geny są wspólne dla wszystkich pacjentów?
## b) Jakie elementy/geny są wspólne dla 2 pacjentów?
## c) Jakie elementy/geny występują wyłącznie w przypadku 1 choroby?

# set_gene1 = set(['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
#                 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
#                 'SAC19A22', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
# set_gene2 = set(['SLC19A3', 'ATP7B', 'ERBB3', 'FGFR4', 'ABCC3','GALNT14', 'ERCC1',
#                 'LJS19A2', 'AKM7B', 'ELLB32', 'FULR421', 'ANGC3', 'WELNT14', 'EOO11',
#                 'SAC19A2', 'AAAP7B', 'ERB3', 'FGR4', 'ACC3', 'GASNT14', 'ERSS4'])
# set_gene3 = set(['SLC19A3', 'ATP7B1', 'ERBB32', 'FGFR4', 'ABCC3','GALNT14', 'ERCC11',
#                 'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT15', 'EOO1',
#                 'SAC19A22', 'AAP7B', 'ERBB3', 'FGR4', 'ACC4', 'GASNT14', 'ERSS4'])
# common_genes = set_gene1 & set_gene2 & set_gene3
# print(common_genes)
# common_two = (set_gene1 & set_gene2) | (set_gene1 & set_gene3) | (set_gene2 & set_gene3) - common_genes
# print(common_two)
# unique_genes = {
#     "Pacjent 1": set_gene1 - set_gene2 - set_gene3,
#     "Pacjent 2": set_gene2 - set_gene1 - set_gene3,
#     "Pacjent 3": set_gene3 - set_gene1 - set_gene2
# }
# print(unique_genes)


######### Operatory porównania lokalnego i globalne
####################Przykład
### Sprawdź wynik działania następujących operacji:
# l1 = [5,10]
# l2 = [5,11]
#
# print(l1,l2)
# print('l1 == l2 wynik:',l1 == l2)
# print('l1 is l2 wynik:',l1 is l2)
# print('l1 != l2 wynik: ',l1 != l2)
# print('l1 is not l2 wynik:',l1 is not l2)
# print('l1 >= l2 wynik:', l1 >= l2)

## x or y	jeżeli x == False, to y, w przeciwnym razie x
## w przybliżeniu alternatywa
## x and y	jeżeli x == False, to x, w przeciwnym razie y
## w przybliżeniu koniunkcja
## not x	negacja



####################Przykład
# a = False
# b = 2
# c = True
#
# print(a or b)
# print(b or a)
# print(c or a)
# print(a or c)
# print(b and a)
# print(a and b)
# print(a and c)

###### Przykład
# list1 = [1,2,3,4,5,6,7,6,5,6,5]
# for element in list1:
#     print(element is 5)

# ##########Zadanie 2
# ### Sprawdź czy w poniższym zbiorze występuje gen 'FGFR4' oraz 'FGERA4', jeśli tak to wskaż index
# ### genu na liście
#
lista_gene1 = ['SLC19A2', 'ATP7B', 'ERBB3', 'FGFR14', 'ABCC3','GALNT14', 'ERCC1',
                'LJS19A2', 'AKM7B', 'ELLB34', 'FULR4', 'ANGC3', 'WELNT14', 'EOO1',
                'SAC19A22', 'FGFR4', 'ERB3', 'FGR4', 'FGFR4', 'GASNT14', 'ERSS4']

genes = ["FGFR4", "FGERA4"]

for gene in genes:
    if gene in lista_gene1:
        print(lista_gene1.index(gene))


####################Łańcuchy znaków
## Zapoznaj się z wybranymi metodami dla typu string
## więcej metod znajdziesz tu: https://pl.python.org/docs/lib/string-methods.html
## s.endswith(przyrostek[, początek[, koniec]]) - sprawdzenia, czy napis jest zakończony napisem przyrostek
## s.index(napis[, początek[, koniec]]) - indeks wystąpienia napisu
## s.isalpha() - czy wszystkie znaki napisu są literami i napis składa się przynajmniej z jednego znaku.
# s.capitalize() - zmienia pierwszą literę na dużą\\
# s.center(długość) - Centruje napis w polu o podanej długości\\
# s.count(sub) - zlicza wystąpienie podciągu sub w napisie s\\
# s.encode(kodowanie) - zwraca zakodowaną wersję napisu ('utf-8', 'ascii', 'utf-16')\\
# s.isalnum() - sprawdza czy wszystkie znaki są znakami alfanumerycznymi\\
# s.isdigit() - sprawdza czy wszystkie znaki są cyframi\\
# s.islower() - sprawdza czy wszystkie litery są małe\\
# s.isspace() - sprawdza czy wszystkie znaki są białymi znakami\\
# s.isupper() - sprawdza czy wszystkie litery są duże\\
# s.join(t) - łączy wszystkie napisy na liście t używając s jako separatora\\
# s.lstrip() - usuwa początkowe białe znaki\\
# s.replace(old, new) - zastępuje stary podciąg nowym\\
# s.rstrip() - usuwa końcowe białe znaki\\
# s.split(separator) - dzieli napis używają podanego separatora\\
# s.strip() - usuwa początkowe i końcowe białe znaki\\
# s.upper() - Zwraca kopię napisu z wszystkimi literami zamienionymi na wielkie litery.

#### Przykład
# word = 'Python jest super, każdy to wie'
# print(word.capitalize())
# print(word.count('super'))
# print(word.endswith('per'))
# print(word.index('super'))
# print('-'.join(word))
# print(word.split(' '))
# print(word.upper())

#####Zadanie 3
## Przekopiuj dowolny ale długi fragment tekstu ze strony:
## http://www.national-geographic.pl/ludzie/dziennikarka-kontra-komputer-kto-napisze-lepszy-tekst
## sprawdź:
## a) ile razy w tekście występuje słowo Emma
## b) zamień całość tekstu na duże litery
## c) wstaw poszczególne wyrazy jako elementy listy
## d) ile zdań jest w analizowanym tekście?

tekst = "Któregoś dnia w zeszłym tygodniu dokładnie o 9:29 pochyliłam się nerwowo nad klawiaturą komputera gotowa do walki ze sztucznym tworem o nazwie Emma."
print(tekst.count("Emma"))
tekst = tekst.upper()
print(tekst)
word_list = tekst.split()
print(word_list)
print(len(tekst.split(" ")))

######################################
#################Instrukcje sterujące tj. instrukcje warunkowe i pętle
 ################# 1. Instrukcja warunkowa "IF"#########struktura
# if warunek_1:
#     #lista instrukcji         # odstęp/wcięcie w programie 4 spacje lub 1 tablulacja
# elif warunek_2:
#     #lista instrukcji
# elif warunek_3:
#     #lista instrukcji
#     ...
# else:                          # każdy inny przypadek
#     #lista instrukcji

######################Przykład ########################
# liczba = int(input('Ile punktów dostałeś z wejściówki'))
# if liczba == 5:
#     print('Ocena 5')
# elif liczba == 4:
#     print('Ocena 4')
# elif liczba == 3:
#     print('Ocena 3')
# else:
#     print('Wejściówka do poprawy')


########Zadanie 4
## Sprawdź czy dowolnie podana przez użytkownika liczba jest parzysta czy nieparzysta
liczba = int(input("Podaj liczbe "))

if liczba % 2 == 0:
    print(f"Liczba {liczba} jest parzysta.")
else:
    print(f"Liczba {liczba} jest nieparzysta.")

#################Instrukcje sterujące tj. instrukcje warunkowe i pętle  Teoria
################# 1. Instrukcja warunkowa "MATCH"#########struktura
# match zmienna:
#     case wartość zmiennej 1:
#         blok instrukcji
#     case wartość zmiennej 2:
#         blok instrukcji
# ....
#     case wartość zmiennej n:
#         blok instrukcji

## Przykład 

#dane_osobowe = input('Wpisz "PESEL" albo "nazwisko"'))
#match dane_osobowe:
#    case "PESEL":
#        print('781123242622')
#    case "nazwisko":
#        print('Kowalska')


########Zadanie 5
## W zależności od procentu uzyskanych punktów z kolokwium z Python'a
## student uzyskuje określoną ocenę końcową z laboratorium
## np 50%-60% to 3.0, 61%-70% to 3.5, ...., 91%-100% to 5.0 - if
## np 50% to 3.0, 61% to 3.5, ...., 91% to 5.0 - match
## Korzystając z instrukcji match, napisz program który będzie wyznaczał ocenę studenta na podstawie uzyskanych punktów (max 15pkt)
# Pobranie liczby punktów od użytkownika
punkty = int(input("Podaj liczbe punktow (max 15): "))

# Obliczenie procentowego wyniku
procent = (punkty / 15) * 100

# Przypisanie oceny na podstawie przedziałów procentowych
match procent:
    case p if 50 <= p <= 60:
        print("Ocena: 3.0")
    case p if 61 <= p <= 70:
        print("Ocena: 3.5")
    case p if 71 <= p <= 80:
        print("Ocena: 4.0")
    case p if 81 <= p <= 90:
        print("Ocena: 4.5")
    case p if 91 <= p <= 100:
        print("Ocena: 5.0")
    case p if p < 50:
        print("Niezaliczone")
    case _:
        print("Wprowadz poprawna liczbe punktow (0-15)")
########### Pętla for  - jako wektor

# for i in wektor:  # wektor tworzymy korzystając z funkcji range(początek,koniec)
#     instrukcje
#
# print(list(range(0,5)))  # range(0,5) --> i przyjmuje wartości kolejno 0,1,2,3,4
##########Przykład
# for i in range(1, 6):
#     print('Python')

################# Pętla for - po kolekcji
## for x in kolekcja:      uwaga: elementy kolekcji moga być dowolnego typu,
##     instrukcje           #nie musi to być wektor liczb.

################Przykład #########################################
# for i in ['Ala','Ola','Tola']:
#     print(i)
#######################################################################################3
# # #Zadanie 6
### Napisz skrypt, ktory obliczy sume ciagu: 1+1/2+1/3+...+1/n korzystając z pętli for
### Zmienna wejsciowa n jest dowolnia, m-parametr wprowadzany jako dane wejsciowe przez uzytkownika (użyj input)
### Write a program that calculates the sum of the sequence: 1+1/2+1/3+...+1/m using the for loop.
### The input variable m is arbitrary. The m-parameter is provided as input by the user (use input).

################# Pętla while
# while warunek:  # pętla działa dopóki warunek jest prawdziwy
#     instrukcje
# while condition:  # the loop runs as long as the condition is true
#     instruction
############## Przykład ###########################################
# i = 0   # i to zmienna tzw iterator który w każdym kroku zwykle zmienia się o jakąś wartość np.  o 1
# while i < 5:
#    print('I like python')
#    i += 1      # equivalent to i = i + 1

###### Zadanie 7
###### Calculate the root of the numbers from 1 to 10 using the while loop
###### Oblicz pierwiastek liczb od 1 do 10 korzystając z pętli while

### Jeśli masz problem z tłumaczeniem treści użyj https://www.deepl.com lub poproś o dodatkowe wyjaśnienie

###### Task 8
###### Write a program which takes 3 digits: a, b, c as input and
###### calculate the roots of a quadratic equation ax^2 + bx + c = 0

###### Task 9
##### Write a program, which will find all such numbers between 1 and 1000 (both included) such
##### that each digit of the number is an even number the numbers obtained should be printed 
### in a comma-separated sequence on a single line.

################ Methods versus function (metoda vs funkcja)
#### Example
# a = [2, 70, 5, 6]
# a.sort()   # wywołanie metody na obiekcie
# print(a)

# a = [2, 70, 5, 6]
# a = sorted(a)  # override of a variable (nadpisanie zmiennej)
# print(a)

###### Generally, methods and functions have one or more parameters
###### (Metody i funkcje często mają jeden lub więcej parametrów)

#### Example
# a = [2, 70, 5, 6]
# a.sort(reverse=True)
# print(a)
#
# a = [2, 70, 5, 6]
# a = sorted(a, reverse=True)  # override of a variable
# print(a)

######## Function: break() and continue()
## the break() function is often used to stop loops (for, while)
## the continue() function allows to leave a block of instructions and return to the beginning of the loop

## Funkcja break() jest używana często do zakończenia pętli (for, while)
# podczas gdy funkcja continue() pozwala opuścić blok instrukcji i wrócić do początku pętli.

#### Example: the program only prints the numbers 0 1 2 3 4

# list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# licz = 0
# while licz in list_1:
#     print(list_1[licz]),
#     licz += 1  # licz = licz + 1
#     if licz >= 5:
#         break

####### Example: the program prints out only odd numbers: 1 3 5 7 9
# for x in range(1, 10):
#     if x % 2 == 0:  # Sprawdź, czy x jest parzystą liczbą
#         continue
#     print(x)


# # ################################ Task 10
## Write a program using if statement, for loop, break(), continue() which takes 2 digits: x, y as input and
###### calculate multiplication x*y. The program stops working if x or y is equal to 0.
## Korzystając z instrukcji sterujących napisz program który będzie wczytywał kolejno z klawiatury 2 liczby,
## a następnie obliczał i wyświetlał na ekranie iloczyn wprowadzonych przez użytkownika liczb,
## program kończy działanie jeżeli uzytkownik wprowadzi cyfrę 0. Użytkownik może wykonać obliczenia tylko na
## liczbach całkowitych (wstaw odpowiedni warunek).

## # ################################ Task 11
## Napisz program, który wyświetli twoje imię i nazwisko jeżeli użytkownik poda
## właściwe hasło, jedno z 2 do wyboru, (hasła są przechowywane w krotce)

## Write a program that will display your name if the user enters the correct
## password (the password is stored in a variable)

############################## Python module random
## Random module implements pseudo-random number generators for various distributions.

### Example:  random - returns a random float number between 0 and 1
# import random     # generator liczb losowych
# print(random.sample(range(10000),4))
# print(random.choice(range(10000)))

################################## Task 12
## Generate list with 100 random numbers (integer type)
## Ascending sort these odd numbers and print only odd numbers from list.

## Wygeneruj listę złożoną z 100 liczb całkowitych parzystych i nieparzystych
## wypisz wszystkie liczby parzyste z tablicy liczby, od najmniejszej do największej.
## Do losowania liczb wykorzystaj moduł random patrz przykład poniżej

#################### One line if/else statement in Python
########### Example
## Syntax/Składnia: <expression1> if <condition> else <expression2>
## Option 1
# a = 20
# b = 1
# print('większe') if a > b else print('mniejsze')

# Option 2
# a = 1
# b = 20
# x = a > b and print('większe') or print('mniejsze')

# Option 3
# age = 21
# print(('adult', 'kid')[age < 20])  # choice from the tuples

# Option 4
# age = 21
# print(('adult', 'kid')[True])

############### Task 13
## Uprość kod z Zadania 11 korzystając w w/w struktur
## Simplify the code from Task 11 using a one line if/else statement


################################## Python function
## Syntax: def function_name(input_argument1, input_argument2, ... ,input_argumentN):
##       instructions
##      return output_argument   or  return output_arguments
##
##
## Calling the function (wywołanie funkcji )
## name_function(value of input_argument1, ... ,value of input_argumentN)

### Example

# def sum_numbers(x, y):
#     sum_xy = x + y
#     return sum_xy

# print('Result is equal:', sum_numbers(3,5))

#################### Task 14
## Write a function that calculates the quotient of 3 even numbers
## Utwórz funkcje która obliczy iloraz 3 parzystych liczb, użyj "one line statement"

