#https://www.acmicpc.net/problem/3052

answer = {}
count = 0
for i in range(10):
    a = input()
    if int(a)%42 not in answer:
        answer[int(a)%42] = 1
        count += 1

print(count)