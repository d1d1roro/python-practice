# 1. 텍스트 파일을 읽어서 각 라인에 있는 공백으로 분리된 단어의 수를 세는 프로그램을 작성하라.
# 단, 라인의 첫 문자가 # 으로 시작하면 주석문으로 처리하지 않고 넘어간다.
# word = []
# for l in open('t.txt'):
#     if l.startswith("#"):
#         continue
#     word.extend(l.split())
# print(len(word))        

# 2. 다음 코드로 출력될 내용을 파일 number.txt에 출력하시오. (write 혹은 writelines 이용)
# f = open('number.txt', 'w')
# for k in range(10):
#     f.write(str(k) + ", ")
# f.close()
# f = open('number.txt')
# print(f.read())

# 3. 파일 s.txt에 있는 라인들을 정렬해서 출력하시오. 파일 s.txt의 내용은 다음과 같다.
# pig ham
# cat dog
# ham bird
# dog pig
# f = open('s.txt')
# lines = f.readlines()
# lineArr = ''.join(lines).split('\n')
# lineArr = ' '.join(lineArr)
# lineArr = lineArr.split()
# print(sorted(lineArr))

# for line in sorted(open('s.txt')):
#     print(line.rstrip())

# 4. 문제 3번의 파일을 두번째 단어를 기준으로 정렬하여라. 결과는 다음과 같아야한다.
# ham bird
# cat dog
# pig ham
# dog pig
# for line in sorted(open('s.txt'), key=lambda x:x.split()[1]):
#     print(line.rstrip())

# 5. 문제 3번의 파일을 읽고 한 줄에 3개의 단어가 오도록 출력하여라. 결과는 다음과 같아야 한다.
# pig ham cat
# dog ham bird
# dog pig
# ws = open('s.txt').read().split()
# for i in range(0, len(ws), 3):
#     print(' '.join(ws[i: i+3]))