T=int(input())
for i in range(T):
    n=int(input())
    li=list(map(int,input().split(" ")))
    c=0
    for j in li:
        if(j>c):
            c=j
    print(c)
    
