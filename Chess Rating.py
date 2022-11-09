# cook your dish here
T=int(input())
for i in range(T):
    (X,Y)=map(int,input().split(" "))
    remRating=Y-X
    if(remRating%8==0):
        print(int(remRating/8))
    else:
        print(int((remRating/8)+1))
