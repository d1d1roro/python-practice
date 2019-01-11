#file 106-128.py

# while01
count = 1
while count < 11:
    print(count)
    count = count + 1 # count += 1

# while02
sum = 0
a = 0
while a < 10:
    a = a + 1 # a += 1
    sum = sum + a # sum += a
print(sum)

# while03
a = 0
while a < 10:
    a = a + 1 # a += 1
    if a < 3: continue
    if a > 9: break
else:
    print('else block')
print ('done')

def add(a, b):
    return a + b

print(add(3, 4))

def minus(x, y):
    return x - y

print (minus(x=10, y=5))
print (minus(y=10, x=5))

def incr(x, d=1):
    return x + d

print(incr(5))
print(incr(5, 10))

a = 23
b = 0o23
c = 0x23

print(a, b, c)

import sys
print(sys.maxsize) # 2,147,483,647

a = 1.2
b = 3.5e3
c = -0.2e-4
print(a, b, c) # 1.2 3500.0 -2e-05

e, f, g = 3.14, 2.16e-9, 3E220
print (e, f, g) # 3.14 2.16e-09 3e+220

print(2 ** 3) # 2의 3제곱
print (2 ** 3 ** 2) # 512
print((2 ** 3) ** 2) # 64
print(5 % 2) # 1
print(-5 % 2) # 1
print (5 ** -2.0) # 0.04

print(3 + 5) # 8
print(3 + 5.0) # 8.0
print(5 / 2.0) # 2.5
print(5 / 2) # 2.5, python 2.7 이하 버전의 경우 정수/정수 > 정수, 2.7 이후 버전은 실수로 출력
a = 5 // 3 # 몫: return value: 우선순위
a1 = 5 / 3 # 몫: return value: 실수
b = 5 % 3 # 나머지
print(a, a1, b) # 1 1.6666666666666667 2

# divmod: 몫과 나머지를 튜플 형태로 리턴하는 함수
print(divmod(5, 3)) # 몫: 1(//), 나머지: 2, 

# 나머지의 부호: 제수의 부호
print(5 % 3) # 2
print(5 % -3) # -1
print(-5 % 3) # 1
print(-5 % -3) # -2

print(5 // 3) # 1
print(5 // -3) # -2
print(-5 // 3) # -2
print(-5 // -3) # 1

print(3 // 4) # 0
print(3.0 // 4.0) # 0.0
print(-3 // 4) # -1
print(-3 // 4.0) # -1.0

print(3 / 4) # 0.75
print(3.0 / 4.0) # 0.75
print(-3 / 4) # -0.75
print(-3 / 4.0) # -0.75

print(4 * -5) # -20

print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20

print(++3) # 3
print(--3) # 3
print(-+3) # -3
print(+-3) # -3

print(4 / 2 * 2) # 4.0
print(4 // 2 * 2) # 4

print(2 ** 3 ** 4) # 2417851639229258349412352
print((2 ** 3) ** 4) # 4096

# QUIZ
# 1. 다음 문들의 출력 결과를 예측하고 확인하라.
a, b, c, d, e = 2, -3, 5, -7, 11
print(a / b) # -0.6666666666666666
print(c / b) # -1.6666666666666667
print(7 + c * d / e) # 3.8181818181818183
print(2 * a % - b + c + 1) # 7

# 2. 인치를 센티미터로 바꾸는 프로그램 코드를 작성하라. (1인치 = 2.54센티미터)
def changeToCm(a):
    return a * 2.54
print(changeToCm(2)) # 5.08

# 3. 화씨를 섭씨로 바꾸는 프로그램 코드를 작성하라. (c = (f - 32) * 5.0 / 9.0)
def changeToCelsius(a):
    return (a - 32) * 5.0 / 9.0
print(changeToCelsius(86)) # 30.0   

# 관계 연산자
print(6 == 9) # False
print(6 != 9) # True
print(1 > 3) # False
print(4 <= 5) # True
a = 5
b = 10
print(a < b) # True
print(0 < a < b) # True

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a), id(b)) # 객체는 다름
s = t = [1, 2, 3]
print(id(s), id(t))

import keyword
print(keyword.kwlist)

from decimal import *
a = Decimal(1234)
b = Decimal('1234')
c = Decimal(1.1)
print(type(a), type(b), type(c))
print(a, b, c, round(c, 1))

e = 0.0
for k in range(100000):
    e += 0.00001
print(e)
print(repr(e))
print(round(e, 1))

e = Decimal('0.0')
delta = Decimal('0.00001')
for k in range(100000):
    e += delta
print(e)

a = Decimal('35.72')
b = Decimal('1.73')
print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(a ** 2)
print(a ** b)

a = Decimal("1.2")
print(a + 2)
print(2 + a)
# print(a + 1.5)

import math, cmath
d = Decimal('123.456789012345')
print(math.sqrt(d), cmath.sqrt(-d), d.sqrt(), d.quantize(Decimal('.01'), rounding=ROUND_DOWN))

a = Decimal((1, (1, 4, 7, 5), -2))
print(a)

print(getcontext())
print(Decimal(1) / Decimal(7))
getcontext().prec = 9
print(Decimal(1) / Decimal(7))

print("---")
setcontext(ExtendedContext)
print(Decimal(1) / Decimal(7))
setcontext(DefaultContext)
print(Decimal(1) / Decimal(7))

print(2 ** 3) # 2의 3제곱
print (2 ** 3 ** 2) # 512
print((2 ** 3) ** 2) # 64
print(5 % 2) # 1
print(-5 % 2) # 1
print (5 ** -2.0) # 0.04

a = 0
while a < 10:
    a = a + 1 # a += 1
    if a < 3: continue
    if a > 9: break
else:
    print('else block')
print ('done')