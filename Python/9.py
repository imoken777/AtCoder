def check_lie(N, Y):
    for i in range(N+1):
        for j in range(N+1-i):
            if 10000*i + 5000*j + 1000*(N-i-j) == Y:
                return [i, j, N-i-j]
    return [-1, -1, -1]

N, Y = map(int,input().split())

print(check_lie(N , Y))