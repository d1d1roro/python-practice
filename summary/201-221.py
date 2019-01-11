# 6. 튜플
# 1. 튜플의 연산
# t = 1, 2, 3 # 튜플로 인식
# print(t)

# x, y, z = 1, 2, 3
# print(x, y, z)

# x = 1
# y = 2
# x, y = y, x
# print(x, y)

# 2. 패킹과 언패킹
# 패킹: 한 튜플 안에 여러 개의 데이터를 넣는 것
# t = 1, 2, 'hello'
# 언패킹: 튜플에서 데이터를 꺼내 오는 것
# x, y, z= t
# print(x, y, z, t)
# 언패킹은 리스트도 가능
# a = ['foo', 'bar', 4, 5]
# [x, y, z, w] = a

# 3. 리스트와의 공통점과 차이점
# 리스트와 튜플 상호 변환 가능
# T = (1, 2, 3, 4, 5)
# L = list(T)
# L[0] = 100
# print(L)
# T = tuple(L)
# print(T)

# 4. 튜플을 사용하는 경우
# 1) 함수에 있어서 하나 이상의 값을 리턴하는 경우
# def calc(a, b):
#     return a+b, a*b
# x, y = calc(5, 4)
# print(x, y)

# 2) 문자열 포매팅
# print('id: %s, name: %s' % ('gslee', 'GanSeong'))

# 3) 튜플에 있는 값들을 함수 인수로 사용할 때
# args = (4, 5)
# print(calc(*args))

# 4) 그 이외에 고정된 값을 표현하기 위해
# d = {'one': 1, 'two': 2}
# print(d.items())

# 5. 경로명 다루기

# 6. url 다루기