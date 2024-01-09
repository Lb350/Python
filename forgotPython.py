from random import randint

# a = 768
#
# print(id(a))

# Unit 8


# def sample(name):
#         print(f'Hello {name}! Hope you are fine {name}. Good morning {name}')
#
#
# sample(input())


# Программа, которая генерирует 10 случайный чисед и находит наибольшее из них

# nums = []
# count = 10
#
# while count != 0:
#     nums.append(randint(1, 99999))
#     count -= 1
#
# print(f'{nums}\n{max(nums)} is highest number')


# n = 10
# nums = [randint(1,9999) for n in range(n)]
#
#
# print(f'{nums}\nReverse sorted: {sorted(nums, reverse=True)}\nSum:{sum(nums)}')


# count = 10
# text_list = []
#
# while count != 0:
#     enter_text = input()
#     text_list.append(enter_text)
#     count -= 1
#
# def reverse_text(text_list):
#     for i in text_list:
#         for l in reversed(i):
#             print(l, end='')
#         print(' ')
# reverse_text(text_list)

# Factorial



# def factorial(n):
#     fact = n
#     for i in range(1, n):
#         fact = fact * i
#
#     return fact
#
# print(factorial(100))



# Unit 9


# class Car():
#
#     def __init__(self, name, engine, fuel, transmission):
#         self.name = name
#         self.engine = engine
#         self.fuel = fuel
#         self.transmission = transmission
#
#     def short_view(self):
#         print(f'It`s {self.name}\nEngine - {self.engine}\n'
#               f'Fuel - {self.fuel}\nTransmission - {self.transmission}')
#
# class Honda(Car):
#
#     def __init__(self):
#         self.name = 'Honda'
#         self.engine = '1.8l'
#         self.fuel = 'gasoline'
#         self.transmission = 'MT'
#
#
# print(Honda().short_view())
#


# Unit 11


def devide(number):
    try:
        x = 64 / number
        print(x)
    except ZeroDivisionError:
        print('Cannot divide by 0')


devide(5)
devide(1)
devide(0)
devide(2)

















