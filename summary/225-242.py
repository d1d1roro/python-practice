# 7. 사전 및 집합
# 1. 사전 객체의 기초 연산
# d = {}
# d['str'] = 'abc'
# d[1] = 4
# d[(1, 2, 3)] = 'tuple'
# d[[1, 2, 3]] = 'list' # unhashable type: 'list'
# def add(a, b):
#     return print(a+b)
# def sub(a, b):
#     return print(a-b)
# action = {0: add, 1: sub}
# action[0](4, 5)
# action[1](4, 5)

# keys = ['one', 'two', 'three']
# values = (1, 2, 3)
# print(list(zip(keys, values)))
# print(dict(zip(keys, values)))

# quiz
# 1. 사전의 키로 사용될 수 있는 자료는 어떤 것들이 있는지 시험해 보라. 예를 들어 다음과 같이 사용할 수 있는가?
# d = {}
# d[(1,2,3)] = 10
# d[[1,2,3]] = 10 # 상수만 가능
# d[{1:2, 3:4}] = 10 # 상수만 가능

# 2. 사전의 값으로 사용될 수 있는 자료형에 어떤 제약이 있는지 조사해 보라. 다음이 모두 가능한가?
# d[10] = (1, 2, 3) # 가능
# d[10] = [1, 2, 3] # 가능
# d[10] = {1:2, 3:4} # 가능

# 2. 사전 객체의 메서드
# phone = {'jack': 9465215, 'jim': 1111, 'Joseph': 6584321}
# print(phone.keys())
# print(phone.values())
# print(phone.items())
# print('jack' in phone)
# print('lee' in phone)

# 메서드
# |         메서드        | 역할                                                     |
# |:---------------------:|----------------------------------------------------------|
# | keys()                | 키 리스트                                                |
# | values()              | 값 리스트                                                |
# | items()               | (key, value) 리스트                                      |
# | key in D              | 멤버십 테스트                                            |
# | clear()               | 모든 아이템 삭제                                         |
# | copy()                | 사전 복사(Shallow copy)                                  |
# | get(key [, x])        | 값이 존재하면 D[key], 아니면 x 리턴                      |
# | setdefault(key [, x]) | get()과 같으나 값이 존재하지 않을 때 값을 설정(D[key]=x) |
# | update(b)             | for k in b.keys(): D[k] = b[k]                           |
# | popitem()             | (키, 값) 튜플을 리턴, 사전에서 항목 제거 (앞부터 pop)       |
# | pop(key)              | key 항목의 값 리턴, 사전에서 제거                        |

# copy 비교

# 객체 공유
# p = phone
# phone['jack'] = 1234
# print(phone, p)

# 객체 생성 (객체 공유X)
# ph = phone.copy()
# phone['jack'] = 1234
# print(ph, phone)

# quiz
# 1. 다음 두 개 코드의 차이를 설명하라.
# a = d # 객체 공유
# a = d.copy() # 객체 생성/복사, 객체 공유 X

# 2. 다음 두 개 코드의 차이를 설명하라.
# d = {'a': 1, 'b': 2}
# del d['a'] # 아이템 삭제
# d['a'] = None # 아이템 값 변경
# print(d)

# 3. 심볼 테이블
# 심볼 테이블: 변수들이 저장되는 공간
# 키: 심볼 이름, 값: 심볼의 값

# 3-1. 전역/지역 심볼 테이블
# a = 1
# b = 100
# name = 'gslee'
# dic = {'Python': 'Good', 'Perl': 'Not Good'}
# print(globals())
# print(locals()) # 대화형 최상위 모드에서의 globals(), locales() 별 차이가 없음

# 3-2. 객체의 심볼 테이블
# 이름 공간(심볼들이 저장되는 공간)을 가지는 모든 객체는 심볼 테이블을 소유
# __dict__ 속성을 이용하여 해당 객체의 심볼 테이블을 얻을 수 있음
# class c:
#     x = 10
#     y = 10
# c.a = 100
# c.b = 200
# print(c.__dict__)

# 파이선 2.1 부터는 함수에도 속성 값을 지정할 수 있음.
# def f():
#     pass # 아무것도 하지 않습니다. 문법적으로 문장이 필요하지만, 프로그램이 특별히 할 일이 없을 때 사용할 수 있습니다.
# f.a = 1
# f.b = 2
# print(f.__dict__)

# 4. 사전을 for 문으로 참조하기
# D = {'b': 2, 'a': 1, 'c': 3}
# for key in D.keys():
#     print(key, D[key])

# 2.2 이상부터는 D.keys() 를 하지 않고도 객체 자체로 사용 가능
# for key in D:
#     print(key, D[key])

# for key, value in D.items():
#     print(key, value)

# items = D.items()
# items = sorted(items)

# for key, value in items:
#     print(key, value)

