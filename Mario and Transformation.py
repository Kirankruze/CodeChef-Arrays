T=int(input())
for i in range(T):
    X=int(input())
    now='normal'
    while(X>0):
        if (now=='small'):
            now='normal'
        elif (now=='normal'):
            now='huge'
        elif (now=='huge'):
            now='small'
        X-=1
    print(now)
