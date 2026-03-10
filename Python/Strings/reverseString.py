s = ["h","e","l","l","o"]
i=0
while(i<(len(s)/2)):
    intermediate = s[len(s)-1-i]
    s[len(s)-1-i] = s[i]
    s[i] = intermediate 
    i+=1
print(s)