# 6. Counter 클래스를 설계하라.
# 가) 이 클래스의 생성자는 정수의 초기 값을 받는다. 만일 인수가 주어지지 않으면 초기 값 0을 가진다.
# 나) 멤버 step은 카운터 값을 증가시키는 증분이다. 초기 값은 1이다.
# 다) 메서드 incr를 호출하면 현재의 카운터에서 step만큼 증가한다.
# 라) 카운터 값을 문자열로 변환하는 __str__, __repr__ 메서드를 추가하여라.
# 마) __call__ 메서드를 추가하여 인스턴스 객체를 직접 호출할 수 있도록 하라.
# class Counter:
#     def __init__(self, init=0):
#         self.init = init
#     def incr(self, step=1):
#         self.init += step
#     def __str__(self):
#         return 'value is %s' % self.init
#     def __repr__(self):
#         return 'value is %s' % self.init
#     def __call__(self, step=1):
#         self.incr(step)
#         return self.init
# c = Counter(50)
# print(c(7))
# c.incr(10)
# print(c)
    
# 7. 집합 클래스 Set을 정의하라. &로 두 집합의 교집합을, |로 두 집합의 합집합을, -로 두 집합의 차집합을 연산하라.
# 초기 멤버는 __init__ 메서드를 통해서 받는다. __init__ 메서드는 다른 Set 인스턴스나 리스트, 튜플, 문자열과 같은 시퀀스 자료형을 초기 집합으로 받을 수도 있다.
# 예를 들어 Set([1,2,3])와 같이 호출하면 초기 집합 원소로 1,2,3이 할당된다. __len__, __getitem__, __setitem__, delitem__, __contains__메서드도 함께 구현하라.
# 또한 진리 값 테스트를 위한 __nonzero__ 메서드도 추가하여라. 이 메서드는 집합에 자료가 없으면 0, 있으면 1을 리턴한다.
# class Set:
#     def __init__(self, target):
#         self.target = target[:]
#     def union(self, comp):
#         res = self[:]
#         for n in comp:
#             if n not in res:
#                 res.append(n)
#         return Set(res)
#     def __len__(self):
#         return len(self.target)
#     def __getitem__(self, i):
#         return self.target[i]
#     def __setitem__(self, i, v):
#         self.target[i] = v
#     def __delitem__(self, i):
#         self.target.remove(i)
#     def __contains__(self, v):
#         return True if v in self.target else False
#     def __nonzero__(self):
#         return 1 if len(self.target) > 0 else 0
#     def __repr__(self):
#         return repr(self.target)

# A = Set([1, 2, 3])
# B = Set([3, 4, 5])
# print(A.union(B))

# 8. 응.