## 4. 라인 단위로 파일 쓰기
# lines = ['first line1\n', 'second line1\n', 'third line1\n']
# f = open('t1.txt', 'w')
# f.writelines(lines)
# f.write(''.join(lines))
# lines = ['first line2', 'second line2', 'third line2']
# f.write('\n'.join(lines))
# f.close()

# f = open('t1.txt')
# print(f.read())

# 예제1. 텍스트 t.txt의 단어 수를 출력하는 프로그램을 작성하라. 여기서 단어란, 공백으로 분리된 문자의 모임을 뜻한다.
# f = open('t1.txt')
# text = f.read()
# print(len(text.split())) # len(open('t.txt').read().split())

# 예제2. 텍스트 파일 t.txt의 라인 수를 출력하는 프로그램을 작성하라.
# f = open('t1.txt')
# text = f.read()
# print(len(text.split('\n')))
# print(text.count('\n'))
# print(len(f.readlines()))
# print(len(open('t1.txt').readlines()))
# print(open('t1.txt').read().count('\n'))

# 예제3. 텍스트 파일 t.txt의 문자 수를 출력하는 프로그램을 작성하라.
# f = open('t1.txt')
# print(len(f.read()))

# import os
# print(os.linesep)

# 5. 파일에서 원하는 만큼의 문자 읽기
# f = open('t1.txt')
# print(f.read(10))

# f = open('t1.txt')
# f.seek(6)
# print(f.tell())
# print(f.read(1))

# import os

# f.seek(-3, 2)
# 위 안됨 / 아래와 같은 형태로 해야됨
# In text files (those opened without a b in the mode string), 
# only seeks relative to the beginning of the file [os.SEEK_SET] are allowed...

# f.seek(0, os.SEEK_END)
# f.seek(f.tell() - 3, os.SEEK_SET)

# print(f.tell())
# print(f.read(1))

import sys
# f = open('t3.txt', 'w')
# stdout = sys.stdout
# sys.stdout = f
# print('Sample output')
# print('Good')
# print('Not Good')
# f.close()
# sys.stdout = stdout

# import StringIO
# python3: The StringIO and cStringIO modules are gone. 
# Instead, import the io module and use io.StringIO or io.BytesIO for text and data respectively.

# from io import StringIO
# stdout = sys.stdout
# sys.stdout = f = StringIO()
# print('Sample output')
# print('Good')
# print('Not Good!')
# sys.stdout = stdout
# s = f.getvalue()
# print('Done--')
# print(s)

# from io import StringIO
# s = '''
# Python is a cool little language.
# It is well designed, compact, easy to learn and fun to program in.
# Python strongly encourages the programmer to grogram in an OO-way,
# but does not require it.
# In my opinion, it is one of the best lnaguages to use when learing OO-programming.
# '''
# f = StringIO(s)
# print(f.read().upper())

# 11. 지속 모듈
# import pickle

# phone = {
#     'tom': 4358382,
#     'jack': 9465225,
#     'jim': 6852325,
#     'Joseph': 6584325
# }
# List = ['string', 1234, 0.2345]
# Tuple = (phone, List)
# f = open('t2.txt', 'wb')
# pickle.dump(Tuple, f)
# f.close()

# f = open('t2.txt')
# x, y = pickle.load(f)
# print(x, y)