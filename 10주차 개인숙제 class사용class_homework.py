class UserInformation:

    userName = 0
    userAge = 0
    userMajor = 0

    def input_info(self):
        # 객체 내부 변수에 직접 입력을 받음
        UserInformation.userName = input("이름을 입력하세요 : ")
        UserInformation.userAge = input("나이를 입력하세요 : ")
        UserInformation.userMajor = input("전공을 입력하세요 : ")

    def output_info(self, userName, userAge, userMajor):
        print('------------------')
        print('이름은 : '+userName)
        print('나이는 : '+userAge)
        print('전공은 : '+userMajor)





# 객체생성
info = UserInformation()

# 생성된 객체 입력함수 실행
info.input_info()
# 생성된 객체 출력함수 실행, 객체 내부의 변수를 매개변수로 출력함수에 전달 후 실행
info.output_info(info.userName, info.userAge, info.userMajor)


