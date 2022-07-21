#https://www.acmicpc.net/problem/4673


a = []
for i in range(10000):
    if i < 10:
        a.append(i+i)
    elif i < 100:
        a.append(i + i//10 + i%10)
    elif i <1000:
        a.append(i + i//100 + i//10%10 + i%10)
    elif i < 10000:
        a.append(i + i//1000 + i//100%10 + i//10%10 + i%10)

for i in range(10000):
    if i not in a:
        print(i)
        
