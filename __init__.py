# def set_func(func):
#     __singleton = None
#
#     def call_func(*args, **kwargs):
#         nonlocal __singleton
#         if not __singleton:
#             __singleton = func(*args, **kwargs)
#             return __singleton
#         else:
#             return __singleton
#
#     return call_func
#
#
# @set_func
# class Std(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# s2 = Std('jack', 18)
# print(id(s2), s2.name, s2.age)
#
# s1 = Std('leo', 23)
# print(id(s1), s1.name, s1.age)

# A=[1, 3, 5 ,7]
# B=[1, 4, 5, 7, 9]
# # list1 = A.extend(B)
# print(list(set(A+B)))

# def sum_a_b(a,b):
#     sum = 0
#     if b > a:
#         for X in range(a, b + 1):
#             sum = sum + X
#         print(f"{a}+{b}之和的值：", sum)
#
#     else:
#         print("请输入b要大于a的值")
#
# sum_a_b(1,3)
