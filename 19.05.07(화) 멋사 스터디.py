# 멋쟁이 사자처럼 [7주차 스터디팀 과제] 팀 명단 만들기
# 작성자 : Joo

student_Max = int(input("입력 받을 학생의 최대 수 : "))
mySortList = []  # 빈 리스트 생성

for i in range(student_Max):
    mySortList.append(input("학번과 이름을 입력해주세요 : "))

mySortList.sort(reverse=True)

for i in range(student_Max):
    print(mySortList[i])










