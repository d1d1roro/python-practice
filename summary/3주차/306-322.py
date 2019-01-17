# def incr(a, step = 1):
#     return a + step
# b = 1
# b = incr(b)
# print(b) # 2
# b = incr(b, 10)
# print(b) # 12

# def area(height, width):
#     return height * width

# a = area(width = 20, height = 10)
# print(a)
# b = area(height = 'height string ', width = 3)
# print(b)

# print(area(width = 5, 20))

# def varg(a, *arg):
#     print(a, arg)

# print(varg(1), varg(2, 3), varg(2, 3, 4, 5, 6))

# def printf(format, *args):
#     print(format % args)

# printf("I've spent %d days and %d night to do this", 6, 5)

# def f(width, height, **kw):
#     print(width, height)
#     print(kw)

# f(width = 10, height = 5, depth = 10, dimension = 3)

# def h(a, b, c):
#     print(a, b, c)

# args = (1, 2, 3)
# h(*args)

# dargs = {'a': 1, 'b': 2, 'c': 3}
# h(**dargs) # 알아서 값을 가져가나?

# def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
#     print("kwarg_1:", kwarg_1)
#     print("kwarg_2:", kwarg_2)
#     print("kwarg_3:", kwarg_3)

# kwargs = {"kwarg_1": "Val", "kwarg_2": "Harper", "kwarg_3": "Remy"}
# some_kwargs(**kwargs)

# args = (1, 2)
# dargs = {'c': 3}
# h(*args, **dargs)

# f = lambda: 1
# print(f())

# g = lambda x, y: x + y
# print(g(1, 2))

# incr = lambda x, inc = 1: x + inc
# print(incr(10), incr(10, 5))

# b = 10

# def db():
#     print(b + 1)
#     # b = 3 + 1

# db()

# vargs = lambda x, *args: args
# print(vargs(1, 2, 3, 4, 5))

# kwords = lambda x, *args, **kw: kw
# print(kwords(1, 2, 3, a=4, b=6))

# def f1(x):
#     return x*x + 3*x - 10

# def f2(x):
#     return x*x*x

# def g(func):
#     return [func(x) for x in range(-10, 10)]

# print(g(f1))
# print('-'*30)
# print(g(f2))

# def g(func):
#     return [func(x) for x in range(-10, 10)]
# print(g(lambda x: x*x + 3*x - 10))
# print('-'*50)
# print(g(lambda x: x*x*x))

# func = [lambda x, y: x+y, lambda x, y: x-y, lambda x, y: x*y, lambda x, y: x/y]

# def menu():
#     print("0. add")
#     print("1. sub")
#     print("2. mul")
#     print("3. div")
#     print("4. quit")
#     return eval(input('Select menu: '))

# while 1:
#     sel = menu()
#     if sel < 0 or sel > len(func):
#         continue
#     if sel == len(func):
#         break
#     x = eval(input('First operand: '))
#     y = eval(input('Second operand: '))
#     print('Result = ', func[sel](x, y))

# def f(x):
#     return x*x
# X = [1, 2, 3, 4, 5]
# start = time.time()
# Y = map(f, X)

# def f(x):
#     return x*x
# X = [1, 2, 3, 4, 5]
# Y = []
# start = time.time()
# for x in X:
#     y = f(x)
#     Y.append(y)

# X = [1, 2, 3, 4, 5]
# Y = map(lambda a: a*a, X)
# print(list(Y))

# X = range(10)
# Y = map(lambda x: x*x + 4*x + 5, X)
# print(list(Y))

# X = [1, 2, 3, 4, 5]
# Y = [6, 7, 8, 9, 10]
# Z = map(lambda x, y: x+y, X, Y)
# print(list(Z))

# import operator
# X = [1, 2, 3, 4, 5]
# Y = [6, 7, 8, 9, 10]
# Z = map(operator.add, X, Y)
# print(list(Z))

# a = [1, 2, 3, 4]
# b = [10, 20, 30, 40]
# c = map(None, a, b)
# print(list(c)) # If you are using Python 3, then the map() method does not support None as a first argument:

# print(list(filter(lambda x: x>2, [1,2,3,4,5])))

# L = ['high', 'level', '', 'built-in', '', 'function']
# L = filter(None, L)
# print(list(L))

# range(100) 에서 5의 배수이거나 7의 배수인 수만을 걸러내어라.
# a = range(100)

# def check(num):
#     if not num % 5 or not num % 7:
#         return num
    
# b = filter(check, a)
# print(list(b))

# b = filter(lambda n: not n % 5 or not n % 7, a)
# print(list(b))

from functools import reduce

# 문제1. 전통적으로 최대값 구하기
li = [1, 2, 3, 4, 5]

# 문제1. reduce 활용하여 최대값 구하기
a = reduce(lambda a, b: a if a > b else b ,li)
print(a)