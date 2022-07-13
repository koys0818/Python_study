#https://school.programmers.co.kr/learn/courses/30/lessons/12906


def solution(s):
    a = []
    count = 0
    for i in s:
        count += 1
        if a[-1:] == [i]: continue
        a.append(i)
    return a



"""
arr	answer
[1,1,3,3,0,1,1]	[1,3,0,1]
[4,4,4,3,3]	[4,3]

"""