# to improve code introduce ana rray of 26 length and add s chars then subtract t chars if all 0 then true

s = "a"
t = "ab"
output = True
if(len(s)==len(t)):
    s_dict = {}
    for i in s:
        if(i in s_dict):
            s_dict[i]+=1
        else:
            s_dict[i] = 1
    print(s_dict)
    t_dict = {}
    for i in t:
        if(i in t_dict):
            t_dict[i]+=1
        else:
            t_dict[i] = 1
    print(t_dict)
    for key in s_dict:
        if(key in t_dict and s_dict[key] == t_dict[key]):
            output = True
        else:
            output = False
            break
else:
    output = False

print(output)
