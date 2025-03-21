import random

random_num = random.randint(1, 6)

while True:
    try:
        num = int(input("숫자를 입력하세요(1~6): "))
        
        if num < 1 or num > 6:
            print("입력 가능한 숫자는 1부터 6까지 입니다.")
        elif num == random_num:
            print("정답입니다!")
            break
        elif num > random_num:
            print("입력하신 숫자는 정답보다 큽니다.")
        elif num < random_num:
            print("입력하신 숫자는 정답보다 작습니다.")
        else:
            print("잘못된 값을 입력하였습니다.")
    
    except ValueError:
        print("숫자를 입력해주세요!")
