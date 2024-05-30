# ООП - объектно ориентированое программирование
class Siu:
    type = 'Iphone'
    memory = 256
    model = 11

# __init__ - метод
# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
# gentra = Car('Ravon', 'Black', 2022)
#
# print(gentra.model)

# class User:
#     def __init__(self, username, text, likes=0):
#         self.username = username
#         self.text = text
#         self.likes = likes
#     def add_comment(self):
#         print('комментарий опубликован')
# userneme = User('Rama', 'Лаваш отстой', 12)
# userneme.add_comment()
# print(vars(userneme))
# # print(userneme.__dict__)

# class Car:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#     def stop(self):
#         print('тачка остановилась')
#     def change_color(self, new_color):
#         self.color = new_color
#
# gentra = Car('Ravon', 'Black', 2022)
# gentra.change_color('White')
# print(gentra.color)

#TZ
# class BankAccount:
#     def __init__(self, name, balance, deposit, cash, my_balance):
#         self.name = name
#         self.balance = balance
#         self.deposit = deposit
#         self.cash = cash
#         self.my_balance = my_balance
# account = BankAccount('Ramazan', 1200, 1000, 12000, 100000)
# print(vars(account))

# class BankAccount:
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         self.balance += amount
#         print('деньги успешно добавлены на счет')
#     def cash(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print('Деньги сняты')
#         else:
#             print('недостаточно средств')
#     def my_balance(self):
#         print(f'Денег на балансе: {self.balance} сум')
#
# user1 = BankAccount('Botir')
# while True:
#     menu = input("чо хочешь сделать?: \n"
#                  "1-Посмотреть баланс\n"
#                  "2-Пополнить счет\n"
#                  "3-Снять деньги\n"
#                  "Действие: ")
#     if menu == '1':
#         user1.my_balance()
#     elif menu == '2':
#         amount = float(input('Введи сумму: '))
#         user1.deposit(amount)
#     elif menu == "3":
#         amount = float(input('Введите сумму для снятия: '))
#         user1.cash(amount)
#     else:
#         print('непонял')
# TZ
class User:
    def __init__(self, name, email, age, phone_number):
        self.name = name
        self.email = email
        self.age = age
        self.phone_number = phone_number
    def change_name(self, new_name):
        self.name = new_name
    def change_number(self, new_number):
        self.phone_number = new_number
    def change_email(self, new_email):
        self.email = new_email

user1 = User(name='Рамазан', email='aboba@gmail.com', age=20, phone_number='+998909393939',)
print(vars(user1))




