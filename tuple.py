# *list처럼 .replace 등 값을 옮기거나 추가하거나 삭제하는건 안됨*
# 1. t2를 넣는거는 됨
t1 = (1,2,'a','b')
t2 = (3,5)

print(t1 + t2)

# 2. 같은게 세번 출력
t1 = (1,2,'a','b')
a = t1 * 3
print(a)

