# 1. 기본 구조
test_list = ['one','two','three']

for i in test_list:
    print(i)

# 2. 튜플 빼기
a = [(1,2),(3,4),(5,6)]
for (first,last) in a :
    print(first + last)

# 3. 성적
score = [90,25,67,45,80]
number = 0
for mark in score:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 통과" %number)
    else:
        print("%d번 학생은 실패" % number)
print("------------")

# 4. 성적(continue)
score = [90,25,67,45,80]
number = 0
for mark in score:
    number = number + 1
    if mark >= 60: continue
    print("%d번 학생은 통과" %number)

# 5. range
sum = 0

for i in range(1,10):
    sum = sum + i
print(sum)

# 6. 구구단(range)
x = 2
y = 1
for x in range(2,10):
    for y in range(1,10):
        print(x, "*", y, '=',  x* y, end = '\t')
        if(y == 9):
            print() # print()로 한칸 띄우기

# 7. 리스트 내포(List comprehension)

result = [num * 3 for num in a if num % 2 == 0]

# result = []
# for num in a :
#     if num % 2 == 0:
#         result.append(num*3)

print(result)
