# 13. 예외 처리
# 5-1. 내장 예외의 발생
# class SquareSeq:
#     def __init__(self, n):
#         self.n = n
#     def __getitem__(self, k):
#         if k >= self.n or k < 0:
#             raise IndexError
#         return k*k
#     def __len__(self):
#         return self.n

# s = SquareSeq(10)
# print(s[2], s[4])
# for x in s:
#     print (x, end=' ')
# print(s[20])

# 5-2. 사용자 클래스 예외 발생시키기
# import sys
# class Big(Exception):
#     pass
# class Small(Big):
#     pass
# def dosomething1():
#     x = Big()
#     raise x
# def dosomething2():
#     raise Small()

# for f in (dosomething1, dosomething2):
#     try:
#         f()
#     except Big:
#         print(sys.exc_info())

# 5-3. 예외값 전달하기
# class MessageClass:
#     def __init__(self, message, dur):
#         self.message = message
#         self.duration = dur
# def f():
#     m = MessageClass('message', 10)
#     print(id(m))
#     raise Exception(m)

# try:
#     f()
# except Exception as a:
#     print(a, a.__class__.__name__, id(a))
#     print(a.args[0], a.args[0].__class__.__name__, id(a.args[0]))
#     print(a.args[0].duration, a.args[0].message)

# 5-4. 사용자 문자열 예외 발생
# MyException = 'my excpetion'
# def dosomething():
#     raise MyException
# try:
#     dosomething()
# except MyException:
#     print('Exception occured')

# try:
#     dosomething()
# except 'my exception':
#     print('Exception occured')

# 6. assert문으로 예외 발생시키기
# a = 30
# margin = 2 * 0.2
# if __debug__:
#     assert margin > 10, 'not enough margin %s' % margin

# 14. 약한 참조, 반복자, 발생자
# 약한 참조: 레퍼런스 카운트로 고려되지 않는 레퍼런스
# 순환적인 참조에 이용될 수 있다.

# 2-3. 클래스에 반복자 구현하기
# class Seq:
#     def __init__(self, fname):
#         self.file = open(fname)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         line = self.file.readline()
#         if not line: raise StopIteration
#         return line
# S = Seq('t1.txt')
# for line in S:
#     print(line, end='')

# 2-4. 사전의 반복자
# https://legacy.python.org/dev/peps/pep-0469/

# import math
# def accum(sum, a):
#     return sum+a
# sum = 0
# for sum in iter(lambda: accum(sum, math.pi), None):
#     if sum >= 20: break
#     print(sum, end=' ')

# 2-7. itertools 모듈
# from itertools import *
# L1 = [1, 2, 3]
# L2 = [4, 5, 6]
# for k in chain(L1, L2):
#     print(k, end=' ')
# for k in (L1+L2):
#     print(k, end=' ')
# for k in count(10):
#     print(k, end=' ')
# names = ['gslee', 'kim', 'park']
# for regNo, name in zip(count(140), names):
#     print(regNo, name)
# for k in cycle([1, 2, 3]):
#     print(k, end=' ')

# 참이 되는 한 데이터를 버리고 거짓이 되는 이후의 데이터를 끝까지 취한다.
# for k in dropwhile(lambda x: x<3, [1, 2, 3, 4, 5, 1, 2]):
#     print(k, end=' ')

# 참이 되는 한 데이터를 취하고 거짓이 되면 멈춘다.
# for k in takewhile(lambda x: x<3, [1, 2, 3, 4, 5, 1, 2]):
#     print(k, end=' ')

# L = [(1, 2), (2, 3), (1, 2), (4, 2)]
# for key, group in groupby(sorted(L)):
#     print(key, list(group))

# from operator import itemgetter
# for key, group in groupby(sorted(L, key=itemgetter(1)), key=itemgetter(1)):
#     print(key, list(group))

# s = 'I like python I like programming'
# for key, group in groupby(sorted(s.split())):
#     print(key, len(list(group)))

# a = [1, 2, 3, 4]
# b = [10, 20, 30, 40]
# print(dict(zip(a, b)))

# print(list(starmap(lambda x, y: x+y, L)))

# print(list(filterfalse(lambda x: x%2, range(10))))

# L = [1, 2, 6, 4, 3, 8, 7, 6]
# for ele in islice(L, 0, len(L), 2):
#     print(ele, end=' ')

