# cook your dish here
T=int(input())
for i in range(T):
    (A,B)=map(int,input().split(" "))
    S=str(A+B)
    dictn={"0":6,"1":2,"2":5,"3":5,"4":4,"5":5,"6":6,"7":3,"8":7,"9":6}
    sum=0
    
    for j in S:
        for k in dictn:
            if (j==k):
                sum+=dictn.get(k)
    print(sum)
                
        
