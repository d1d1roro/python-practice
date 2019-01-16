# 1. 다음 코드를 수행했을 때 객체들 간의 관계를 그래프로 그려 보아라.
# s는 1, 2, 4 라는 세 개의 객체를 추가로 가지는가? 메모리의 사용이 얼마나 증가하는가?
# t = (1, 2, 3, 4)
# s = t[:2] + t[3:]
# print(s)

# 2.다음과 같은 코드가 있다. 일요일부터 토요일까지 0-6의 값을 할당받았다.
# print Sun, Mon에 의해서 0과 1이 출력될 것이다. weekday에 입력된 값이 'Sun', 'Mon' 등의 문자열일 때 이것을 정수 0, 1로 변환해서 출력하도록
# 마지막 print 문을 완성하라. (globals()를 이용하라)
# Sun, Mon, Tue, Wed, Thu, Fri, Sat = range(7)
# weekday = input('요일 하나를 입력하세요: ')
# print(int(globals()[weekday]) % 2)

# 3. 다음 코드는 10장 함수에서 설명될 가변 인수에 관한 내용이다.
# 이 코드를 수정하여 다음과 같은 연산이 가능하도록 addall() 함수를 만들어라.
# def vargs(*args):
#     s = 0
#     for n in args:
#         s += n
#     print(s)   

# vargs(1)
# vargs(1, 2, 3, 4)
