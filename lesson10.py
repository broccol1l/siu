# class Noname:
#     def punkt(self, word):
#         return f'слово: {word}'
# c = Noname()
# print(c.punkt('123'))

# class Noname:
#     def __init__(self, name):
#         self.name = name
#     def punkt(self, word):
#         return f'слово: {word}, {self.name}'
#
#
# c = Noname("Oleg")
# b = Noname('Ivan')
# print(c.punkt('privet'))

# Принципы ООП:
# Наследование
# class Father:
#     def work(self, worker):
#         self.a = worker
#
# class sluga(Father):
#     def sluga(self, slave):
#         self.b = slave

# class Parent:
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#     def hello(self):
#         print('Hello')
# class Son(Parent):
#     pass
#
# mom = Parent('Ann', "female")
# son1 = Son('Paul', 'male')
# mom.hello()
# mom.hello()

#super() - включает атрибуты родительского класса

# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
# class SuperCar(Car):
#     def __init__(self, model, color, year, sponsor):
#         super().__init__(self, model, color, year)
#         self.sponsor = sponsor

# Множественное наследование
# @classmethod
# class MyClass:
#     @classmethod
#     def class_info(cls):
#         print(f'Название этого класса {cls.__name__}')
#
# MyClass.class_info()

# @property()
class Worker:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def work(self):
        print(f'{}')