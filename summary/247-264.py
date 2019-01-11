# print(round(1.1))

# import math
# print(math.floor(1.1))
# print(math.ceil(1.0))

# octtab = {
#     '0': '000',
#     '1': '001',
#     '2': '010',
#     '3': '011',
#     '4': '100',
#     '5': '101',
#     '6': '110',
#     '7': '111'
# }

# def bin1(d, width=0):
#     "integer to binary(string)" 
#     s = "%o" % d
#     b = ''
#     for el in s:
#         b += octtab[el]
#     if width > 0:
#         if len(s) > width:
#             return b[:width]
#         b = b.zfill(width)
#     return b
# print(bin1(23, 7))

# import locale
# locale.setlocale(locale.LC_ALL, "")
# print(locale.format("%d", 10030405, 1))

# L = ['파란 하늘', 'blue sky', 1, 1234, 1/3.0]
# for s in L:
#     print('s', s)
#     print('str(s)', str(s))
#     print('repr(s)', repr(s))
#     print()

# f = open('t.txt', 'r+')
# f.write('test123')
# f.close()
# line = f.readline()
# while line:
#     print(line, end='')
#     line = f.readline()

# for line in f.readlines():
#     print(line, end='')

# for line in f:
#     print(line, end='')

# s = [1, 2, 3, 4, 5]
# t = s[1:4]
# print(id(s), id(t))
# s[2] = 100
# print(s, t)

# s = [[1, 2, 3], [4, 5, 6]]
# t = s[:]

# d = {
#     id(s): id(t),
#     id(s[0]): id(t[0]),
#     id(s[0][0]): id(t[0][0])
# }

# print(d)

# s[0] = 100
# print(s, t)

# s[0][0] = 100
# print(s, t)

# L1 = [1, 2, 3]
# L2 = [4, 5, 6]
# d = {'low': L1, 'high': L2}
# e = d
# f = d.copy()
# d['low'] = [10, 20, 30]
# d['high'][1] = 500

import copy

s = [[1, 2, 3], [4, 5, 6]]
t = copy.deepcopy(s)

d = {
    id(s): id(t),
    id(s[0]): id(t[0]),
    id(s[0][0]): id(t[0][0]),
    id(s[0][1]): id(t[0][1]),
    id(s[0][2]): id(t[0][2])
}

print(d)

# s[0] = 100
# print(s, t)

# s[0][0] = 100
# print(s, t)
