# #################### Przypomnijmy dokumentację funkcji (Google style) z poprzednich zajęć
# def divide(x: int,y: int) -> float:
#   """
#   Funkcja dzieli liczbę x przez liczbę y
  
#   Args:
#     x (int): dzielna
#     y (int): dzielnik
    
#   Returns:
#     wynik dzielenia x/y
    
#   """
#   result = x/y
#   return(result)

# print(divide(2,3))
# print(divide(x = 1, y = 2))
# help(divide)
# print(divide.__doc__)
################################################################################

'''
###################################################################################################################
Dziś zajęcia dotyczą tworzenia funkcji ze zmienną liczbą argumentów wejściowych.
Przed realizacją zadań koniecznie zapoznaj się ze slajdami prezentacji do Wykładu 3 

Dodatkowe linki do filmów, które ułatwią Ci zrozumienie materiału z laboratorium:
"Co oznacza zapis *args oraz **kwargs w funkcjach?"   -  https://www.youtube.com/watch?v=7nwXBWzkqNU
####################################################################################################################

'''
############################### Teoria: Funkcja z dowolną liczbą argumentów wejściowych (*args)  #########################
### def nazwa_funkcji(*args):
###    instrukcje
##     return obiekt                 *args - krotka argumentów pozycyjnych

###### Wyrażenie “args” bierze się z od słowa “arguments” czyli argumenty i jest to zazwyczaj zmienna,
###### która zawiera tuple argumentów pozycyjnych. Wyrażenia z jedną gwiazdką (*) używamy gdy do funkcji
### chcemy przekazać dowolną liczbę argumentów pozycyjnych (czyli takich dla których
### przy wywołaniu funkcji nie podajemy ich nazwy, a przypisanie wartości bazuje na kolejności argumentów dlatego
### args - argumenty umieszczane są w krotce/tupli po której możemy iterować args[0], args[1] itd.
## używamy *args gdy nie są istotne dla nas nazwy zmiennych
### Pamiętaj aby parametr *args umieszczać na końcu listy parametrów w definicji funkcji!


################################## Example suma dowolnego ciągu cyfr
# def suma(*args):
#     if not args:                        # wkazane jest kontrolowanie przypadku braku argumentów
#         return('brak argumentów')
#     return(sum(args))
#
# print(suma(1,2,3))
# print(suma(1,2,3,4,5,6))


################################### Example suma dowolnego ciągu cyfr plus wartość stałej
# def suma2(x,*args):
#     sumaLiczb = x + sum(args)
#     return(sumaLiczb)
#
# print(suma2(100,1,2,3))

#################################### Example suma pierwszych 4 cyfr dowolnego ciągu cyfr
# def suma3(*args):
#     if bool(args):
#         sumaLiczb = args[0] + args[1] + args[2] + args[3]
#     else:
#         sumaLiczb = 0
#     
#      print(sumaLiczb)
#     return(None)
#
# suma3(1,2,3,4,5,6,7,8,9,10)
# suma3()

#########################################################################################################
#############funkcje z dowolną liczbą argumentów kluczowych (**kwargs) ############
### ** kwargs pozwala przekazywać zmienną długość argumentów ze słowami kluczowymi do funkcji.
### W przypadku gdy do naszej funkcji chcemy przekazywać argumenty, które wyróżniają
### się nazwą możemy użyć parametru z dwoma gwiazdkami (**).
### Przekazane w ten sposób argumenty są dostępne w funkcji w postaci słownika.
### Jego pary klucz-wartość stanowią nazwa i wartość przekazanego argumentu.
### używamy **kwargs gdy istotna dla nas jest nazwa zmiennych

# def nazwa_funkcji(**kwargs):
#     instrukcje
#     return obiekt                 # kwargs - słownik argumentów kluczowe

######## wstaw jako argument funkcji:  *kwargs  ########################################

## “kwargs” z j.ang. “keyword arguments” czyli argumenty nazwane
## i zmienna taka zawiera pary nazwa-wartość argumentu.

#################### Example ###### 
# def slownik(**kwargs):
#    for klucz, wartosc in kwargs.items():
#        print(klucz, wartosc)
#
# slownik(a=1, b=2, c=3)

# def witaj(**kwargs):
#     for key, value in kwargs.items():
#         print("{0} = {1}".format(key, value))
#
# witaj(name="yasoob")
################################################################################
## Function with multiple arguments: args, kwargs
################################################################################

################################## Example 1:  sum of a sequence of numbers
# def suma(*args):
#     if not args:                        # case: no input parameters
#         return('no parameters')
#     return(sum(args))
#
# print(suma(1,2,3))
# print(suma(1,2,3,4,5,6))


############# Example 2: Sum of arithmetic sequence
## functional requirements:  
##  minimum number of input parameters: 1

