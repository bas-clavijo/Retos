"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
- las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""
#Un anagrama es algo que contiene las mismas palabras pero de forma desordenada
#Un palíndromo es una palabra que se puede leer de la misma forma al derecho y al reves

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram("Amor", "Roma"))