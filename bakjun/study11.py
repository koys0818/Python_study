#https://www.acmicpc.net/problem/1546

a = input()
max = 0
total = 0
scores =[]
for i in range(a):
    score = input()
    scores.append(score)
    if score > max:
        max = score

for i in scores:
    total += i//max*100

print(total/3)