# for k in repeat(L, 2):
#     print(k, end=' ')

# i1, i2 = tee(L)
# for k in i1:
#     print(k)

# 3. 발생자
# 기존의 함수 호출 방식은 함수가 호출될 때 인수들과 내부 변수들이 새로운 영역(대부분은 스택)에 만들어지고 리턴할 때 메모리에서 사라진다.
# 만일 함수가 호출된 후에 되돌아갈 때, 메모리가 해제되지 않고 그대로 남아 있다면 어떨까?
# 그리고 다시 그 함수가 호출될 때 이전에 수행이 종료되었던 지점 이후를 계속 진행한다면 어떨까?
# 이것이 발생자다. 발생자란 (중단된 시점부터) 재실행 가능한 함수라고 할 수 있다.
# from __future__ import generators
# def generate_ints(N):
#     for i in range(N):
#         yield i

# gen = generate_ints(3)
# print(gen.__next__())

# for i in generate_ints(5):
#     print(i, end=' ')

# 3-2. 발생자 구문
# Q. 리스트 내장 구문으로 작성하면 외부에서 변수 참조가 가능하다는데, 안 됨.

# 3-3. 발생자의 활용 - 피보나치 수열
# def fibonacci(a=1, b=1):
#     while 1:
#         yield a
#         a, b = b, a + b
# # t = fibonacci()
# # for i in range(11):
# #     print(t.__next__())

# for k in fibonacci():
#     if k > 100: break
#     print(k, end=' ')

# 3-4. 발생자의 활용 - 홀수 집합 만들기
# class Odds:
#     def __init__(self, limit=None):
#         self.data = -1
#         self.limit = limit
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.data += 2
#         if self.limit and self.limit <= self.data:
#             raise StopIteration
#         return self.data

# for k in Odds(20):
#     print(k, end=' ')

# print(list(Odds(20)))

# def odds(limit=None):
#     k = 1
#     while not limit or limit >= k:
#         yield k
#         k += 2
# for k in odds(20):
#     print(k, end=' ')

# 3-5. 발생자의 활용 예 - 하나씩 건너뛰어서 값 취하기
# def alternating(a):
#     ta = iter(a)
#     while 1:
#         ta.__next__()
#         yield ta.__next__()
# for x in alternating([1, 2, 3, 4, 5, 6, 7]):
#     print(x, end=' ')

# from itertools import *
# for x in islice([1, 2, 3, 4, 5, 6, 7], 1, 7, 2):
#     print(x, end=' ')

# 3-6. 발생자의 활용 - 트리 탐색
# class Tree(object):
#     def __init__(self, data=None, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right
#     def inorder(self):
#         if self.left:
#             for x in self.left.inorder():
#                 yield x
#         yield self
#         if self.right:
#             for x in self.right.inorder():
#                 yield x

#     def __iter__(self):
#         return self.inorder()

#     def __repr__(self, level=0, indent="    "):
#         s = level * indent + self.data
#         if self.left:
#             s = s + "\n" + self.left.__repr__(level+1, indent)
#         if self.right:
#             s = s + "\n" + self.right.__repr__(level+1, indent)
#         return s
    
# def tree(List):
#     n = len(List)
#     if n == 0:
#         return None
#     i = int(n / 2)
#     return Tree(List[i], tree(List[:i]), tree(List[i+1:]))
    
# if __name__ == '__main__':
#     t = tree('abcdef')
#     print(t)
#     print()
#     for el in t.inorder():
#         print(el.data, end=' ')

# 3-7 발생자의 활용 - 중첩 리스트를 단일 리스트로 만들기
# def traverse(t):
#     if not isinstance(t, list):
#         return [t]
#     res = []
#     for el in t:
#         res.extend(traverse(el))
#     return res
# a = [[1, 2, 3], 4, 5, [6, 7], [8, 9, 10]]
# b = traverse(a)
# print(b)

# def traverse(l):
#     for el in l:
#         if isinstance(el, list):
#             for k in traverse(el):
#                 yield k
#         else:
#             yield el
# a = [1, 2, 3, [4, 5], 6, [7, [8, [9]], 10]]
# b = list(traverse(a))
# print(b, max(traverse(a)), min(traverse(a)))
#### Page 512

#### Page 603
# 17. 소켓 프로그래밍
# http://www.w3big.com/ko/python3/python3-socket.html
