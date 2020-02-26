"""
과제 3 계산기 만들기
-----------------------------
1. 비어있는 값을 모두 채 워오기
2. 파일 이름을 calculator.py로 지정할 것.
-----------------------------
"""
"""
category = {1:"add", 2:"subtraction", 3:"multiplication", 4:"division", 5:"Exit"}

# 정상적인 루트
def calculator():
    while True:
        operation = int(input("Please select operation \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Exit \n\n Select Operations from 1, 2, 3, 4, 5 : "))
        print("You chose %s cal" % category[operation])
        if operation == 1: #사용자 입력이 1인경우
            firstNum = float(input("첫번째 숫자를 입력해주세요 : ")) #첫번째 숫자 입력
            secondNum = float(input("두번째 숫자를 입력해주세요 : ")) #두번째 숫자 입력
            result = firstNum + secondNum
            print("The result is %f" % result)
        
        elif operation == 2:
            firstNum = float(input("첫번째 숫자를 입력해주세요 : ")) #첫번째 숫자 입력
            secondNum = float(input("두번째 숫자를 입력해주세요 : ")) #두번째 숫자 입력
            result = firstNum - secondNum
            print("The result is %f" % result)

        elif operation == 3:
            firstNum = float(input("첫번째 숫자를 입력해주세요 : ")) #첫번째 숫자 입력
            secondNum = float(input("두번째 숫자를 입력해주세요 : ")) #두번째 숫자 입력
            result = firstNum * secondNum
            print("The result is %f" % result)

        elif operation == 4:
            firstNum = float(input("첫번째 숫자를 입력해주세요 : ")) #첫번째 숫자 입력
            secondNum = float(input("두번째 숫자를 입력해주세요 : ")) #두번째 숫자 입력
            result = firstNum / secondNum
            print("The result is %f" % result)

        elif operation == 5:
            print("Thank you")
            break
        else:
            print("You typed wrong number! Please choose the number from 1 to 4.")
"""

# 코드를 줄여봅시다 :)
"""
어차피 사용자한테 변수를 받을거면 operation 도 받아서 계산을 때려봅시다 :)
무한반복이 좀 거시기하니까 계산할때 도망갈 구녕도 남겨놓읍시다.
"""

operator = {"+":"더하기", "-":"빼기", "*":"곱하기", "/":"나누기"}

def exit_ask():
    exit_input = input("끝내시겠습니까?(Y/N) :")
    if exit_input == "Y":
        print("종료합니다.")
        return(True)
    elif exit_input == "N":
        print("계산을 계속합니다.")
        return(False)
    else :
        print("어쩌자는거지...")
        return(False)

def calculator():
    while True:
        operation = input("다음중 사용할 수식을 입력해주세요 \n +, -, *, / :")
        print ("당신이 선택한 수식은 %s 입니다!" % operation)
        firstNum = float(input("첫번째 숫자를 입력해주세요 :"))
        secondNum = float(input("두번째 숫자를 입력해주세요 :"))
        
        if operation == "+":
            result = firstNum + secondNum
            print ("계산 결과 : %f" % result)
            if exit_ask() == True:
                break
        elif operation == "-":
            result = firstNum - secondNum
            print ("계산 결과 : %f" % result)
            if exit_ask() == True:
                break
        elif operation == "*":
            result = firstNum * secondNum
            print ("계산 결과 : %f" % result)
            if exit_ask() == True:
                break
        elif operation == "/":
            result = firstNum / secondNum
            print ("계산 결과 : %f" % result)
            if exit_ask() == True:
                break
        else :
            print ("입력 똑바로 하십시오.")



calculator()