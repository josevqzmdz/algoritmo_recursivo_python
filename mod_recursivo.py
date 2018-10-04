'''
Generar una secuencia de numeros enteros por medio del siguiente metodo recurviso:

X[i+1] = (ax + c)mod(m)

donde
    i = 0
    x0 = semilla
    a = constante a multiplicar
    c = constante aditiva
    m = modulo

    x0 > 0; x[i+1] > 0; a > 0; C > 0; m > 0

    todo s tienen que ser numeros enteros

La operacion "mod(m)" significa multiplicar Xi * a, sumar C y dividir el resultado
entre m para obtener el residuo x[i+1], es importante señalar que la ecuacion
recursiva del algoritmo congruencial lineal genera una secuencia de numeros enteros
es:

S = { 0, 1, 2, 3... m-1 }

Para obtener numeros pseuco-aleaorios en el intervalo {0, 1}, se requiere la siguiente
ecuacion.

r[i] = x[i] / m-1

'''
import math
def algoritmo_recursivo(xi, k, g, c, r, iteracion):

    if (xi == 1):
        print("la variable a calcular regreso 1")
        return 1

    elif iteracion == 10:
        print("iteraciones finalizadas")
        return -1
    else:

        mod = ((xi * a) + c) / m
        sig = mod - math.floor(mod)
        # floor redondea una fraccion a su entero menor mas cercano
        # ( floor(1.99) = 1, floor(2.23) = 2...)
        # http://www.php2python.com/wiki/function.floor/
        r.append(sig)

        print("iteracion #", iteracion)
        print("(", a," * ", xi, " + ", c, ")mod(", m, ") = ", mod)
        print("r(", iteracion, ") = ", r[iteracion])
        print()
        iteracion += 1
        sig *= m
        return algoritmo_recursivo(sig, k, g, c, r, iteracion)
'''
x0 = 87
a = 1
c = 3
m = 59
g = 0
k = 0
n = 59
'''
try:
    r = []
    print("escribir: ")
    xi = int(input("x0: "))
    a = int(input("a: "))
    c = int(input("c: "))
    m = int(input("m: "))
    g = int(input("g: "))
    k = int(input("k: "))
    n = int(input("n: "))

    algoritmo_recursivo(xi, k, g, c, r, 0)
except ValueError as a:
    print("necesito valores en decimal unicode (0-9)")
    print(a)





