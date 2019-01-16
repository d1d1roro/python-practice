# PAGE 109
### 1. 주석문은 무엇인가?
- 설명 등 실행에 영향을 미치는 코드가 아닌 문장

### 2. 변수명 및 예약어
#### 가) 파이썬의 예약어의 종류와 예약어를 알아보는 방법을 쓰시오.
- and, global, or, false etc.
- import keyword \ print(keyword.kwlist)
#### 나) 변수명을 만드는 규칙을 쓰시오.
- 첫 문자: 영문, 언더스코어(_)
- 두 번째 문자부터는 제약이 없다.
- 크기의 제한이 없다.
- 대/소문자를 구분한다.
#### 다) 변수명을 만들 때, 조심해야할 점은 무엇인가?
- 예약어, 내장 함수명, 모듀명을 피해야한다.

### 3. 치환문
#### 가) 다양한 치환문의 종류를 정리하시오.
- a = 1: 하나 치환
- c, d = 3, 4: 여러 개를 한 번에 치환
- x = y = z = 0: 여러 개를 같은 값으로 치환
- 확장 치환문 (+=, -= 등)
- 객체 치환문 (x = [1, 2, 3])
#### 나) 치환문에서 a = a + 1의 의미는 무엇인가?
- 변수 a에 a + 1 을 대입하라.
#### 다) 1 + 3 = a 가 가능하지 않은 이유는 무엇인가?
- 좌변에는 치환될 변수명이 와야한다.
#### 라) a = b = 0 과 a = (b = 0)의 차이는 무엇인가?
- a = b = 0 은 a 와 b 라는 변수에 0을 대입 (정상)
- a = (b = 0) 은 b = 0이 문이기 때문에 허용되지 않는다.

### 4. import 의 의미를 간단히 정리하시오.
- 모듈 파일을 수행. 그 모듈 안에 있는 전역 변수들을 모듈 이름을 통하여 사용할 수 있다.

### 5. 콘솔 입/출력
#### 가) 키보드 입력 함수인 raw_input과 input의 차이는 무엇인가?
- raw_input: 입력한 값을 문자열로 초기화(python 3 버전에서는 input 으로 변경됨)
- input: 입력한 값의 자료형에 맞게 초기화(python 3 버전: eval(input()))
#### 나) 각 자료형을 입력받을 때의 예를 보이시오.
- string: i = input('자료형: ')
- etc: i = eval(input('자료형: ))
#### 다) 화면 출력 함수 print로 줄바꾸기를 하지 않고 출력하는 방법은?
- print 끝에 콤마(,)를 사용한다. (python 2)
- print('py', end=''), print('thon') (python 3)
#### 라) 복잡한 자료형을 출력할 때 쓰는 print의 실행 예를 보이시오.
~~~
import pprint
pprint.pprint(['python', 3, [1,2,3]])
~~~

### 6. 자료형의 종류
#### 가) 각 자료형의 특징을 정리해보시오.
- 수치형: 정수, 롱형 정수, 실수, 복소수 등
- 문자열: 문자들의 모임
- 리스트: 순서를 가지는 객체 집합
- 사전: 순서가 없고, key: value 형식의 객체 집합
- 튜플: 순서를 가지는 객체 집합, 내용 변경이 안 됨
- 파일: 파일에 자료를 입/출력하기 위한 객체
#### 나) 문자열, 리스트, 튜플의 다음 특징을 간단히 설명하고 실행 예를 보여라.
##### 1) 표현 방법
- 문자열: s = "python"
- 리스트: l = [1, 2, 3]
- 튜플: t = (1, 2,3)
##### 2) 인덱싱(Indexing)
- 문자열: s[0]
- 리스트: l[0]
- 튜플: t[0]
##### 3) 슬라이싱(Slicing)
- 문자열: s[1:3]
- 리스트: l[1:3]
- 튜플: t[1:3]
##### 4) 연결(Concatenation)
- 문자열: 'py' + 'thon'
- 리스트: l + l
- 튜플: t + t
##### 5) 반복(Repetition)
- 문자열: 'python' * 3
- 리스트: l * 3
- 튜플: t * 3
##### 6) 값의 변경
- 문자열: 불가
- 리스트: l[0] = 100, l.append(4)
- 튜플: 불가
#### 다) 사전은 다른 자료형과 어떻게 다른지 간단히 정리해 보시오.
- 순서가 없고, key: value 형태

### 7. 문자열 s = 'python' 에 대해서 다음 문제를 풀어보시오.
#### 가) s[0][0][0] 이 어떤 값이 나오는가 보고 이유를 설명해 보시오.
#### 나) s[-100], s[100], s[-100:100] 문들을 수행해 보고 수행되는 것과 수행되지 않는 것을 확인하라.
####     또, 수행되지 않는 경우에는 어떠한 에러 메시지를 내는지 관찰하라.
#### 다) s[1:-1]는 어떤 결과를 내는가?
#### 라) s[3:-3]는 어떤 결과를 내는가?

### 8. 다음과 같은 문자열이 주어져 있다.
~~~
s = '''We propose to start by making it possible to teach programming in Python, an existing scripting language, and to focus on creating a new development environment and teaching materials for it.'''
~~~
#### s.split()을 하면 위의 문자열이 단어 단위로 분리된 문자열 리스트를 얻게 된다. 이 리스트에 저장된 단어들을 알파벳 순으로 정렬하고(리스트 연산), 각 단어를 순서대로 출력하라. (for 문)
~~~
s = '''We propose to start by making it possible to teach programming in Python, an existing scripting language, and to focus on creating a new development environment and teaching materials for it.'''
arr = s.split()
arr.sort()
for s in arr:
    print(s)
~~~

### 9. while 문을 이용하여 1부터 20까지의 홀수를 출력하라.
~~~
a = 1
while a <= 20:
    if (a % 2 == 1):
        print(a)
    a += 1
~~~

### 10. while 문을 이용하여 20부터 0까지 짝수를 출력하라.
~~~
a = 20
while a >= 1:
    if (a % 2 == 0):
        print(a)
    a -= 1
~~~

### 11. while 문을 이용하여 1부터 100까지의 홀수의 합을 계산하라.
~~~
a = 1
sum = 0
while a <= 100:
    if (a % 2 == 1):
        sum += a
    a += 1
print(sum)
~~~

### 12. 다음 코드를 테스트해보고 결과를 말하라.
~~~
for el in range(-10, 110):
     exec('x = %d' % el)
     exec('y - %d' % el)
     print el, x is y
~~~
- -10에서 109까지 숫자와 True가 출력된다.