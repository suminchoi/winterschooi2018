import random

ans1="자!해보세요"
ans2="됐네요, 이사람아"
ans3="뭐라고?다시 생각해보세요"
ans4="모르니 두려운 것입니다"
ans5="과연..."
ans6="그것은 틀림"
ans7="그것은 정답"
ans8="성공할 운명"



print("random8ball에 오신 여러분 환영합니다")

question = input("조언을 구하고 싶은 질문을 입력하고 엔터 눌러라.\n")

print("고민중...\n"*4)

choice = random.randint(1,8)
if choice == 1:
    answer=ans1
elif choice == 2:
    answer = ans2
elif choice == 3:
    answer = ans3
elif choice == 4:
    answer = ans4
elif choice == 5:
    answer = ans5
elif choice == 6:
    answer = ans6
elif choice == 7:
    answer = ans7
elif choice == 8:
    answer = ans8

print(answer)

input("\n\n마치려면 엔터키를 누르세염")