# def suma2(x,*args):
#     sumaLiczb = x + sum(args)
#     return(sumaLiczb)
#
# print(suma2(100,1,2,3))

############  Example 3:   Sum the first four elements of arithmetic sequence
## functional requirements:  
##  minimum number of input parameters: 4

# def sum2(*args):
#     if bool(args):
#         sumaLiczb = args[0] + args[1] + args[2] + args[3]
#     else:
#         sumaLiczb = 0
#     
#      print(sumaLiczb)
#     return(None)
#
# sum2(1,2,3,4,5,6,7,8,9,10)
# sum2()

############  Example 3:   Sum the three elements 
## functional requirements:  
## minimum number of input parameters: 3
## user enter the name of input parameters

# def dict1(**kwargs):
#    for klucz, wartosc in kwargs.items():
#        print(klucz, wartosc)
#
# dict1(a=1, b=2, c=3)

############  Example 4: Say hello to a friend
## functional requirements:  
## minimum number of input parameters: unknown
## name of input parameters: unknown

# def hello(**kwargs):
#     for key, value in kwargs.items():
#         print("{0} = {1}".format(key, value))
#
# hallo(firstname="John", secondname='Smith')
# hallo(user="John")

############  Example 5: unpack list

# list_arg = [1, 3, 5]
#
# def unpack1(arg1, arg2, arg3):
#     print(arg1)
#     print(arg2)
#     print(arg3)
#
#
# unpack1(*list_arg)     
#####################################################
################################################################################
################################################################################
############  Example 6:
### Zapoznaj się z przykładem sumowania liczb w różnej kombinacji i ilości argumentów wejściowychdef 

# def funckcja1(x = 0,y = 0,*args,**kwargs):
#     if len(args) == 0 and len(kwargs.keys()) == 0: suma = x + y
#     if len(args) > 0 and len(kwargs.keys())==0: suma = x + y + sum(args)
#     if len(args) == 0 and len(kwargs.keys())>0: suma = x + y + sum(kwargs.values())
#     if len(args) > 0 and len(kwargs.keys()) > 0: suma = x + y + sum(args) + sum(kwargs.values())
#     return suma

# print(funckcja1())
# print(funckcja1(x=1,y=1))
# print(funckcja1(x=1,y=1,a=1,b=1))
# print(funckcja1(1,1,3,3))
# print(funckcja1(1,1,3,3, a = 2, b = 2))

########################################## Zapamiętaj:
#### 1. “args” i “kwargs” możesz zastąpić dowolnymi innymi nazwami zmiennych
#### 2. Pamiętaj umieszczając w definicji funkcji wyrażenie z jedną lub dwoma asterisk-mi (gwiazdkami)
### pozwalamy na przekazywanie do niej argumentów w dowolniej liczbie i nazwie.
### bez konieczności konkretnego określenia tych parametrów.
### 3. Pamiętaj o kolejności – wyrażenie **kwargs
### musi być na końcu, *ars wcześniej, a pozostałe zdefiniowane argumenty na początku.


#### Asterisk * możesz również używać w wywołaniu funkcji.
#### Jest to tak zwane rozpakowywanie list i słowników z argumentami.
#### Jeżeli funkcja przyjmuje kilka argumentów i posiadasz listę,
#### która zawiera argumenty, które chcesz przekazać do tej funkcji
#### wystarczy poprzedzić nazwę listy gwiazdką zamiast podawać kolejne argumenty ręcznie.

# list_arg = [1, 3, 5]
#
# def rozpakowywanie(arg1, arg2, arg3):
#     print(arg1)
#     print(arg2)
#     print(arg3)
#
#
# rozpakowywanie(*list_arg)     # odpowiednik dużo dłuższego kodu:   rozpakowywanie(list_arg[0], list_arg[1], list_arg[2])
########################## Zadania do wykonania
# # ################################ Task 0
# '''
## Write a function which will find all such numbers which are divisible by 7 but
## are not a multiple of 5  in range  from x to y (both included).
## The numbers obtained should be printed in a comma-separated sequence on a 
## single line. Don't forget about function documentation
#
# '''
# ##### do testów możesz użyć:
# x = 1000
# # y = 2101
# # my_list = list(range(x,y,1))
# # print(my_list)
#
# ''

# def checknum(*xy) -> None:
#     """
#     Funkcja sprawdza czy liczby z przedzialu od xy[0] do xy[1] sa podzielne przez 7 i nie sa iloczynem z 5 i wypisuje te liczby na ekran

#     Args:
#         xy[0] (int): Pierwsza liczba z przedzialu
#         xy[1] (int): Druga liczba z przedzialu
#     """
#     for i in range(xy[0], xy[1]):
#         if i % 7 == 0 and i % 5 != 0:
#             print(f"{i}, ")

