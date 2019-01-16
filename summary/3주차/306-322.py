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
b = 10

def db():
    print(b + 1)
    # b = 3 + 1

db()