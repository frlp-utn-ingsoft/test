def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def es_par(n):
    return n % 2 == 0


def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def maximo(lista):
    if not lista:
        raise ValueError("La lista está vacía")
    return max(lista)


def minimo(lista):
    if not lista:
        raise ValueError("La lista está vacía")
    return min(lista)


def promedio(lista):
    if not lista:
        raise ValueError("La lista está vacía")
    return sum(lista) / len(lista)


def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    if n == 0:
        return 1
    return n * factorial(n - 1)


def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]


def contar_palabras(frase):
    return len(frase.strip().split())


def invertir_lista(lista):
    return lista[::-1]


def eliminar_duplicados(lista):
    return list(set(lista))


def contiene_elemento(lista, elemento):
    return elemento in lista
