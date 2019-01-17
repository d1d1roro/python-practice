# 10. 함수 객체의 속성
# def f(a, b, c=1):
#     'func attribute testing'
#     localx = 1
#     localy = 2
#     return 1
# print(f.__doc__, f.__name__, f.__defaults__) # func_doc: __doc__

# def f(a, b, c, *args, **kw):
#     localx = 1
#     localy = 2
#     return 1
# code = f.__code__
# print(code.co_name, code.co_argcount, code.co_nlocals, code.co_varnames)

# 재귀적 프로그래밍
# def sum(N):
#     if N == 1: return 1
#     return N + sum(N-1)
# print(sum(10))