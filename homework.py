# 과제 1 리스트와 튜플 만들기
"""
1. 리스트와 튜플을 만든다. (단, 리스트와 튜플에는 문자열, 숫자, 불리언 (Boolean)값이 들어가야 한다.
2. 리스트의 두번째 값을 출력한다.
3. 튜플 내부에 있는 값을 반복하여 모두 출력한다.
"""

# list_example = ["char", 1991, True] #리스트 생성
# tuple_example = ("char2", 227, False) #튜플 생성

# print (list_example[1])
# tuple_example = ("char2", 227, False) #튜플 생성

# # for로 만들기
# for i in range(0,len(tuple_example)): #인터넷에서 보고한거긴한데 그냥 변수를 넣었는데 되네 = =?
#     print (tuple_example[i])

# # While로 만들기
# i=0
# while i < len(tuple_example):
#     print (tuple_example[i])
#     i+=1

#딕셔너리
"""
딕셔너리로 여러분만의 게임 캐릭터를 만들어보세요!
---------------------------------------------------
- health, power, mana, armor, name을 키 값으로 만드세요.
- Key : value 쌍으로 딕셔너리를 만들어보세요. - 캐릭터에 당신만의 특성을 부여해보세요.
"""

char = {"health":"100", "power":"150", "mana":"200", "armor":"250", "nick":"Jin"}
question = input ("무엇이 궁금하세요? \n 1.health \n 2.power \n 3.mana \n 4.armor \n 5.nick \n 입력해주세요 : ")
print ("당신의 %s는 %s입니다." %(question,char[question]) ) #와 이건 좀 헷갈려따