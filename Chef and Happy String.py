# cook your dish here
T=int(input())
for i in range(T):
    S=str(input())
    flag=0
    vowels=['a','e','i','o','u']
    for j in range(len(S)-2):
        if(S[j] in vowels):
            if(S[j+1] in vowels):
                if(S[j+2] in vowels):
                    flag=1
                    print("Happy")
                    break
    if(flag==0):
        print("sad")
        
        
