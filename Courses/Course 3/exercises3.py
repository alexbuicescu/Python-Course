__author__ = 'Alexandru'

class BankAccount(object):
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def isSumValid(self, sum):
        if sum < 0:
            print 'The sum must be positive'
            return False
        return True

    def extract(self, sum):
        if self.isSumValid(sum) == False:
            return
        if self.money - sum >= 0:
            self.money -= sum
        else:
            print 'Fonduri insuficiente!'

    def deposit(self, sum):
        if self.isSumValid(sum) == False:
            return
        self.money += sum


class Person(object):
    def __init__(self, name, account, salary=0):
        self.name = name
        self.account = account
        self.__salary = salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return 'Confidential!'

    salary = property(get_salary, set_salary)

    def receive_salary(self):
        self.account.deposit(self.__salary)

    def make_shopping(self, sum):
        self.account.extract(sum)


class SpecialBankAccount(BankAccount):
    def __init__(self, name, money, overdraft):
        self.overdraft = overdraft
        super(SpecialBankAccount, self).__init__(name, money)

    def extract(self, sum):
        if self.isSumValid(sum) == False:
            return
        if self.money - sum >= -self.overdraft:
            self.money -= sum
        else:
            print 'Creditul maxim a fost atins'


# person1 = Person('gigel', BankAccount('gigel', 100), 100)
# print person1.salary
account = SpecialBankAccount('giorgica', 10, 10)
person2 = Person('giorgica', account, 20)
person2.receive_salary()
print 'The money from account after first salary', account.money
person2.salary = -30
person2.receive_salary()
print 'Just received a negative salary, and the money from account are:', account.money
person2.make_shopping(10)
print 'The money from account after first shopping', account.money
person2.make_shopping(30)
print 'The money from account after second shopping', account.money
person2.make_shopping(1)
print 'The money from account after third shopping', account.money


import random
class Zar(object):
    def roll(self):
        return random.randint(1, 6);


class ZarNecinstit(object):
    def roll(self):
        return 3

dices = [Zar(), Zar(), ZarNecinstit(), Zar(), ZarNecinstit()]
print [x.roll() for x in dices]


class Pet(object):
    def get_my_pet_name(self):
        print 'You just asked for my pet name, and it is:', 'Courrage'


class Dog(Pet):
    def get_my_pet_name(self):
        super(Dog, self).get_my_pet_name()
        print 'You just asked for my dog name, and it is:', 'The cowardly dog'

pet = Pet()
pet.get_my_pet_name()
dog = Dog()
dog.get_my_pet_name()
