# 1. range 함수와 유사한 frange 함수를 만들어라. frange는 실수 리스트를 리턴한다.
# frange의 기본 시작 값은 0.0이고 기본 단계 값을 0.25이다. frange(5.0), frange(1.0, 5.0), frange(1.0, 3.0, 0.1) 등이 동작하도록 하라.
# def frange(s, *args):
#     start = 0.0
#     end = 0.0
#     step = 0.25

#     if len(args) == 0:
#         end = s
#     elif len(args) == 1:
#         start = s
#         end = args[0]
#     elif len(args) == 2:
#         start = s
#         end = args[0]
#         step = args[1]
    
#     res = []
#     num = start

#     while num < end:
#         res.append(round(num, 4))
#         num += step
    
#     return res

# print(frange(5.0))
# print(frange(1.0, 5.0))
# print(frange(1.0, 5.0, 0.1))

# 2. 조합 논리 회로 1비트 덧셈기 adder 를 시뮬레이션 하고자 한다. adder 는 두 개의 0 또는 1의 값을 가지는 인수를 받고 두 개의 값을 리턴한다.
# 리턴 값은 덧셈 결과를 두 자리로 한 결과이다. adder(0, 0)의 결과는 (0, 0)이고, adder(1, 1)은 (1, 0)이다.
# adder(0, 1)이나 adder(1, 0)은 (0, 1)의 결과를 낳는다. 이 adder 함수를 작성하여라.

# 3. 함수 sum을 정의하라. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산하다. 예를 들면 sum()은 0을, sum(1, 2)은 3을,
# sum(1, 5, 7, 2, 3)은 18을 리턴한다. (가변 인수)
# def sum(*args):
#     res = 0
#     if len(args) == 0: return res

#     for i in args:
#         res += i
#     return res

# print(sum(), sum(1, 2), sum(1, 5, 7, 2, 3))

# 4. 이미지 파일을 작게 표시하기 위한 썸네일이라는 작은 이미지 파일들이 있다.
# 이 파일들은 원래의 이미지 파일에 _thumb란 이름이 추가로 붙는다. 예를 들면 a.jpg 의 썸네일 파일은 a_thumb.jpg이다.
# 이미지 파일 이름들이 리스트에 담겨 있을 때, filter를 이용하여 여기서 일반 이미지 파일만 혹은 썸네일 파일만 골라 내어라.
# li = ['a.jpg', 'a_thumb.jpg', 'b.jpg', 'b_thumb.jpg', 'c.jpg']
# res1 = filter(lambda s: s.endswith('_thumb.jpg'), li)
# res2 = filter(lambda s: not s.endswith('_thumb.jpg'), li)
# print(list(res1), list(res2))

# 5. 주어진 문자열(예: as soon as possible)에서 각 단어의 첫 글자를 취해서 하나의 단어를 만들어라.
# split, map, join 이용
# s = 'as soon as possible'
# arr = s.split()
# res = map(lambda s: list(s)[0], arr)
# res = "".join(list(res))
# print(res)

# 6. data.txt 파일에 다음과 같은 내용이 저장되어 있다. 이들을 읽어 리스트 x에 [1, 4, 7], 리스트 y에 [2, 5, 8],
# 리스트 z에 [3, 6, 9]가 저장되도록 map 함수를 이용하여 작성하라. (리스트 안의 숫자는 모두 정수형이어야 한다.)
# 1 2 3
# 4 5 6
# 7 8 9

# 7. N!(팩토리얼)을 계산하는 함수 fact를 재귀적 함수로 만들어라.
# def fact(num):
#     if num <= 1:
#         return 1
#     return num * fact(num-1)
# print(fact(3))

# 8. 리스트의 구조를 변경하지 말고 리스트의 값을 바꾸는 함수를 작성하고 시험하라. 예를 들어 [3, 2, [3, [[3], 4]]] 에서
# 3을 5로 바꾼다면 [5, 2, [5, [[5], 4]]] 결과가 나와야한다. (재귀적 프로그래밍)
