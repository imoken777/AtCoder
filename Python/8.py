def mochi(N,d):
    replica = d.copy()
    count = 0
    for i in replica:
        replica.remove(i)
        if i not in d:
            count += 1
    return count

N = int(input())
d = []
count = 0
while count < N:
    d.append(int(input()))
    count += 1

print(mochi(N,d))