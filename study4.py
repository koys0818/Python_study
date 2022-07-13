def solution(numbers):
    answer = ''
    m = 0
    for j in range(len(numbers)):
        for i in numbers:
            a = str(i)
            x = int(a[0])
            if a[0] > m:
                m = a[0]

        answer = answer + str(m)
        m = 0
    
    return answer


solution([6, 10, 2])