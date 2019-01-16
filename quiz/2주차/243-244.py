# 1. 다음과 같은 if 문을 대신할 수 있는 코드를 사전을 이용해서 작성하라.
# if menuselection == 'odeng':
#     price = 300
# elif menuselection == 'sundae':
#     price = 400
# elif  menuselection == 'mandu':
#     price = 500
# else:
#     price = 0

# menuselection = {
#     'odeng': 300,
#     'sundae': 400,
#     'mandu': 500
# }

# 2. 사전의 값은 어떠한 객체라도 무방하다. 키로 사용될 수 있는 객체는 무엇인가?
# 리스트와 사전 객체를 제외한 상수 객체 (문자열, 튜플)

# 3. 다음 코드를 수행했을 경우에 e와 f의 출력 결과를 예측해 보아라.
# L1 = [1, 2, 3]
# L2 = [4, 5, 6]
# d = {'low': L1, 'high': L2}
# e = d
# f = d.copy()
# d['low'] = [10, 20, 30]
# d['high'][1] = 500

# e값만 변경될 줄 알았는데, d['high'][1] 의 경우, 모든 값이 복사됨
# print(e, f)

# 4. 사전 {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5} 이 주어져 있을 때, 키의 알파벳을 기준으로 순서대로
# (키, 값) 쌍을 출력하라. 또 반대로 값을 중심으로 작은 값부터 큰 값 순서대로 (키, 값) 쌍을 출력하라.
# d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
# for k, v in sorted(d.items(), key=lambda item:item[0]):
#     print(k, v)
# for k, v in sorted(d.items(), key=lambda item:item[1]):
#     print(k, v)

# 5. 다음과 같은 두 개의 리스트가 주어져 있다.
# ['one', 'two', 'three', 'four'], [1, 2, 3, 4]
# 이들로부터 {'one': 1, 'two': 2, 'three': 3, 'four': 4} 사전을 만들어 내도록 하라.
# a, b = ['one', 'two', 'three', 'four'], [1, 2, 3, 4]
# c = dict(list(zip(a, b)))
# print(c)

# 6. 어떤 문자열(예: s = 'one two one two three four')이 주어져 있을 때, 사전을 이용하여 주어진 문자열의 각 단어를 중복되지 않게
# 한 번씩만 출력하여라.
# s = 'one two one two three four'
# d = {d for d in s.split()}
# print(d)

# 7. 다음 주어진 문자열에서 모든 대문자를 소문자로 변환하고, 문자 ',' 와 '.'를 없앤 후에 각 단어를 순서대로 출력하시오.
# 단, 중복적인 한 단어는 한 번만 출력되어야 하며 단어가 문자열에서 발생한 횟수도 함께 출력한다.
# s = 'We propose to start by making it possible to teach programming in Python, an existing scripting language, and to focus on creating a new development environment and teaching materials for it.'
# s = s.lower().replace(',', '').replace('.', '').split()
# r = {s: 0 for s in s}
# for v in s:
#     for d in r:
#         if (v == d):
#             r[d] = r[d] + 1

# print(sorted(r.items()))

# 8. 문자열의 'a', 'b', 'c', 'd' 각 문자에 대해서 'w', 'x', 'y', 'z' 으로 또한, 'w', 'x', 'y', 'z' 는 'a', 'b', 'c', 'd'로 변환하는
# 프로그램을 작성하라. (예: cabsz = ywxsd)
# d = {
#     'a': 'w',
#     'b': 'x',
#     'c': 'y',
#     'd': 'z'
# }

# dr = {}
# for k in d:
#     dr.setdefault(d[k], k)

# s = 'cabsz'
# r = ''
# sr = list(s)
# for v in sr:
#     if v in d:
#         r += d.get(v)
#     elif v in dr:
#         r += dr.get(v)
#     else:
#         r += v

# print(s, r)