# class Simple:
#     pass

# s1 = Simple()
# s2 = Simple()
# s1.stack = []
# s1.stack.append(1)
# s1.stack.append(2)
# s1.stack.append(3)
# print(s1.stack, s1.stack.pop(), s1.stack.pop(), s1.stack)
# print(s2.stack)

# class MyClass:
#     def set(self, v):
#         self.value = v
#     def put(self):
#         print(self.value)
#     def incr(self):
#         self.set(self.value + 1)

# c = MyClass()
# c.set('egg')
# c.put()

# class D:
#     def spam(x, y):
#         print('static method', x, y)
#     spam = staticmethod(spam)

# D.spam(1, 2)
# d = D()
# d.spam(1, 2)

# 클래스메서드란? 왜 필요할까.
# 모든 인스턴스가 공유하는 클래스 변수와 같은 데이터를 생성, 변경 또는 참조하기 위한 메소드

# class C:
#     def spam(cls, y):
#         print(cls, y)
#     spam = classmethod(spam)
# print(C)
# C.spam(5)
# c = C()
# c.spam(5)

# 상속 받은 경우
# class D(C):
#     pass
# D.spam(3)
# d = D()
# d.spam(3)

# def accepts(*types):
#     def check_accepts(f):
#         assert len(types) == f.__code__.co_argcount
    
#         def new_f(*args, **kwds):
#             for (a, t) in zip(args, types):
#                 assert isinstance(a, t), "arg %r does not match %s" % (a, t)
#             return f(*args, **kwds)
#         new_f.__name__ = f.__name__

#         return new_f
#     return check_accepts

# @accepts(int, int)
# def f(a, b):
#     return a + b
# print(f(1, 2.3)) # arg 2.3 does not match <class 'int'>

# class Var:
#     c_mem = 100
#     def f(self):
#         self.i_mem = 200
#     def g(self):
#         print(self.i_mem)
#         print(self.c_mem)
# v1 = Var()
# v1.f()
# v2 = Var()
# print(v1.c_mem, v2.c_mem)
# v1.c_mem = 50
# print(v1.c_mem, v2.c_mem, Var.c_mem)

# class Const:
#     def initialize(self):
#         self.hand = 2
#         self.foot = 2
#         self.eye = 2
#     def print_info(self):
#         print('hands=%s foot=%s eyes=%s' % (self.hand, self.foot, self.eye))
# c = Const()
# c.initialize()
# c.print_info()

# from time import time, ctime, sleep

# class Life:
#     def __init__(self):
#         self.birth = ctime()
#         print('Birthday', self.birth)
#     def __del__(self):
#         print('Deathday', ctime())

# def test():
#     mylist = Life()
#     print('sleeping for 3 sec')
#     sleep(3)

# test()

# class MyString:
#     def __init__(self, str):
#         self.str = str
#     def __truediv__(self, sep):
#         return self.str.split(sep)
#     def __neg__(self):
#         t = list(self.str)
#         t.reverse()
#         return ''.join(t)

# m = MyString("abcdef")
# print(-m)

# print(dir(int))

# class Square:
#     def __init__(self, end):
#         self.end = end
#     def __len__(self):
#         return self.end
#     def __getitem__(self, k):
#         if k < 0 or self.end <= k: raise IndexError
#         return k*k
# s1 = Square(10)
# print(len(s1), s1[1])
# print(s1[4])
# print(s1[20])
# for x in s1:
#     print(x, end=' ')

# s = slice(1, 10, 2)
# print(s, type(s), dir(s), s.start, s.stop, s.step)

# print(slice(10))

# class Square:
#     def __init__(self, end):
#         self.end = end
#     def __len__(self):
#         return self.end
#     def __getitem__(self, k):
#         if isinstance(k, int):
#             if k < 0 or self.end <= k: raise IndexError
#             return k * k
#         elif isinstance(k, slice):
#             start = k.start or 0
#             if k.stop or self.end > self.end: stop = self.end
#             else: stop = k.stop or self.end
#             step = k.step or 1
#             return list(map(self.__getitem__, range(start, stop, step)))
# s= Square(10)
# print(s[4])
# print(s[1:5])
# print(s[1:10:2])
# print(s[:])