# d = {'three': 3, 'two': 2, 'one': 1}
# for key, value in sorted(d.items(), key=lambda item:item[1]):
#     print(key, value)

# 예제 1. 다음 예제는 사전에 이름과 전화번호를 등록하고 출력한다.
# def print_menu():
#     print('1. 전화 번호 출력')
#     print('2. 전화 번호 추가')
#     print('3. 전화 번호 삭제')
#     print('4. 전화 번호 찾기')
#     print('5. 종료')
#     print()

# def print_dic(numbers):
#     print("전화번호: ")
#     for name in numbers:
#         print("이름: ", name, "\t 번호: ", numbers[name])
#     print()

# def add_member(numbers):
#     print("이름과 번호 추가")
#     name = input("이름: ")
#     phone = input("번호: ")
#     numbers[name] = phone

# def remove_member(numbers):
#     print("이름과 번호 삭제")
#     name = input("이름: ")
#     if name in numbers:
#         del numbers[name]
#     else:
#         print(name, "은 없습니다")

# def lookup_member(numbers):
#     print("번호 찾기")
#     name = input("이름: ")
#     if name in numbers:
#         print("번호: ", numbers[name])
#     else:
#         print(name, "을 찾을 수 없습니다.")

# numbers = {}
# menu_choice = 0
# print_menu()
# while menu_choice != "5":
#     menu_choice = input("번호를 입력해 주세요[1-5]: ")
#     if menu_choice == "1":
#         print_dic(numbers)
#     elif menu_choice == "2":
#         add_member(numbers)
#     elif menu_choice == "3":
#         remove_member(numbers)
#     elif menu_choice == "4":
#         lookup_member(numbers)
#     if menu_choice != "5":
#         print_menu()

# 예제2. 함수 레퍼런스를 사전에 저장해 두었다가 함수를 호출하는 예제.
# def add(a, b):
#     return a+b

# def sub(a, b):
#     return a-b

# def mul(a, b):
#     return a*b

# def div(a, b):
#     return a/b

# def choose_menu():
#     print("What do you want to do?")
#     print("add, sub, mul, div, quit")
#     return input("Your choide: ")

# menu = {
#     'add': add,
#     'sub': sub,
#     'mul': mul,
#     'div': div
# }
# choice = choose_menu()
# while choice != 'quit':
#     if choice in menu:
#         x = eval(input('first value: '))
#         y = eval(input('second value: '))
#         print(menu[choice](x, y))
#     choice = choose_menu()

# 5. 집합 자료형
# 2.4 부터 set / frozenset 집합 내장 자료형이 새롭게 도입
# 변경 불가능한 값들을 저장하는 순서가 없는 집합적 자료형
# set: 자체는 변경 가능 자료형
# frozenset: 변경 불가능 자료형, 자신을 변경시키는 연산을 수행할 수 없다.

# 적용 가능한 연산들
# |            연산           | 동등한 표현 | 내용                        |
# |:-------------------------:|-------------|-----------------------------|
# | len(s)                    |             | 원소의 수                   |
# | x in s                    |             | x가 집합 s의 원소인가?      |
# | x not in s                |             | x가 집합 s의 원소가 아닌가? |
# | s.issubset(t)             | s <= t      | s가 t의 부분집합?           |
# | s.issuperset(t)           | s >= t      | s가 t의 포함집합?           |
# | s.union(t)                | s | t       | 새로운 s와 t의 합집합       |
# | s.intersection(t)         | s & t       | 새로운 s와 t의 교집합       |
# | s.difference(t)           | s - t       | 새로운 s와 t의 차집합       |
# | s.symmetric_difference(t) | s ^ t       | 새로운 s와 t의 배타집합     |
# | s.copy()                  |             | 집합s를 얕은 복사           |

# set 자료형에만 적용 가능한 연산들
# |               연산               | 동등한 표현 | 내용                                                                              |
# |:--------------------------------:|-------------|-----------------------------------------------------------------------------------|
# | s.update(t)                      | s |= t      | s와 t의 합집합을 s에 저장                                                         |
# | s.intersection_update(t)         | s &= t      | s와 t의 교집합을 s에 저장                                                         |
# | s.difference_update(t)           | s -= t      | s와 t의 차집합을 s에 저장                                                         |
# | s.symmetric_difference_update(t) | s ^= t      | s와 t의 배타집합을 s에 저장                                                       |
# | s.add(x)                         |             | 원소 x를 s에 추가                                                                 |
# | s.remove(x)                      |             | 원소 x를 s에서 제거; 없으면 KeyError 예외 발생                                    |
# | s.discard(x)                     |             | 원소 x가 있다면 s에서 제거                                                        |
# | s,pop()                          |             | s에서 임의의 원소를 하나 리턴하고 집합에서는 제거; 빈 집합이면 KeyError 예외 발생 |
# | s.clear()                        |             | 집합 s의 모든 원소 삭제                                                           |