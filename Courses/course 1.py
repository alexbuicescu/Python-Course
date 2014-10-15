# for i in range(100):
# 	print str(i + 1) + ' Hello World'

# s = 'Aoleuuuu '
# for i in range(100):
# 	s += ' Hello'
# print s + ' de capu meu'

# for i in range(1, 101):
# 	if i % 3 == 0 and i % 5 == 0:
# 		print "'fizz buzz'"
# 	elif i % 3 == 0:
# 		print "'fizz'"
# 	elif i % 5 == 0:
# 		print "'buzz'"
# 	else:
# 		print i

# tastatura = 70
# mouse = 50
# casti = 100
# tva = 24.0 / 100
# print str((tastatura + mouse + casti) * tva + (tastatura + mouse + casti))

# def factorial(n):
# 	rezultat = 1
# 	for i in range(1, n + 1):
# 		rezultat *= i
# 	print rezultat
# factorial(4)

# def numereDinInterval():
# 	rezultat = ''
# 	for i in range(2000, 3001):
# 		if i % 5 == 0 and i % 7 != 0:
# 			rezultat += str(i) + ', '
# 	if len(rezultat) > 0:
# 		print rezultat[:-2]
#numereDinInterval()

# def numereDinInterval():
# 	rezultat = []
# 	for i in range(2000, 3001):
# 		if i % 5 == 0 and i % 7 != 0:
# 			rezultat.append(str(i)) #+= str(i) + ','
# 	print ', '.join(rezultat)
#numereDinInterval()

# def palindrom(stringulMeu):
# 	verificare = ''
# 	for i in range(len(stringulMeu) - 1, -1, -1):
# 		verificare += stringulMeu[i]
# 	if verificare == stringulMeu:
# 		print stringulMeu + ' este palindrom'
# 	else:
# 		print stringulMeu + ' nu este palindrom '
# palindrom('acca')

# def elementInComun(lista1, lista2):
# 	ok = False
# 	for i in lista1:
# 		for j in lista2:
# 			if i == j:
# 				ok = True
# 	print ok
# elementInComun([1,2,3], [4,5,3])

# def findLongestWord(listaDeCuvinte):
# 	lungimeMaxima = 0
# 	for cuvant in listaDeCuvinte:
# 		if len(cuvant) > lungimeMaxima:
# 			lungimeMaxima = len(cuvant)
# 	print lungimeMaxima
# findLongestWord(['ana', 'are', 'mere'])

# def filterLongestWord(listaDeCuvinte, n):
# 	listaNoua = []
# 	for cuvant in listaDeCuvinte:
# 		if len(cuvant) > n:
# 			listaNoua.append(cuvant);
# 	return listaNoua
# print filterLongestWord(['ana', 'are', 'mere'], 3)

# def sumaDeNumere(*numere):
# 	rezultat = 0
# 	for numar in numere:
# 		rezultat += numar
# 	print rezultat
# sumaDeNumere(1, 2, 2)