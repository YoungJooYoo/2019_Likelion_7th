# 7주차 개인과제 파이썬으로
# 구구단 출력 프로그램과 숫자를 입력 받아 구구단 출력하기
# 작성일 2019.05.07(화)
# 작성자 : Joo

while True:
 result = int(input("구구단에 사용할 숫자를 입력하세요 : \n"))
 for i in range(1,10):
  print(result, "X", i, "=", result*i)