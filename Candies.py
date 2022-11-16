# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    li=list(map(int,input().split(" ")))
    flag=0#flag Variable
    j=0
    while(j<2): #to iterate through list
        c=1 #to count occurance
        k=j+1
        while(k<(2*N)): #loop to compare one element with rest of elements
            if(li[j]==li[k]):
                c+=1
            k+=1
        j+=1
        if(c>=3):  #if occurance is >=3 then we cant split distinct arrays
            flag=1
            break
    if(flag==1):
        print("no")
    elif(flag==0):
        print("yes")
            
