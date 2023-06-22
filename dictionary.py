# *키가 똑같으면 안 된다 but value는 똑같아도 된다.*
# dic = {'name':'sajieun', 'name':'24'} -> 안됨
# dic = {'name':'sajieun', 'age':'sajieun'} -> 가능

# 1. 예시
dic = {'name':'sajieun', 'age':'24'}
print(dic['name'])

# 2. 딕셔너리 쌍 추가하기
a = {'1':'jieun'}
a['age'] = '24'
print(a)

# 3. 딕셔너리 요소 삭제하기
b = {1:'jieun'}
b['age'] = '24'

del b['age'] # 키값으로 지워야한다.
print(b)

# 4. Key 또는 Value 또는 새로운 배열안에 튜플 형태로 값 추출
c = {1:'blue',2:'red',3:'yellow'}
print(c.keys())
print(c.values())
print(c.items())

# 5. Key 배열을 뽑고 싶을 때
d = {1:'blue',2:'red',3:'yellow'}
for i in d.keys():
    print(i)

# 6. Key , Value 배열을 뽑고 싶을 때
e = {1:'blue',2:'red',3:'yellow'}
for i,v in e.items():
    print("key: " + str(i))
    print("value: " + str(v))

# 7. 내용 모두 지우기
f = {1:'blue',2:'red',3:'yellow'}
f.clear()
print(f)

# 8. 값이 없는걸 대체해서 값 넣어줄 때 (4라는 키값이 없을때 없음을 반환해라)
g = {1:'blue',2:'red',3:'yellow'}
print(g.get(4,'없음'))