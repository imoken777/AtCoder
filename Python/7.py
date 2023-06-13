def game(N,a):
    count =0
    bob_point = 0
    alice_point = 0
    a.sort(reverse=True)
    for i in a:
        if count % 2 == 0:
            alice_point += i
        else:
            bob_point += i
        count += 1
    return alice_point - bob_point

N =int(input())
a =list(map(int,input().split()))
print(game(N,a))