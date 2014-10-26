#1
with open('input.txt', 'r') as inf:
	l = inf.readlines()
	print len(l)
	with open('output.txt', 'w') as outf:
		outf.write(str(len(l)))

#2
import random
with open('output.txt', 'w') as outf:
	outf.write('')
with open('output.txt', 'a') as outf:
	lineNumbers = random.randrange(1, 10, 2)
	for i in range(0, lineNumbers):
		nr = random.randrange(100, 1000, 2)
		outf.write(str(nr) + '\n')

#3
import datetime
with open('input.txt', 'r') as inf:
	data = inf.read().split()
	year, day, month = int(data[0]), int(data[1]), int(data[2])
	diff = datetime.date(year, day, month)
	print str(datetime.date.today() - diff)

#4
import random
def randomCard():
	totalCards = range(2, 15)
	totalCards[9:13] = ['A', 'J', 'Q', 'K']
	card = random.randint(0, 12)
	totalColor = ['romb', 'trefla', 'rosie', 'neagra']
	color = random.randint(0, 3)
	return totalCards[card], totalColor[color]
print randomCard()

#5
import random
def randomCard():
	totalCards = range(2, 15)
	totalCards[9:13] = ['A', 'J', 'Q', 'K']
	totalColor = ['romb', 'trefla', 'rosie', 'neagra']
	hand = []
	while(len(hand) < 5):
		card = random.randint(0, 12)
		color = random.randint(0, 3)
		newCard = str(totalCards[card]) + ' ' + totalColor[color]
		if newCard not in hand:
			hand.append(newCard)
	return hand
print randomCard()