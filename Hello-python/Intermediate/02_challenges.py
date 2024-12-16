## Challenges

'''
FIZZ BUZZ
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
'''

def fizzbuzz():
    # Rango de 1 a 100
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print("fizzbuzz") 
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")   
        
        else:
            print(i)
fizzbuzz()

'''
/*
    Es un anagrama
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
'''   
def is_anagram(word_one,word_two):
    if word_one.lower()==word_two.lower():
        return False
    return sorted(word_one.lower()) == sorted(word_two.lower())

print(is_anagram("Amor","roma"))

'''
Succesion de Fibonacci
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
'''
def Fibonacci():
    prev = 0
    next = 1
    for i in range(0,50):
        print(prev)
        fib=prev+next
        prev=next
        next=fib
    
Fibonacci()
    
    
'''
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
'''

def es_primo():
    for n in range(1,101):
        if n>=2:
            div=False
            
            for i in range(2,n):
                if n%i==0:
                    div=True
                    
            if not div:
                print(n)
        
es_primo()

'''
INVERTIR CADENA
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
'''
def invertir_cadena(texto):
    revere_text = ""
    for i in range (0,len(texto)):
        revere_text +=texto[len(texto)-i-1]  
    return revere_text
    
print(invertir_cadena("Hola mundo"))