strs = ["cir","car"]
# strs.sort(key = len)
char_index = 0
output = ""
str_index = 2

if(len(strs)==1):
    print(strs[0])

for i in range(len(strs[0])):
    if(i<len(strs[1]) and strs[0][i] == strs[1][i]):
        output = output + strs[0][i]
    else:
        break

print("initial output == ",output)

while(str_index<len(strs)):
    char_index = 0
    while(char_index<len(output) and char_index<(len(strs[str_index])) and output[char_index] == strs[str_index][char_index]):
        char_index+=1
        continue
    output = output[:char_index]
    str_index+=1
print(output)
    