# class MyDict:
#     def __init__(self, d=None):
#         if d == None: d= {}
#         self.d = d
#     def __getitem__(self, k):
#         return self.d[k]
#     def __setitem__(self, k, v):
#         self.d[k] = v + "!"
#     def __len__(self):
#         return len(self.d)
#     def keys(self):
#         return self.d.keys()
#     def values(self):
#         return self.d.values()
#     def items(self):
#         return self.d.items()
# m = MyDict()
# m['day'] = 'light'
# m['night'] = 'darkness'
# print(m, m['day'], m['night'], len(m))
# m = MyDict({'one': 1, 'two': 2, 'three': 3})
# print(m.keys(), m.values(), m.items())

# class StringRepr:
#     def __repr__(self):
#         return 'repr called'
#     def __str__(self):
#         return 'str called'
# s = StringRepr()
# print(s, repr(s))

# class Hash1:
#     def __hash__(self):
#         return id(self)
# h1 = Hash1()
# d = {}
# d[h1] = 1
# print(d[h1])
# print(list(d.keys()))

# class Truth:
#     def __init__(self, num):
#         self.num = num
#     def __bool__(self):
#         return self.num == 10
# t = Truth(3)
# print(bool(t))
# t1 = Truth(10)
# print(bool(t1))

# class Attr:
#     def __init__(self):
#         self.mem1 = 1
#     def method1(self):
#         print('method1')
#     def __getattr__(self, name):
#         if name == 'mem3': return 3
#         raise AttributeError
#     def __setattr__(self, name, value):
#         print('__setattr__(%s)=%s called' % (name, value))
#         self.__dict__[name] = value
#     def __delattr__(self, name):
#         print('__delattr__(%s) called' % name)
#         del self.__dict__[name]
# a = Attr()
# print(a.mem1)
# a.method1()
# print(a.mem3)
# a.mem5 = 5
# del a.mem5

# class New(object):
#     def __getattribute__(self, x):
#         print('__getattribute__ called', x)
#         return object.__getattribute__(self, x)
# n = New()
# n.x = 1
# print(n.y)

# 상위스코프에서 계속 찾는가보다.
# __getattribute__ called y
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __class__
# __getattribute__ called __iter__

# class Accumulator:
#     def __init__(self):
#         self.sum = 0
#     def __call__(self, *args):
#         self.sum += sum(args)
#         return self.sum
# acc = Accumulator()
# print(acc(1, 2, 3, 4, 5))
# print(acc(6))
# print(acc(7, 8, 9))
# print(acc.sum)

# def check(func):
#     if callable(func):
#         print('callable')
#     else:
#         print('not callable')
# class B:
#     def func(self, v):
#         return v
# class A:
#     def __call__(self, v):
#         return v
# a = A()
# b = B()
# check(a)
# check(b)

# class D(object):
#     def __init__(self):
#         self.__degree = 0
#     def get_degree(self):
#         return self.__degree
#     def set_degree(self, d):
#         self.__degree = d % 360
#     degree = property(get_degree, set_degree)
# d = D()
# d.degree = 10
# print(d.degree)
# d.degree = 370
# print(d.degree)

# class Person:
#     def __init__(self, name, phone=None):
#         self.name = name
#         self.phone = phone
#     def display(self):
#         return '<Person %s %s' % (self.name, self.phone)
# class Employee(Person):
#     def __init__(self, name, phone, position, salary):
#         Person.__init__(self, name, phone)
#         self.position = position
#         self.salary = salary
# m1 = Employee('손창희', 5564, '대리', 200)
# m2 = Employee('김기동', 8546, '과장', 300)
# print(m1.name, m1.position)
# print(m2.name, m2.position)

# class Person:
#     def __init__(self, name, phone=None):
#         self.name = name
#         self.phone = phone
#     def __repr__(self):
#         return '<Person %s %s>' % (self.name, self.phone)

