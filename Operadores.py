from functools import reduce

lista = [1, 3, -1, 15, 9]


listaDobles = map(lambda x: x*2, lista)
a = list(listaDobles)

listaPares = filter(lambda x: x % 2 == 0, lista)
b = list(listaPares)

sumatorio = reduce(lambda x, y: x+y, lista)

print(a)
print(b)
print(sumatorio)