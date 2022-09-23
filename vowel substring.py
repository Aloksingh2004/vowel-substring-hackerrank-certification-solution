def findSubstring(s, k):
    # Write your code here
    n= len(s)
    count=0
    v="aeiou"
    for i in range(k):
        if(s[i] in v):
            count+=1
    cur = s[:k]
    temp=count
    for i in range(1,n-k+1):
        if(s[i-1] in v):
            temp-=1
        if(s[i+k-1] in v):
            temp+=1
        if(count<temp):
            count=temp
            cur=s[i:i+k]
    if(count==0):
        return "Not found!"
    return cur
