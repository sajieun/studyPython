# 1. 예시 1
a = 0
while a < 10 :
    a = a+1
    print("나무 %d  찍기" %a)
    if a == 10:
        print('나무 넘어가유')

# 2. 예시 2 (break문)
coffee = 10
money = 300
while money:
    print("커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피의 양은 %d개 입니다." %coffee)
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매 중지")
        break

# 3. 예시 3 (continue문)
b = 0
while b < 10:
    b = b + 1
    if b % 2 == 0:
        continue
    print(b)



