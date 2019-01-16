# file 179-207.py

# # a = ['spam', 'eggs', 123, 1234]
# a[0:2] = [1]
# print(a)

# a = [1, 12, 123, 1234]
# a[0:2] = []
# print(a) 

# a = [123, 1234]
# a[1:1] = ['spam', 'ham']
# print(a)

# a[:0] = a
# print(a)

# a = list(range(4))
# a[::2] = range(0, -2, -1)
# print(a)

# a[::2] = range(3)
# print(a)

# lt = [('one', 1), ('two', 2), ('three', 3)]
# for t in lt:
#     print(t[0], t[1])

# for t in lt:
#     print('%s, %s' % t)

# for name, num in lt:
#     print(name, num)

# LL = [['one', 1], ['two', 2], ['three', 3]]
# for name, num in LL:
#     print(name, num)

# L = [1, 5, 3, 9, 8, 4, 2]
# L.sort()
# print(L)

# L = [1, 5, 3, 2, 4, 6]
# L.sort(key=lambda a: a, reverse=True)
# print(L)

# L = [('lee', 5, 38), ('kim', 3, 28), ('jung', 10, 36)]
# L.sort()
# print(L)

# L.sort(key=lambda a: a[1])
# print(L)

# L.sort(key=lambda a: a[2])
# print(L)

# L = [k * k for k in range(10)]
# print(L)

# L = [k * k for k in range(10) if k%2]
# print(L)

# seq1 = 'abc'
# seq2 = (1, 2, 3)
# print([(x, y) for x in seq1 for y in seq2])

# GNU = ['is not Unix']
# GNU.insert(0, GNU)
# print(GNU)
# print(GNU[0])
# print(GNU[0][0])
# print(GNU[0][0][0])

# 08. 순차적인 정수 리스트 만들기
# print(list(range(10)))
# for el in range(10):
#     print(el, el*2.54)

# sun, mon, tue, wed, thu, fri, sat = range(7)
# print(sun, mon)

# 9. 지역적으로 사용 가능한 이름 리스트 얻기
# print(dir()) # ['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# a = 100
# print(dir())
# print(__name__)

import sys
# print(dir(sys))

# 10. 명령행 인수 처리
# 10-1 명령행 인수 얻기
# print(sys.argv) # ['c:\\Users\\iser\\Desktop\\practice\\python\\test\\summary\\179-207.py']

# print(sys.argv[1:])

# 10-2 명령행 옵션 처리
# 옵션 처리의 예
import getopt
# options, args = getopt.getopt(sys.argv[1:], 'a:b:c:')
# for op, p in options:
#     if op == '-a':
#         print('option a', p)
#     elif op == '-b':
#         print('option b', p)
#     elif op == '-c':
#         print('option c', p)
#     else:
#         print('unknown option', op)
# print(args)

# checkext = 1
# verbose = 1
# maxpage = 500

# opts, args = getopt.getopt(sys.argv[1:], 'xvm:')

# for o, a in opts:
#     if o == '-x':
#         checkext = not checkext
#     if o == '-v':
#         verbose = verbose + 1
#     if o == '-m':
#         maxpage = int(a)
# print(checkext, verbose, maxpage)

# 11. 배열 표현하기
# 11-1 리스트로 1차원 배열 표현하기
# a = [1, 2, 3, 4, 5]
# b = list(range(10))
# print(a, b)

# a = [0] * 10
# print(a)

# 11-2 내용 없는 리스트 미리 생성하기
# N = [20, 15, 39, 2, 7, 5, 223, 75, 46, 87]
# M = [3, 5, 9, 2, 7]
# L = [None] * 10
# for k in M:
#     L[k] = k * N[k]
# print(L)

# 11-3 리스트로 2차원 배열(행렬) 표현하기
# mat = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(mat, mat[1][2])

# 주의: 다음과 같이 할 경우, 레퍼런스의 복사가 됨
# mat = [[0] * 4] * 3
# mat[0][0] = 100 # 모든 1차원 배열 값이 변경됨
# print(mat)

# 피하는 방법
# mat = []
# for x in range(3):
#     mat.append([0] * 4)
# print(mat)
# mat[0][0] = 100
# print(mat)

# mat = [[0] * 4 for x in range(3)]
# print(mat)
# mat[0][0] = 100
# print(mat)

# 11-4 array 모듈 이용하기
# | 타입 코드 | C 타입           | 최소 바이트 수 |
# |:---------:|------------------|----------------|
# | 'c'       | Character        | 1              |
# | 'b'       | Signed integer   | 1              |
# | 'B'       | Unsigned integer | 1              |
# | 'h'       | Signed integer   | 2              |
# | 'H'       | Unsigned integer | 2              |
# | 'i'       | Signed integer   | 2              |
# | 'I'       | Unsigned integer | 2              |
# | 'l'       | Signed integer   | 4              |
# | 'L'       | Unsigned integer | 4              |
# | 'f'       | Floating point   | 4              |
# | 'd'       | Floating point   | 8              |

# array(typecode [, initializer])

# 1) 초기값으로 생성
from array import *
# a = array('i', range(10))
# print(a)
# a = array('i', [0] * 10)
# print(a)

# 2) 동적으로 생성하기 (append, insert, extend 메서드 이용)
# a = array('i')
# a.append(1)
# a.append(4)
# a.insert(1, 2)
# a.extend(array('i', [1, 2, 3, 4, 5]))

# 3) 배열 참조
# del a[:3]
# print(a)

# a = array.array('i')
# print(dir(a))

# 12. 디렉토리의 파일 목록 얻기
# 12-1 목록 얻기
