# * 집합은 순서가 없고 중복이 허용 되지 않는다. *
# 1. 집합 자료형
s1 = set([1,2,3])
print(s1)

#2. 중복된걸 없애고 하나의 값씩만 가지고 싶을 때
l = [1,2,2,3,4,5,5,34,3,2]
newList = set(l)
print(newList)

#2-1. list로 만들고 싶을 때
q = [1,2,2,3,4,5,5,34,3,2]
newList2 = list(set(q))
print(newList2)

# 3. 교집합
s1 = set([1,3,6,5,7,2,9])
s2 = set([12,4,3,2,5])
print(s1 & s2)
print(s1.intersection(s2))

# 4. 합집합
s1 = set([1,3,6,5,7,2,9])
s2 = set([12,4,3,2,5])
print(s1 | s2)
print(s1.union(s2))

# 5. 합집합
s1 = set([1,3,6,5,7,2,9])
s2 = set([12,4,3,2,5])
print(s1 - s2)
print(s1.difference(s2))

# 6. 한개 혹은 여러개 추가할때
s3 = set([1,3,6,5,7,2,9])
s3.add(19)
print(s3)
s3.update([33,44,55])
print(s3)