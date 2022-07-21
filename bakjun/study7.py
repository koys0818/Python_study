#https://www.acmicpc.net/problem/1065


n = int(input())
total = 0
for i in range(n+1):
    if i < 100:
        total += 1
    else:
        if (i//100 - i//10%10) == (i//10%10 - i%10):
            total += 1

print(total-1)