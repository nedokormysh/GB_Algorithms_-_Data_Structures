from collections import namedtuple

hero_1 = ('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_1[4])

class Person:

    def __init__(self, name, race, healtg, mana, strength):
        self.name = name
        self.race = race
        self.healtg = healtg
        self.mana = mana
        self.strength = strength

# при инициализации объекта класса будем запрашивать 5 параметров. И свойства объекта будут этими 5 параметрами

hero_2 = Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_2.mana)
# слева название нового класса. Первый параметр - название нашего класса. Названия должны быть одинаковы слева и справа.
# второй аргумент - строка с именами характеристик через запятую, но можно просто пробелы оставить
# если характеристики хранятся в списке, то проблем тоже не будет. См. ниже prop
New_Person = namedtuple('New_person', 'name, race, healtg, mana, strength')
hero_3 = Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_3.race)

prop = ['name', 'race', 'healtg', 'mana', 'strength']

New_Person1 = namedtuple('New_person1', prop)
hero_4 = Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_4.name)

# проверка на правильность имени

prop = ['name', '3race', 'healtg', '_mana', 'strength']

New_Person1 = namedtuple('New_person1', prop, rename=True)
hero_5 = Person('Aaz', 'Izverg', 100, 8.0, 250)
print(hero_5)

# точка с координатами трехмерного измерения

print('*' * 100)

Point = namedtuple('Point', 'x, y, z')

p1 = Point(2, z=3, y=4)
print(p1)

t = [5, 10, 15]

p2 = Point._make(t)
print(p2)

d2 = p2._asdict()
print(d2)

# p2.x = 6

p3 = p2._replace(x=6)
print(p3)

print(p3._fields)

print('*' * 100)

New_Point = namedtuple('New_point', 'x y z', defaults=[0, 0])
p4 = New_Point(5)
print(p4)

# print(p4._fields_defaults)


dct = {'x': 10, 'y': 20, 'z': 30}
p5 = New_Point(**dct)
print(p5)
