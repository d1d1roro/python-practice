# 1. infix 표기를 postfix 표기로 변경하는 코드를 생성자를 이용하여 작성하라. 수식에는 다음과 같은 연산자를 사용할 수 있다.
# ()
# *, / (우선 순위 높음)
# +, - (낮음)
# tokenizer() 함수는 키보드 혹은 파일 입력으로부터 읽어 들인 라인을 토큰 단위로 분리한다. 더이상 입력을 읽을 수 없으면 중단한다.
# 하나의 토큰은 (토큰 종류, 토큰 문자열) 형식을 가진다. 토큰의 종류는 다음과 같다. (적당한 정수 값으로 처리할 것)
# NAME - 변수명
# NUMBER - 정수
# OP - 연산자(+, -, *, /)
# PAREN - 괄호 ()
# NL - newline 수식의 끝을 알림
# ERRORTOKEN - 기타
# 예를 들어 다음과 같은 입.출력 조건을 만족한다.
# 입력 라인: 3 + 5
# 출력 토큰:
# (NUMBER, '3')
# (NUMBER, '5')
# infix2postfix() 함수는 tokenizer()의 출력을 입력으로 받고 토큰을 출력한다. 처리하는 알고리즘은
# 가) 오퍼랜드인 경우, 그냥 토큰 출력한다.
# 나) 연산자인 경우, 이미 스택에 저장된 연산자의 우선 순위가 높거나 같은 경우 저장된 연산자 출력 연산자를 저장한다.
# 다) 여는 괄호는 스택에 그냥 저장한다.
# 라) 닫는 괄호는 여는 괄호가 나올 때까지 스택에서 출력한다.
# 마) NL인 경우는 스택 안의 모든 연산자를 출력한다.
# 다음과 같은 테스트 코드를 만족하도록 하라.
# def test_in2post():
#     for toktype, token in infix2postfix(raw_input):
#         if toktype != NL:
#             print(token, end=' ')
#         else:
#             print()

import tokenize
from io import StringIO
f = StringIO('3 + 5 + (6 + 7)')
for el in tokenize.generate_tokens(f.readline):
    print(el.type, el.string)