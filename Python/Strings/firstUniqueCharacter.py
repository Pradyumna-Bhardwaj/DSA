s = "cccaabadb"
my_dict = {}
for i in s:
    if(i in my_dict):
        my_dict[i] = my_dict[i]+1
    else:
        my_dict[i] = 1
index = 0

for i in s:
    if(my_dict[i]==1):
        break
    index+=1
    if(index == len(s)):
        index = -1

print(index)