#https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    day = []
    for p,s in zip(progresses,speeds):
        p = 100 - p
        if p % s == 0:
            day.append(p//s)
        else:
            day.append(p//s + 1)
        
    check = 0
    x = day[0]
    for i in day:
        if i <= x:
            check += 1
        else:
            answer.append(check)
            check = 1
            x = i
    answer.append(check)        
    return answer


    """
    progresses	speeds	return
    [93, 30, 55]	[1, 30, 5]	[2, 1]
    [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
    """



    """
    def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]

    """