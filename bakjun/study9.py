#https://www.acmicpc.net/problem/2577

n = []
for i in range(3):
    a = input()
    n.append(int(a))

a = n[0]*n[1]*n[2]
answer={}


for i in str(a):
    if i not in answer:
        answer[i] = 1
    else:
        answer[i] += 1


for i in range(10):
    if str(i) in answer:
        print(answer[str(i)])
    else:
        print(0)