# class Employee(Person):
#     def __init__(self, name, phone, position, salary):
#         Person.__init__(self, name, phone)
#         self.position = position
#         self.salary = salary
#     def __repr__(self):
#         s = Person.__repr__(self)
#         return s + '<Employee %s %s>' % (self.position, self.salary)

# p1 = Person('gslee', 5284)
# m1 = Employee('kslee', 5224, 'President', 500)
# print(p1, m1)

# class Person:
#     def __init__(self, name, phone=None):
#         self.name = name
#         self.phone = phone
#     def __repr__(self):
#         return "name=%s tel=%s" % (self.name, self.phone)

# class Job:
#     def __init__(self, position, salary):
#         self.position = position
#         self.salary = salary
#     def __repr__(self):
#         return "position=%s salary=%s" % (self.position, self.salary)

# class Employee(Person, Job):
#     def __init__(self, name, phone, position, salary):
#         Person.__init__(self, name, phone)
#         Job.__init__(self, position, salary)
#     def raisesalary(self, rate):
#         self.salary = self.salary * rate
#     def __repr__(self):
#         return Person.__repr__(self) + ' ' + Job.__repr__(self)

# e = Employee('gslee', 5244, 'prof', 300)
# e.raisesalary(1.5)
# print(e)

# class A:
#     def save(self):
#         print ('A save called')

# class B(A):
#     pass

# class C(A):
#     def save(self):
#         print('C save called')

# class D(B, C):
#     pass

# d = D()
# d.save()
# print(D.mro())

# class Base:
#     def f(self):
#         self.g()
#     def g(self):
#         print('Base')

# class Derived(Base):
#     def g(self):
#         print('Derived')

# b = Base()
# b.f()

# a = Derived()
# a.f()

# 8-10. 실제적인 클래스 상속의 예
# 1) list, dict 서브 클래스 만들기

# class Stack(list):
#     push = list.append
# s = Stack()
# s.push(4)
# s.push(5)
# s = Stack([1,2,3])
# s.push(4)
# s.push(5)
# print(s, s.pop()) # 뭐지. 순서가 어떻게 되는 거지. 메서드부터 실행하나? 거꾸로 실행한다고 하기도 아니고..

# class Queue(list):
#     enqueue = list.append
#     def dequeue(self):
#         return self.pop(0)

# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# print(q, q.dequeue())

# class MyDict(dict):
#     def keys(self):
#         L = list(dict.keys(self))
#         L.sort()
#         return L

# d = MyDict({'one': 1, 'two': 2, 'three': 3})
# print(d.keys())

# class A:
#     pass
# class B:
#     def f(self):
#         pass
# class C(B):
#     pass
# def check(obj):
#     print(obj, '->', end=' ') 
#     if issubclass(obj, A): print('A', end=' ')
#     if issubclass(obj, B): print('B', end=' ')
#     if issubclass(obj, C): print('C', end=' ')
#     print()
# check(A)
# check(B)
# check(C)

# def ListSuperClasses(classInstance, clist=None):
#     if not clist: clist = []
#     for klass in classInstance.__bases__:
#         clist.append(klass.__name__)
#         ListSuperClasses(klass, clist)
#     return clist

# class Super1:
#     m1 = 1
#     def a(self):
#         pass
#     def b(self):
#         pass

# class Super2(Super1):
#     m2 = 2
#     def c(self):
#         pass
#     def d(self): pass

# class Super3(Super1):
#     m2 = 2
#     def c(self):
#         pass
#     def d(self):
#         pass

# class Sub(Super2, Super3):
#     m3 = 3
#     m4 = 4
#     def x(self): pass
#     def y(self): pass

# print(ListSuperClasses(Sub))
# s = Sub()
# print(ListSuperClasses(s.__class__))

# class Simple:
#     member = 1
#     def method(self): self.method2 = 'HERE'
# s = Simple()
# print(s.__class__.__name__)
# print(Simple.__dict__)

# s = Simple()
# print(s.__dict__)
# s.method()
# print(s.__dict__)
# s.attr = 'member + method'
# s.num1 = 10
# print(s.__dict__)
# print(dir(s))

