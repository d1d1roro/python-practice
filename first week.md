### 9-4. while문
- 조건식을 만족할 동안 반복
- continue: 조건식으로 이동
- break: 반복문 강제 종료
- else: 반복문을 모두 수행 후 종료되는 경우 실행.
else를 이용하면 정상적인 종료인지 어떤 조건식에 의한 강제 종료인지 구분할 수 있다.

- 1부터 10까지의 숫자를 증가시키는 while 문
~~~
count = 1
while count < 11:
    print(count)
    count = count + 1
~~~
#### count = count + 1 >> count += 1 변경 가능

- 1부터 10까지의 합을 구하는 while 문
~~~
sum = 0
a = 0
while a < 10:
    a = a + 1
    sum = sum + a
print(sum)
~~~
#### a = a + 1 >> a += 1
#### sum = sum + a >> sum += a

- while문 + if문
~~~
a = 0
while a < 10:
    a = a + 1
    if a < 3: continue
    if a > 10: break
else:
    print('else block')
print ('done')
~~~

### 9-5. 함수
- 하나의 이름으로 코드를 묶은 단위를 말한다.
- 보통 반복적인 코드를 함수로 작성한다.
- 함수를 잘 작성하면 유지보수 및 추후 확장하는 데에 도움이 된다.

#### 작성방법
~~~
def 함수명(가인수들):
    문들
~~~

- 가인수들: 파라미터를 받는 이름을 의미
- 함수를 호출할 때 넘겨주는 인수: 실인수
- 즉, 실인수를 넘겨주면 함수에서는 가인수로 받는다.
- 함수의 결과값은 return 으로 반환한다.
- 동적인 인수 전달을 하므로 함수 선언 시에 인수의 형을 지정할 필요가 없다.
- 따라서, 어떠한 형의 인수도 받을 수 있으며, 그 형에 맞는 + 연산을 수행해준다. >> 동적인 형 결정 (python 특징)

~~~
def add(a, b):
    return a + b

print(add(3, 4))
~~~

- 함수명: add
- 가인수: a, b
- 반환값(return): a + b
- 실인수: 3, 4

~~~
def minus(x, y):
    return x - y

print (minus(x=10, y=5))
print (minus(y=10, x=5))
~~~

- 위와 같이 실인수를 넘겨줄 때, 가인수의 변수명을 일치시켜 값을 선언할 수 있다.

~~~
def incr(x, d=1):
    return x + d

print(incr(5))
print(incr(5, 10))
~~~

- 또한, 위와 같이 함수 선언 시 기본값을 설정할 수 있다.
- 위 함수의 경우, 두 개의 인자를 받는데, 두번째 인자가 넘어오지 않을 경우, 기본값으로 계산한다.

## 3. 수치 자료형
### 1-1. 정수형 상수
- 10진, 8진, 16진 상수
- 컴퓨터 내부에서는 2진수로 수치를 표현하므로 2진수와 관련된 8진수나 16진수가 많이 사용된다.
- 표현 범위: -2,147,483,648 ~ 2,147,483,647

~~~
a = 23    # 10진수
b = 0o23  # 8진수 (0o / 0O)
c = 0x23  # 16진수 (0x)

print(a, b, c)
~~~
- print 함수의 기본 숫자 입력은 10진수이다.


- [최대 정수값 확인하기]
~~~
import sys
print(sys.maxsize) # 2,147,483,647
~~~

### 1-2. 실수형 상수
- 소수점을 포함하거나 e나 E로 지수를 포함
- C언어의 double 형과 동일, 8바이트(64비트)로 표현됨
- 52비트: 소수부 / 11비트: 지수부 / 1비트: 부호
- 표현 범위: 유효 자리 17, 지수는 10의 -308 ~ 308 범위

~~~
a = 1.2
b = 3.5e3
c = -0.2e-4
print(a, b, c) # 1.2 3500.0 -2e-05

e, f, g = 3.14, 2.16e-9, 3E220
print (e, f, g) # 3.14 2.16e-09 3e+220
~~~

