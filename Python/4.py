def a(N,A):
    count = 0
    while all(a % 2 == 0 for a in A):
        A = [a // 2 for a in A]
        count += 1
    return count

N = int(input())
A = list(map(int,input().split()))
print(a(N,A))

