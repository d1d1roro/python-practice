# 1. L = [1, 2, 3, 4, 5] 일 때, 다음 두 개의 코드가 어떤 결과를 내겠는가?
# L = [1, 2, 3, 4, 5]
# L[1:3] = [100]
# print(L)
# L[1:3] = 100 # 값 변경 시, 오류: 배열이어야함

# 2. 다음 두 개의 치환문이 수행하는 절차를 설명하라. 두 번째 문에 의해서 a의 레퍼런스가 변경되었는가?
# a = [1, 2, 3]
# a[:] = [4, 5, 6]

# 값을 변경했기 때문에 레퍼런스는 동일
# a = [4, 5, 6] # 이 경우, 객체가 변경되었기에 변경됨

# 3. 다음 문자열 S에 대해서 다음을 풀어라.
# S = 'Sometimes I feel like a motherless child'

# 가) 단어의 순서가 바뀐 문자열을 만들어라. ('child motherless a like feel I Sometimes')
# srr = S.split()
# srr.reverse()
# print(srr)

# 나) 위 문자열의 앞뒤 순서를 완전히 바꾼 문자열을 만들어라.
# one = []
# for s in srr:
#     tmp = list(s)
#     tmp.reverse()
#     one.append("".join(tmp))
# print(" ".join(one))

# 다) 문자열 메서드 split 과 join을 이용하여 위 문자열에서 공백을 모두 없앤 문자열을 만들어라.
# print("".join(one))

# 4. 다음 각 물음에 답하시오.
# a = [1, 2, 3]
# b = a * 3
# c = [a] * 3

# 가) b, c 의 차이점
# b: 1차원 배열, c: 2차원 배열

# 나) 다음 코드를 수행한 후에 b와 c는 어떻게 변화하겠는가?
# a[0] = 0
# b: 값 변경X, c: 값 변경O

# 다) 그렇게 변화한 이유를 설명하라.
# b는 값을 새로 생성, c는 참조값의 복사

# 라) 코드 >>> c = [a[:]] * 3 은 위의 c와 어떻게 다른가?
# 값을 새로 생성, a 값 변경에 따른 영향 없음

# 마) 다음 코드는 또 어떻게 다른가?
# ~~~
# c = [a[:], a[:], a[:]]
# ~~~
# 값을 새로 생성, a 값 변경에 따른 영향 없음

# 5. 다음 리스트 L을 5로 나눈 나머지를 기준으로 정렬하라.
# L = list(range(10))
# print(L)
# L.sort(key=lambda x: x%5)
# print(L)

# 6. 다음 각 물음에 답하시오
# a = [1]
# b = [2]
# a.append(b)
# b.append(a)
# 가) 위 코드의 자료 구조를 그림으로 그려 보아라.
# 나) 값을 출력해 보라. 어떤 결과가 나오는가?
# [1, [2, [...]]] [2, [1, [...]]]
# 다) 객체 a의 레퍼런스 카운트 값은 얼마인가?
# import sys
# print(sys.getrefcount(a)) # 3
# 라) 객체 b를 지웠다. 객체 a의 레퍼런스 카운트 값은?
# del b
# print(sys.getrefcount(a)) # 3
# print(a)
# del a

# ----------------------------------------------------------------------------------
# 마) 객체 b를 삭제한 구조를 그림으로 그려라. a 값을 출력해보라. 구조가 맞는가?
# 바) a를 삭제하였다. 무슨 문제가 발생하겠는가? 설명하라.
# ----------------------------------------------------------------------------------

# 7. 문자열의 리스트가 있다. 리스트의 sort 메서드를 이용하여 이들을 정렬하라. 단, 대/소문자는 구별하지 않는다.
# sl = ['Spam', 'egg', 'Ham']
# sl.sort(key=str.lower)
# print(sl)

# 8. 다음 문자열을 ':' 기준으로 분리하여 리스트로 만들고, 각 문자열의 좌우의 공백을 제거하라. 즉, 다음 문자열 s에서 L을 만들어라. (for문 이용)
# s = ' first item  : second item   : third item   '
# L = s.split(":")
# for i, v in enumerate(L):
#     L[i] = v.strip()
# print(L)

# 9. 문제 8번을 리스트 내장을 이용하여 한 줄로 해결하라.
# L = [v.strip() for v in s.split(":")]
# print(L)

# 10. 현재 디렉토리에 있는 .py 파일들 중에서 크기가 500바이트를 넘는 것들만 파일 목록을 출력하라. (힌트: glob와 os.path 모듈을 이용하라.)
# import glob
# import os
# flist = glob.glob('*.py')
# for fname in flist:
#     if (os.path.getsize(fname) > 500):
#         print(fname)

# 11. 현재 디렉토리에 있는 모든 파일들 중에서 최근 24시간 이내에 변경된 파일들의 목록을 출력하라.

# 12. 롱 옵션의 처리 방법을 공부하고 그 예를 만들어 보라.(다음 예를 참조)
# 롱 옵션은 getopt.getopt의 세 번째 인수로 지정된다. 세번째 인수는 리스트이며 옵션의 인수를 필요로 한다면 condition=와 같이 옵션 이름 뒤에 =를 추가한다.
# 아래의 예에서 args는 명령행 인수를 인공적으로 만든 리스트이다. 앞서 설명한 바와 같이 실제로는 args = sys.argv[1:] 와 같이 할 수 있다.

# 연습문제
# 1. 명령행에 URL 주소를 입력하면 그 URL 의 HTML 문서를 화면에 출력하는 프로그램을 작성하라.
# (url에서 HTML 문서를 가져오는 것은 다음과 같은 코드를 이용한다.)
import urllib.request
import sys
import getopt

def getpage(url):
    f = urllib.request.urlopen(url)
    return f.read()

# text = getpage(sys.argv[1])
# print(text)

# 가) 위 코드를 수정하여 명령행에서 인수가 입력되지 않았을 때 사용법을 출력하도록 에러 처리 루틴을 추가하라.
# 나) 명령행 인수에 두 개 이상의 인수를 입력받아서 그 문서들을 출력하도록 코드를 수정하라.
# 다) 잘못된 url이 입력되면 그 url 출력은 건너뛰고, 나중에 잘못된 url 목록을 출력하도록 수정하라.