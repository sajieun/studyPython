# 1. 예시 1
pocket = ['paper','card']

if 'money' in pocket :
    print('택시 궈궈')
elif 'card':
    print('걸어가자..')
else:
    print('걸어가라')

# 2. 예시 2
socore = 70

# if socore >= 60:
#     message = 'success'
# else:
#     message = 'failure'

message = 'success' if socore >= 60 else 'failure'

print(message)