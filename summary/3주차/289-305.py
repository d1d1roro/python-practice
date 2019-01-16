# import math
# x1 = (-b + math.sqrt(b*b - 4*a*c)) / (2.0*a)
# x2 = (-b - math.sqrt(b*b - 4*a*c)) / (2.0*a)

# D = b*b - 4*a*c
# a2 = 2 * a
# sd = math.sqrt(D)
# x1 = (-b + sd) / a2
# x2 = (-b - sd) / a2

# 1-1. 간단한 함수의 정의
def add(a, b):
    return a+b

# abs(-4)

# def myabs(x):
#     if x < 0:
#         x = -x
#     return x

# # print(add(1, 2))
# # print(myabs(-5))

# def addabs(a, b):
#     c = add(a, b)
#     return myabs(c)
# print(addabs(-5, -7))

# 2. 함수의 정의와 호출
# print(add)
# c = add(10, 30)
# print(c)
# print(40 + add(5, 10))
# f = add
# print(f(4, 5))
# print(add, f)
# def simple():
#     pass
# simple()

# def addmember(memberlist, newmember):
#     if newmember not in memberlist:
#         memberlist.append(newmember)

# members = ['kim', 'lee', 'park', 'youn']
# addmember(members, 'jo')
# addmember(members, 'kim')
# print(members)

# def addmember(memberlist, newmembers):
#     if type(newmembers) not in (type([]), type(())):
#         newmembers = [newmembers]
#     for m in newmembers:
#         if m not in memberlist:
#             memberlist.append(m)

# members = ['kim', 'lee', 'park', 'youn']
# addmember(members, 'jung')
# addmember(members, ['son', 'jo', 'jae'])
# print(members)

# 03. 인수 전달 방법
# def f(t):
#     t = 10

# a = 20
# f(a)
# print(a) # 20

# def h(t):
#     t = (1, 2, 3)
# a = (5, 6, 7)
# h(a)
# print(a) # 5, 6, 7

# def g(t):
#     t[1] = 10

# a = [1, 2, 3]
# g(a)
# print(a) # 1, 10, 3

# def gg(t):
#     t = [1, 2, 3]
# a = [5, 6, 7]
# gg(a)
# print(a) # 5, 6, 7

# 4. return 문에 대하여
# 4-1. 인수 없이 리턴하기
# def nothing():
#     return
# print(nothing()) # None: 파이썬 내장 객체, 아무 값도 없음을 나타내기 위한 객체

# def f():
#     return
# f()
# a = f() # 값이 전달되지 않았다면 변수 a가 생성될 수 없었을 것. 그렇군!
# print(a)

# 4-2. return 문 없이 리턴하기
# def print_menu():
#     print('1. Snack')
#     print('2. Snake')
#     print('3. Snick')
# print(print_menu())

# 결과
# 1. Snack
# 2. Snake
# 3. Snick
# None: 파이썬은 리턴 값이 존재하지 않을 때 언제나 None 객체를 넘긴다.

# 4-3. 한 개의 값을 리턴할 때
# def abs(x):
#     if x < 0:
#         return -x
#     return x
# print(abs(-10))

# 4-4. 두 개 이상의 값을 리턴할 때
# 보통 튜플 혹은 리스트를 사용
# def swap(x, y):
#     return y, x
# a, b = swap(b, a)
# x = swap(a, b) # 하나의 이름으로 값을 받아서 처리할 수도 있다.
# print(x[0], x[1])

# a, b = divmod(9, 5)
# print(a, b)

# def length_list(l):
#     res = []
#     for el in l:
#         res.append(len(el))
#     return res
# l = ['python', 'pyson', 'pythong', 'pydon']
# # print(length_list(l))
# print([len(s) for s in l]) # 리스트 내장을 이용

# 05. 동적인 자료형 결정
# def add(a, b):
#     return a+b # __add__
# c = add(1, 3.4)
# d = add('dynamic', 'typing')
# e = add(['list'], ['and', 'list'])
# print(c, d, e)

# class MyClass:
#     def __add__(self, b):
#         print('add %s is called' % b)
# c = MyClass()
# print(c + 1)
# print(c + 'abc')
# print(c + 'anaconda')

# 06. 스코핑 룰
# 지역, 전역, 내장 영역 존재
# 지역: 함수, 전역: 모듈(파일), 내장 영역: 파이썬 언어 자체에서 정의한 내용
# 규칙: LGB 규칙(Local, Global, Built-in 순서)

# 6-1. 지역 변수와 전역 변수
# g = 10
# h = 5

# def f(a):
#     global h # 전역 변수를 변경하고 싶다면
#     h = a + 10
#     b = a + g
#     return b

# g = 10
# def f():
#     a = g # local variable 'g' referenced before assignment
#     g = 20
#     return a
# f()

# 6-2. 내장 영역의 이름 알아보기
# print(dir(__builtins__))

# 6-3. 중첩 영역 지원
# x = 2
# def F():
#     x = 1
#     def G():
#         print(x)
#     G()
# print(F())

# def F():
#     x = 1
#     print(list(filter(lambda a: a > x, range(-5, 5))))
# print(F())

# def f(x):
#     def g(i):
#         print(i)
#         if i: g(i-1)
#     g(x)
# print(f(3))

# 주의
# def bank_account1(initial_balance):
#     balance = initial_balance
#     def deposit(amount):
#         nonlocal balance
#         balance = balance + amount
#         return balance
#     def withdraw(amount):
#         nonlocal balance
#         balance = balance - amount
#         return balance
#     return deposit, withdraw
# d, w = bank_account1(100)
# print(d(100)) # local variable 'balance' referenced before assignment
# print(w(10))

# -------------------------------------------------------------------------------------------------------
# 나는 이걸 함수의 생명으로 봤는데, 책에선 좌변/우변 참조하는 변수가 다르다고 하네.
# 215 라인 시점에서 bank_account1 함수는 이미 종료됨.
# 215 라인 시점에서 d = deposit 함수이고, 그 함수 내부에서는 balance 라는 변수가 선언된 적이 없으므로 에러 발생.
# 이게 그 말인가. 말을 뭐 이리 어렵게 했노.
# -------------------------------------------------------------------------------------------------------

# def bank_account2(initial_balance):
#     balance = [initial_balance]
#     def deposit(amount):
#         balance[0] = balance[0] + amount
#         return balance[0]
#     def withdraw(amount):
#         balance[0] = balance[0] - amount
#         return balance[0]
#     return deposit, withdraw
# d, w = bank_account2(100)
# print(d(100))

# -------------------------------------------------------------------------------------------------------
# 클로저를 지원하는 것인가, 안 하는 것인가.
# 좀 헷갈리네. 클로저를 지원한다면 함수가 종료되더라도 balance가 살아있어야하는 거 아닌가.
# 그런데 위에 변수는 안 되고, 객체는 되고. 뭐꼬?
# 함수가 종료되더라도 클로저와 상관없이 공유되고 있는 객체는 살아있나.
# 그럼 233 라인 시점에서 deposit, withdraw 함수가 balance 객체를 참조하고 있으므로 제거되지 않았다?
# 오메, 실행 컨텍스트가 우째 되노 그러면-__-?
# -------------------------------------------------------------------------------------------------------