# e = 1
# while e <= 1000:
#     e = e * 3
#     print(e)

result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1

print(result)