def a(N,A,B):
    total = 0
    for i in range(1,N+1):
        subtotal = sum(int(d) for d in str(i))
        if A <= subtotal <= B:
            total += i
    return total


N,A,B = map(int,input().split())
print(a(N,A,B))