def pay_count(A,B,C,X):
    count = 0
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                total = (500*a) + (100*b) + (50*c)
                if total == X:
                    count += 1
    return count


A = int(input())
B = int(input())
C = int(input())
X = int(input())
print(pay_count(A,B,C,X))