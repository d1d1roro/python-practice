# class A(object):
#     def save(self):
#         print('A save called')
# class B(A):
#     def save(self):
#         print('B save called')
#         super(B, self).save()
# class C(A):
#     def save(self):
#         print('C save called')
#         super(C, self).save()
# class D(B, C):
#     def save(self):
#         print('D save called')
#         super(D, self).save()
# d = D()
# d.save()

# print(A.__mro__)
# print(B.__mro__)
# print(C.__mro__)
# print(D.__mro__)

# class Simple(object):
#     pass

# s = Simple()
# print(Simple)
# print(type(Simple))
# print(type(s))
# print(s.__class__)
# print(s.__class__ == type(s))

# class MyList(list):
#     def __sub__(self, other):
#         L = self[:]
#         for x in other:
#             if x in L: L.remove(x)
#         return L

# L = MyList([1, 2, 3, 'spam', 4, 5])
# L = L - ['spam']
# print(L)

# class MyDict(dict):
#     def keys(self):
#         K = list(dict.keys(self))
#         K.sort()
#         return K
# d = MyDict({'one': 1, 'two': 2, 'three': 3})
# print(d.keys())

# class Animal:
#     def cry(self):
#         print('...')

# class Dog(Animal):
#     def cry(self):
#         print('멍멍')

# class Duck(Animal):
#     def cry(self):
#         print('꽥꽥')

# class Fish(Animal):
#     pass

# for each in (Dog(), Duck(), Fish()):
#     each.cry()

# class IntergerAdder:
#     def __init__(self, value=0):
#         self.value = value
#     def __add__(self, value):
#         try:
#             return IntergerAdder(self.value + int(value))
#         except:
#             return self
#     def __repr__(self):
#         return repr(self.value)

# a = IntergerAdder(5)
# print(a + 4, a + 4.5, a + '1324', a + 'abc')

# class Set(list):
#     def union(self, A):
#         res = self[:]
#         for x in A:
#             if x not in res:
#                 res.append(x)
#         return Set(res)
# A = Set([1, 2, 3])
# B = Set([3, 4, 5])
# C = A.union(B)
# print(C)

# class Set:
#     def __init__(self, d=None):
#         self.data = d
#     def union(self, A):
#         res = self.data[:]
#         for x in A:
#             if x not in res:
#                 res.append(x)
#         return Set(res)
#     def __getitem__(self, k):
#         return self.data[k]
#     def __repr__(self):
#         return repr(self.data)

# A = Set([1, 2, 3])
# B = Set([3, 4, 5])
# C = A.union(B)

# class Encapsulation:
#     z = 10
#     __x = 1
# print(Encapsulation.z)
# print(Encapsulation.__x) # type object 'Encapsulation' has no attribute '__x'
# print(dir(Encapsulation)) # _Encapsulation__x
# print(Encapsulation._Encapsulation__x)

# class Delegation:
#     def __init__(self, data):
#         self.stack = data
#     # def __getitem__(self, k):
#     #     return self.stack[k]
#     def get(self):
#         return self.stack
#     def __getattr__(self, name):
#         print('Delegation %s ..' % name, end='')
#         return getattr(self.stack, name)

# a = Delegation([1, 2, 3, 1, 5])
# print(a.pop())
# print(a.count(1))
# # print(a[-1]) # 'Delegation' object does not support indexing
# print(a.get()[-1])

# class ClassForMethod:
#     def set(self, data):
#         self.data = data
# obj = ClassForMethod()
# print(ClassForMethod.set)
# print(obj.set)
# print(obj.set.__class__)

# class A(object) :
#     pass
# class B(object) :
#     pass
# class C(A, B):
#     pass

# print(C.__mro__)

# class A():
#     pass
# class B():
#     pass
# class C(A):
#     pass
# class D(B):
#     pass
# class E(C, D):
#     pass
# print(E.__mro__)

class A(object):
    def save(self):
        print('A save called')
class B(A):
    def save(self):
        print('B save called')
        super().save()
class C(A):
    def save(self):
        print('C save called')
        super().save()
class D(B, C):
    def save(self):
        print('D save called')
        super().save()
d = D()
d.save()
print(D.__mro__)