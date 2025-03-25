
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

 ################## Dokumentacja  (docstrings) ########################################
################################################################################
#
# Dla zachowania czytelności i jednolitości kodu stosuj określoną gramatykę kodu, w pythonie
# najczęściej stosuje się konwencję opisaną w dokumencie PEP 258
# Wykonaj dokumentację kodu (dla funkcji, modułu)
# Stosuj obsługę wyjątków

# #################### Przykład 1 - dokumentacja funkcji (Google style)
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

####################  Python function:  anonymous function lambda()
#########  Funkcja anonimowa lambda()
## Syntax:     lambda input_arguments: instruction

################# Example
# resultLambda1 = lambda x, y: x + y
# print('Wynik wywołania funkcji lambda:', resultLambda1(3,5))
################# Example
# name = 'Ala'
# resultLambda2 = lambda oneWord: oneWord.upper()
# print(resultLambda2(name))

# ########################## Task 1
# Utwórz listę złożoną z pojedynczych liter swojego imienia następnie korzystając
# z funkcji lambda połącz kolejne litery w jeden wyraz (swoje imie)

# ########################## Task  2
# Przypisz do zmiennej wartość która będzie twoim imieniem i nazwiskiem następnie korzystając
# z funkcji lambda rozdziel wyraz na poszczegolne wyrazy, a potem wyrazy na litery
# użyj funkcji list i metody split - dla zmiennych typu string

##############################################################
######### Function:  map(), zip(), reduce() i filter()

####### Function map()##################
## Funkcja map() wykonuje operacje z użyciem funkcji na każdym elemencie listy/tupli/słownika:
## Syntax: map(function_name, iter)
## function_name - name of function with one input parameter
## iter is list or dictionary or tuples
## output parameter of mam is list type.
## map() realize operation by using function on each elements of list/tuple/dictionary

######### Example: construct your own function + map()

# def power(number):
#     result = number**2
#     return(result)
#
# list_number = [2, 10, 15, 100, -5]  # equivalent to [double(n) for n in listNumber]
# result_map = map(power, list_number)

# print(list(result_map))  # dump to list

######### Example: construct lambda() + map()

# list_word = ['dnA','RnA']
# print(list_word)
# upper_letter = lambda one_word: one_word.upper()
# result_lambda = map(upper_letter, list_word)  # equivalent to map(lambda one_word: one_word.upper(), list_word)
# print('Result: ', list(result_lambda))

##### Function zip()##########################################################################
# zip() creates pair of elements (tuples) from two list
# zip() tworzy za to listę tupli z podanych elementów

######### Example
# list1 = [1,3,5]
# list2 = [2,4,6]
# resultZip = zip(list1, list2)
# print(list(resultZip))

##### Function reduce()######################################################################
## Funkcja reduce() pobiera dane z sekwencji i zwraca na ich podstawie pojedynczą
## wartość np. sumę liczb. Struktura: functools.reduce(function0, sequence, [initial_value]);
## reduce() realizuje operacje zdeklarowane w function0 na pierwszych dwóch elementów sekwencji, następnie
## wykonuje function0 dla wyniku i trzeciego elementu, aż do wyczerpania elementów sekwencji
## Znajduje się w pakiecie functools

## The reduce(fun,seq) function is used to apply a particular function passed
## in its argument to all of the list elements mentioned in the sequence passed along.
## This function is defined in “functools” module.

######## Example
# import functools, operator
# resultLambda1 = lambda x, y: x + y
# list1 = [1,2,3,4]
# resultReduce1 = functools.reduce(resultLambda1, list1,0)
# print(resultReduce1)

######## Example
## np.można wykorzystywać szereg operacji z użyciem wbudowanych funkcji
## You can use the following operations available as a function:
## Math operations: add(), sub(), mul(), floordiv(), abs()
## Logical operations: not_(), truth()
## Bitwise operations: and_(), or_(), invert()
## Comparisons: eq() -> equal to, ne() -> not equal, lt()->less than,
## le()-less or equal, gt() -> greater than, and ge() -> greater or equal
## Object identity: is_(), is_not()