### 1-3. 롱형 상수
- 정수형으로 표현할 수 없는 큰 수
- 정수 수치 마지막에 l, L 을 붙여서 표현한다.
- 되도록 'L' 을 붙여라.
- 유효 자리: 메모리가 허용하는 한 무한대
- BUT, There is no 'long integer' in Python 3 anymore.

### 1-4. 복소수형 상수
- 실수부 + 허수부로 표현
- 허수부: 숫자 뒤에 'j', 'J' 붙임
- 실수부와 허수부는 실수형 상수로 표현

~~~
c = 4 + 5j
d = 7 - 2j
print(c * d)

c.real
c.imag
~~~

- 켤레 복소수 (이거슨 저도 잘....)

~~~
a = 3
b = 4
complex(a, b)
c.conjugate()
~~~

- [수치 자료형의 수치 표현 범위]
| 데이터 형 | 비트 수 | 표현 범위 | 수 표현 |
| -------- | ------- | -------- | ------- |
| int(정수) | 32비트 | -2,147,483,648 ~ 2,147,483,647 | 10(십진수), 0o34(8진수), 0x38(16진수) |
| float(실수) | 64비트 | 유효자리 15자리, 약 10의 -308승 ~ 308승 | 1.2, 3.5e3 |
| complex(복소수) | 실수부 및 허수부(각각 64비트로 표현) | float과 같음 | 3 + 5j |

### 1-5. Decimal 자료형
- 계산시간에 관계없이 정확한 결과 값을 얻기를 원할 경우, 사용
- Decimal, Context 클래스 제공
- Decimal: 수자를 표현
- Context: 정확도나 반올림 방법 등과 같은 환경 설정

~~~
from decimal import *
a = Decimal(1234)
b = Decimal('1234')
c = Decimal(1.1)
print(type(a), type(b), type(c))
print(a, b, c)
~~~
- 3.3 버전부터 실수도 가능
- 하지만, 기대한 것처럼 1.1이 출력되진 않는다.
- round(c, 1) 과 같이 원하는 값을 출력할 수 있다.

~~~
e = 0.0
for k in range(100000):
    e += 0.0001
print(e)
print(repr(e))
~~~
- print(e), repr(e) 동일한 결과를 나타낸다.

~~~
e = Decimal('0.0')
delta = Decimal('0.00001')
for k in range(100000):
    e += delta
print(e)
~~~
- print(round(e, 1)) 와 같은 방법도 괜찮을 거 같다고 생각한다.

- Decimal 인스턴스끼리는 일반 수치와 같은 연산이 가능
~~~
a = Decimal('35.72')
b = Decimal('1.73')
print(a + b)
print(a - b)
print(a * b)
print(a / b)
~~~

- 하지만, 지수승을 할 때는 정수형이어야한다. (3버전은 가능)
~~~
print(a ** 2)
print(a ** b)
~~~

- 정수형과의 연산은 가능 / 실수형과의 연산은 불가능하다.
~~~
a = Decimal("1.2")
print(a + 2)
print(2 + a)
print(a + 1.5)
~~~
- unsupported operand type(s) for +: 'decimal.Decimal' and 'float'

- math, cmath 모듈 사용 및 메서드 사용 예시
~~~
import math, cmath
d = Decimal('123.456789012345')
print(math.sqrt(d), cmath.sqrt(-d), d.sqrt(), d.quantize(Decimal('.01'), rounding=ROUND_DOWN))
~~~

- 튜플을 이용하여 부호, 지수부, 가수부를 지정하는 객체 생성 예시
~~~
a = Decimal((1, (1, 4, 7, 5), -2))
print(a)
~~~
- 첫번째: 부호(0: 양수)
- 두번째: 가수부
- 세번째: 소수점의 위치

- Context 예시
~~~
print(getcontext())
print(Decimal(1) / Decimal(7))
getcontext().prec = 9
print(Decimal(1) / Decimal(7))
~~~
- 변경 후엔 객체를 다시 생성해야한다.
- 다음은 Decimal 모듈의 미리 설정된 세 가지 Context이다.
-- Extendedcontext, Basicconlext, Defaultcontext
-- 적용 예시
~~~
setcontext(ExtendedContext)
print(Decimal(1) / Decimal(7))
setcontext(DefaultContext)
print(Decimal(1) / Decimal(7))
~~~ 