# checknum(1, 999)
# # ################################ Task 1
## A website requires the users to input username and password to register. 
## Create function to check the validity of password input by users.
## Using continue() or break().
## Following are the criteria for checking the password:
## 1. At least 1 letter between [a-z]
## 2. At least 1 number between [0-9]
## 3. At least 1 letter between [A-Z]
## 4. Minimum length of transaction password: 4
## 5. Maximum length of transaction password: 8
## You should to document your code by using python docstrings (google)
## Save result to *.txt file

# def validate(**creds) -> bool:
#     """
#     Zwraca False w przypadku, gdy haslo nie spelnia wymagan biezpieczenstwa

#     Args: 
#         creds[0] (str): Login
#         creds[1] (str): Password
#     """

#     if len(creds["password"]) < 4 or len(creds["password"]) > 8: return False
#     if len(set("abcdefghijklmnopqrstuvwxyz") & set(creds["password"])) == 0: return False
#     if len(set("abcdefghijklmnopqrstuvwxyz".capitalize()) & set(creds["password"])) == 0: return False
#     if len(set("0123456789") & set(creds["password"])) == 0: return False

#     f = open("temp_validation_res.txt", "wt+")
#     f.write("VALIDATED:\n")
#     for a, v in creds.items():
#         f.write(f"{a}: {v}\n")
#     f.close()


#     return True

# print(validate(login = "login", password = "123"))
# print(validate(login = "login", password = "abcde"))
# print(validate(login = "login", password =  "ABCDeq12"))



################ Task 2
## Write a function which will find all such numbers which are divisible by 7 but
## are not a multiple of 5  in range  from x to y (both included).
## The numbers obtained should be printed in a comma-separated sequence on a 
## single line. 
## You should to document your code by using python docstrings 
## (dokumentacja kodu styl google)
## Wykonaj na Lab6:  Don't forget to handle exceptions (obsłudze wyjątków)
## Save result to *.pkl file use picle package
# '''
# ##### do testów możesz użyć:
# x = 1000
# # y = 2101
# # my_list = list(range(x,y,1))
# # print(my_list)
# 

import pickle
def checknum(*xy) -> None:
    """
    Funkcja sprawdza czy liczby z przedzialu od xy[0] do xy[1] sa podzielne przez 7 i nie sa iloczynem z 5 i wypisuje te liczby na ekran

    Args:
        xy[0] (int): Pierwsza liczba z przedzialu
        xy[1] (int): Druga liczba z przedzialu
    """
    try:
        for i in range(xy[0], xy[1]):
            if i % 7 == 0 and i % 5 != 0:
                print(f"{i}, ") # TODO dopracowac
                p = open("temp_checknum.pkl", "wt")
                p.write(f"{i}, ")
    except TypeError as e:
        print("Blad:", e)

checknum(1,999)
################ Task 3
## Create function with multiple arguments (x1,x2,...,xn) that accepts a sequence of 
## comma-separated numbers from console and returns:
## x1^x1  if number of input parameters equals 1 than y = x1^x1 
## x1^x1, x2^x2 if number of input parameters equals 2
## x1^x1, x2^x2, x3^x3 if number of input parameters equals 3  
## .... 
## x1^x1, ... , x99^x99 if number of input parameters equals 99 
## if number of input parameters equals greater than 100 will display an error message.
## Requirements: 
## Name of input parameters: 
## You should to document your code by using python docstrings (google)
############### 

################ Task 4
## Create function with multiple arguments (x1,x2,...,xn) that accepts a sequence of 
## comma-separated numbers from console and returns:
## x1^x1  if number of input parameters equals 1 than y = x1^x1 
## x1^x1, x2^x2 if number of input parameters equals 2
## x1^x1, x2^x2, x3^x3 if number of input parameters equals 3  
## .... 
## x1^x1, ... , x99^x99 if number of input parameters equals 99  
## if number of input parameters equals greater than 100 will display an error message.
## Requirements: 
## Use: dynamic variable name (exec() or globals() or locals())
## Name of input parameters: x1, x2, ..., xn
## You should to document your code by using python docstrings (google)
## Wykonaj na Lab6:  Don't forget to handle exceptions (obsłudze wyjątków)
###############

########################## Task 5 ########################
## The first step, 
## generate test data: create folder. Create 5 text files to this folder, 
## each file contains more than 5 sentences. 
## Filenames: Text1ID_ABC, Text2ID_405.txt, Text3ID_607.txt, Text4ID_ABC5.txt, Text5ID_DEF.txt
##
## Create function with multiple arguments that:
## a) print all file from folder
## b) if the file name contains 'ABC', count how many words in the text of file 
## contain words with more than 3 letters   
## Wykonaj na Lab6:  Next step, decorate this function, add the following functionality:
## a) the function will check how many files have 0 in the filename 
## b) if the file has 0 in the filename then the function counts words in the text of the file 
## c) if the filename contains 'EF.txt', then the function copy this file to 
## 'DocumentLab5copy' directory






