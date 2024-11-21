from typing import Callable, Generator
print("funcao")

print("")
minhaLista = [3, 3, 3, 4, 3]
print("funcao com retorno")
def superSoma(list_of_numbers):
    my_sum = 0

    for number in list_of_numbers:
        my_sum += number

    return my_sum


return_sum = superSoma(minhaLista)
print(return_sum)


print("")
print("funcao lambda = anonima / essa função não precisa de nome")


soma: Callable[[int, int], int]  = lambda a, b : a+b

r = soma(4, 6)
print(soma(4, 6))
print(r)


mult = lambda a,b,c: (a+b)*c

r = mult(4, 6, 5)
print(r)

print("")
print("chamando e executando funcao lambda")

print((lambda a,b: a-b)(4,2))

print("")
print("passando funcao por paramentro na funcao lambda")
soma_lambda = lambda x, func: x+func(x) # depois essa
resultado = soma_lambda(4, lambda x: x*x) # primiero ele execulta essa lambda
print(resultado)

import time


def infinite_stream(start: int) -> Generator[int]:
    while True:
        start += 1
        time.sleep(2)
        yield start
      


for start in infinite_stream(5):
    print(start)
    if start == 10:
        break