## 파이썬 연산자
### 2-1. 산술 연산자
- + 덧셈
- - 뺄셈
- * 곱셈
- / 나눗셈
- // 몫 연산자
- ** 지수승
- % 나머지

~~~
print(2 ** 3) # 2의 3제곱
print (2 ** 3 ** 2) # 512
print((2 ** 3) ** 2) # 64
print(5 % 2) # 1
print(-5 % 2) # 1
print (5 ** -2.0) # 0.04
~~~

#### 1) 정수 연산 및 나누기 연산
- 우선 순위에 따른 결과값
-- 정수형 + 정수형 = 정수형
-- 정수형 + 실수형 = 실수형
-- 실수형 + 실수형 = 실수형

~~~
print(3 + 5) # 8
print(3 + 5.0) # 8.0
print(5 / 2.0) # 2.5
print(5 / 2) # 2.5, python 2.7 이하 버전의 경우 정수/정수 = 정수, 2.7 이후 버전은 실수로 출력
a = 5 // 3 # 몫: return value: 정수
a1 = 5 / 3 # 몫: return value: 실수
b = 5 % 3 # 나머지
print(a, a1, b) # 1 1.6666666666666667 2
~~~

- divmod: 몫과 나머지를 튜플 형태로 리턴하는 함수
~~~
print(divmod(5, 3)) # 몫: 1(//), 나머지: 2, 
~~~

- 나머지의 부호: 제수의 부호
~~~
print(5 % 3) # 2
print(5 % -3) # -1
print(-5 % 3) # 1
print(-5 % -3) # -2

print(5 // 3) # 1
print(5 // -3) # -2
print(-5 // 3) # -2
print(-5 // -3) # 1
~~~

- 비교 (/, //)
~~~
print(3 // 4) # 0
print(3.0 // 4.0) # 0.0
print(-3 // 4) # -1
print(-3 // 4.0) # -1.0

print(3 / 4) # 0.75
print(3.0 / 4.0) # 0.75
print(-3 / 4) # -0.75
print(-3 / 4.0) # -0.75
~~~

#### 2) 연산자의 우선 순위
연산자  | 설명 | 결합 순서
+, - | 단항 연산자 | 오른쪽 > 왼쪽 
** | 지수 | 오른쪽 > 왼쪽 
*, /, %, // | 곱하기, 나누기, 나머지, 몫 | 왼쪽 > 오른쪽 
+, - | 더하기, 빼기 | 왼쪽 > 오른쪽 

- 예시
~~~
print(4 * -5) # -20
~~~

#### 3) 연산자의 결합 순서
~~~
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
~~~

### QUIZ
#### 1. 다음 문들의 출력 결과를 예측하고 확인하라.
~~~
a, b, c, d, e = 2, -3, 5, -7, 11
print(a / b) # -0.6666666666666666
print(c / b) # -1.6666666666666667
print(7 + c * d / e) # 3.8181818181818183
print(2 * a % - b + c + 1) # 7
~~~

#### 2. 인치를 센티미터로 바꾸는 프로그램 코드를 작성하라. (1인치 = 2.54센티미터)
~~~
def changeToCm(a):
    return a * 2.54
print(changeToCm(2)) # 5.08
~~~

#### 3. 화씨를 섭씨로 바꾸는 프로그램 코드를 작성하라. (c = (f - 32) * 5.0 / 9.0)
~~~
def changeToCelsius(a):
    return (a - 32) * 5.0 / 9.0
print(changeToCelsius(86)) # 30.0   
~~~

### 2-2 관계 연산자
~~~
print(6 == 9) # False
print(6 != 9) # True
print(1 > 3) # False
print(4 <= 5) # True
a = 5
b = 10
print(a < b) # True
print(0 < a < b) # True
~~~