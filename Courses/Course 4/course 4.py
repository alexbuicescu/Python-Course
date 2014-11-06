__author__ = 'Alexandru'

def get_dices():
    return [(x, y) for x in range(1, 7) for y in range(1, 7)]

def remove_duplicates(list_with_duplicates):
    return {x for x in list_with_duplicates}

def gen_dict(buildings):
    return {y: x for x, y in buildings}

def gen_names(companies):
    return [companies.get(i) for i in range(1, 11)]

import this
def get_zen():
    return "".join([c in this.d and this.d[c] or c for c in this.s])

def zen_of_python():
    words = get_zen().split()
    return [index for index, word in enumerate(words) if word == 'better']

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __cmp__(self, other):
        if hasattr(other, 'age'):
            return self.age.__cmp__(other.age)

def person_factory(list_of_properties):
    return [Person(name, age) for name, age in list_of_properties]

def get_person_ages(list_of_persons):
    # list_of_persons = sorted(list_of_persons)
    list_of_persons.sort(key=lambda x: x.name)
    persons = [x.age for x in list_of_persons if x.name.endswith('escu')]
    return persons

def main():
    print get_dices()
    print
    print remove_duplicates([1, 2, 3, 1, 2, 4])
    print
    print gen_dict({("ana", 1), ("are", 2), ("mere", 4)})
    print
    print gen_names(gen_dict({("ana", 2), ("are", 3), ("mere", 5)}))
    print
    print zen_of_python()
    print
    print get_person_ages(person_factory([('gigicaescu', 10), ('aaryescu', 2)]))

if __name__ == '__main__':
    main()