# import functools, operator
# list2 = [1,2,3,4]
# resultReduce2 = functools.reduce(operator.mul, list2, 1)
# print(resultReduce2)


##### Function filter()########################################################
##Funkcja filter filtruje elementy sekwencji przy użyciu podanej funkcji,
## która musi zwracać wartość True lub False:

## The filter() method filters the given sequence with the help of a function
## that tests each element in the sequence to be true or not.
## Syntax: filter(function, sequence)

######### Example
# list1 = [1,2,3,4]
# def even(x):
#  if x%2 == 0:
#     return True
#  else:
#     return False
#
# resultFilter = filter(even, list1)
# print(list(resultFilter))

########### Function enumerate
## Enumerate() adds a counter to an iterable and returns it in the form of the enumerating object.
##
# def main():
#     print("#### function enumerate ###")
#     a = ['a', 'b', 'c']
##    b = [(0, 'a'), (1, 'b')] # sprawdź poniższe również dla zmiennej b
#
#     for i in enumerate(a):
#         print(i)        # [(0, 'a'), (1, 'b')]
#
#     print("#######")
#     for i in enumerate(a):
#         for j in i:
#             print('j element:', j)
#     print("#######")
#     for i in enumerate(a):
#         for j in i[1]:
#             print('j element:', j)
#
# if __name__ == '__main__':
#     main()



# ########################## Task 3
# # Utwórz funkcję która w dowolnym wyrazie (1 argument funkcji)
# # znajdzie dowolną literę (2 argument funkcji)
## użyj lammbda()
# ########################## Task 4
## Utwórz dwie listy, do każdej z nich niezależnie zapisuj odpowiednio
## podawane przez użytkowników login (pierwsza lista) i hasło (druga lista),
## operacja zapisu jest powtarzana aż do momentu wpisania przez użytkownika "STOP"
## użyj break, continue, enumerate().
## Następnie login-y i hasła zapisz do słownika (login to klucz słownika).

# ########################## Task 5  - Module in Python
# # # Zmodyfikuj poprzednie zadanie, tworząc a następnie importując moduł
# # #Utwórz funkcje Poziom: która rysuje gwiazdki poziomo, liczbę gwiazdek podaje użytkownik jako argument funkcji')
# # #Utwórz funkcje Pion: która rysuje gwiazdki pionowo, liczbę gwiazdek podaje użytkownik jako argument funkcji')
# # obie funkcje są z modułu o nazwie stars

# # Korzystając z modułu stars i funkcji Pion Poziom wypisz litery: E, L

# ########################## Task 6
# # utwórz moduł o nazwie sil, w którym znajdzie się funkcja silnia (użyj lammbda), a następnie korzystając z
# modułu sil, oblicz symbol Newtona dla dowolnych 2 liczb wskazanych przez
# użytkownika(http://www.fizykon.org/wzory/wzory_matem_kombinatoryka.htm)

# ########################## Task 7
# # Write a script to filter out only the even items from a list (i.e. made from range(1, 100))
# # using filter() and lambda functions.
# #  The numbers obtained should be printed in a comma-separated sequence on a single line.

# ########################## Task 8
#### Write a script, using reduce(), which will multiply elements in range (1, 100)

# ########################## Task 9
### Write a program which will find all such numbers which are
### divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included)
### use filter

# ########################## Task 10
### Write a program which will find all such numbers which are
### divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included)
### use lambda, filter

# ########################## Task 11
#  # # Utwórz funkcje Poziom: która rysuje gwiazdki poziomo, liczbę gwiazdek podaje użytkownik
##### jako argument funkcji
# # # Utwórz funkcje Pion: która rysuje gwiazdki pionowo,
# ### liczbę gwiazdek podaje użytkownik jako argument funkcji')
# # # Korzystając z w/w funkcji narysuj litery: E, L
### Użyj lambda, użyj wbudowanych funkcji, skróć maksymalnie kod programu, użytkownik, jako wejściowy argument podaje litere E lub L  