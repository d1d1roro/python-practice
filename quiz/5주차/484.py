# 1. 예외 처리를 이용하여 변수가 정의되지 않은 경우를 처리하라. 예를 들면 price = selected 라는 문에서
# 만일 selected가 앞서 정의되지 않았다면 NameError를 일으킨다. selected가 정의되지 않은 경우에 price 의 값을 0으로 설정하여라.
# try:
#     price = selected
# except NameError as e:
#     print(e)
#     price = 0
    
# 2. 사용자 예외를 문자열로 정의하고 예외가 발생했을 때 처리하는 예를 보여라.
# class MyException(Exception):
#     pass
# try:
#     raise MyException()
# except MyException:
#     print('done')

# 4. traceback 모듈을 이용하여 예외 출력 정보를 화면에서 파일로 저장하여라. print_exc 함수를 사용하여라.
import  traceback
try:
    price = selected
except NameError:
    traceback.print_exc()
    print('done')
    print = 0