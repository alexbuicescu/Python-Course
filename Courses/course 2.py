lista = [1, 2, 4, 2, 5]
print lista[:2]
print lista[2:]
print lista[1:3:2]
print lista[-2:]
print lista.count(2)
print lista.index(2)
del lista[2]#daca stim indexul din lista
lista.remove(1)#daca stim valoarea din lista
lista.sort()#pentru sortare
print lista
print sum(lista)#aduna toate elementele din lista

#nume = raw_input("Care este numele tau?")
#print nume

with open('fisier.txt', 'r') as f:#poate fi folosit si asa: f = open('ads.txt', 'r'), doar ca este de preferat sa faci cu with
	for line in f:
		print line
	#trebuie sa ne intoarcem la inceputul fisierului
	f.seek(0)
	print f.read()

with open('fisier.txt', 'a') as f:
	f.write('\nlalala')

import random
#numere random intregi intre 4 si 100
print random.randint(4, 100)
print random.randrange(4, 100, 2)#randragne(a, b, step = 1)
#numere random reale intre 4 si 100
print random.random()
print random.shuffle(lista)