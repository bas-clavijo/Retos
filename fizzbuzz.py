"""
EL FAMOSO "FIZZ BUZZ”:
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""

def fizz_buzz():
    for index in range(1,101):
        if index %3 == 0 and index %5 ==0:
            print("FizzBuzz")
        elif index %3 ==0 :
            print("Fizz")
        elif index %5 ==0 :
            print("Buzz")
        else:
            print(index)

#siempre se debe de llamar a la funcion
fizz_buzz()
