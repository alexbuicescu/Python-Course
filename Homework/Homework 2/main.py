__author__ = 'Alexandru'

def count_lines():
    with open('count_lines_input.txt', 'r') as inf:
        return len(inf.readlines())


import  random
def write_random_lines_and_numbers():
    with open('nr2.txt', 'w') as outf:
        #message for my future self:
        #I got all even numbers between 100 and 1000 with: range(100, 1000, 2)
        #after that I selected a random k numbers from them, k == random.randrange(1, 10, 2) (k - uneven)
        #after that I converted the list of ints to list of strings with: map(str, listOfInts)
        #after that I made the numbers to be written on separate lines with: '\n'.join(listOfStrings)
        outf.write('\n'.join(map(str, (random.sample(range(100, 1000, 2), random.randrange(1, 10, 2))))))

    return


import datetime as date
def my_age_in_days():
    with open('my_birthday.txt', 'r') as inf:
        myBirthDay = inf.read().split()
        year, day, month = int(myBirthDay[0]), int(myBirthDay[1]), int(myBirthDay[2])
        return str((date.date.today() - date.date(year, day, month)).days)


# Exemple de output:
#
#     `'5 romb'`
#     `'K trefla'`
#     `'A rosie'`
#     `'J negru'`

def get_card():
    totalCards = range(2, 11) + ['A', 'J', 'Q', 'K']
    totalColors = ['romb', 'trefla', 'rosie', 'negru']
    return str(totalCards[random.randint(0, len(totalCards) - 1)]) + ' ' + str(totalColors[random.randint(0, len(totalColors) - 1)])


#
#     `['10 romb', '4 romb', 'J negru', '7 rosie', '3 trefla']`

def get_hand_of_cards():
    totalCards = range(2, 11) + ['A', 'J', 'Q', 'K']
    totalColors = ['romb', 'trefla', 'rosie', 'negru']
    myHand = []

    while len(myHand) < 5:
        card = random.randint(0, len(totalCards) - 1)
        color = random.randint(0, len(totalColors) - 1)
        newCard = str(totalCards[card]) + ' ' + totalColors[color]
        if newCard not in myHand:
            myHand.append(newCard)
    return myHand



def loto():
    return random.sample(range(1, 50), 6)


from operator import pow
def sum_of_odd_squares():
    n = 6
    return sum(map(pow, range(1, n + 1, 2), [2] * (n / 2)))


#
#   any_valid_number('numarul meu este 0740123456, sa stii') -> False
#   any_valid_number('noul meu numar este 0218822555, este scris in clar') -> True
#   any_valid_number('noul meu numar este 0218822sss, dar este codificat') -> False
#   any_valid_number('Din numarul meu 021882255 lipseste o cifra') -> False

import re

def any_valid_number(text):
    return re.compile(r'021([0-9]{7})').search(text) != None


#
#     "luna zi, an - ora:minut"
#     Exemplu: "December 31, 1999 - 03:30 PM"
#
#
#     "ora:minut / ziua.luna"
#     Exemplu: "19:30 / 10.01"


def current_time(time_format):
    if time_format == 'USA' or time_format == 'US' or time_format == 'america':
        return str(date.date.today().month) + ' ' + str(date.date.today().day) + ', ' + str(date.date.today().year) + ' - ' + str(date.datetime.now().hour) + ':' + str(date.datetime.now().minute)
    else:
        return str(date.datetime.now().hour) + ':' + str(date.datetime.now().minute) + ' / ' + str(date.date.today().day) + '.' + str(date.date.today().month)




def guess_the_number():
    myNumber = random.randint(1, 20)
    tryouts = 0
    while tryouts < 5:
        theUserNumber = 15#raw_input('Incercarea ' + str(tryouts + 1) + ': ')
        if int(theUserNumber) > myNumber:
            print 'Numarul la care m-am gandit este mai mic'
        elif int(theUserNumber) < myNumber:
            print 'Numarul la care m-am gandit este mai mare'
        else:
            print 'Bravo, ai ghicit numarul din ' + str(tryouts + 1) + ' incercari!'
        tryouts += 1




#
#     valid_email('ion_popescu@yahoo.com') -> True
#     valid_email('ion_popescu@yahoo.ro') -> False
#     valid_email('ion_popescu_yahoo.com') -> False
#     valid_email('pion_popescu@yahoo.com') -> False

def valid_email(email):
    if 'ion_' not in email or '@' not in email:
        return False
    if email.index('ion_') > 0 or email.index('@') < 4 or email[-4:] != '.com':
        return False
    return True


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '{0} got: {1}, expected: {2}'.format(prefix, got, expected)


def main():
    print '1. Numarul de linii dintr-un fisier'
    print count_lines(), '\n'
    print '2. Linii random, numere random\n'
    write_random_lines_and_numbers()
    print '3. Varsta in zile'
    print my_age_in_days(), '\n'
    print '4. Carte de joc'
    print get_card(), '\n'

    print '5. O mana de carti de joc'
    unique_ok = True
    for _ in range(1000):
        hand = get_hand_of_cards()
        if len(hand) > len(set(hand)) or not hand:
            unique_ok = False
    print 'OK\n' if unique_ok else ' X: s-a generat de 2 ori aceeasi carte\n'

    print '6. Extragere 6/49'
    unique_ok = True
    for _ in range(1000):
        numbers = loto()
        if len(numbers) != len(set(numbers)) or not numbers or \
                [n for n in numbers if n not in range(1, 50)]:
            unique_ok = False
    print 'OK\n' if unique_ok \
        else ' X: Numerele se repeta sau nu sunt intre 1 si 49\n'

    print '7. Suma de patrate de numere impare'
    print sum_of_odd_squares(), '\n'

    print '8. Numar de telefon valid din Bucuresti'
    test(any_valid_number('numarul meu este 0740123456, sa stii'), False)
    test(any_valid_number('noul meu numar este 0218822555, este scris in clar'),
         True)
    test(any_valid_number('noul meu numar este 0218822sss, dar este codificat'),
         False)
    test(any_valid_number('Din numarul meu 021882255 lipseste o cifra'), False)
    print

    print '9. Timpul curent in format american'
    print current_time('USA')
    print 'Fara teste \n'

    print '10. Ghiceste numarul'
    guess_the_number()
    #print 'Fara teste \n'

    print '11. Adresa de mail vailda'
    test(valid_email('ion_popescu@yahoo.com'), True)
    test(valid_email('ion_popescu@yahoo.ro'), False)
    test(valid_email('ion_popescu_yahoo.com'), False)
    test(valid_email('pion_popescu@yahoo.com'), False)

# main()
if __name__ == '__main__':
    main()