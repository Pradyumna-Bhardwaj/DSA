haystack = "abghij"
needle = "ghij"

# fastest method but pretty much lowest memory 
if(len(needle)>len(haystack)):
    print("-1")

for hay_index, hay_char in enumerate(haystack):
    if(hay_char==needle[0] and hay_index + len(needle) <= len(haystack)):
        # hay_sec = haystack[hay_index:hay_index+len(needle)]
        # print(hay_sec)
        if(needle == haystack[hay_index:hay_index+len(needle)]):
            print(hay_index)
        else:
            continue
if(hay_index == len(haystack)-1):
    print("-1")

# truthy = 0
# for hay_index, hay_char in enumerate(haystack):
#     if(hay_char==needle[0]):
#         truthy = 0
#         for needle_index, needle_char in enumerate(needle):
#             if(hay_index + needle_index < len(haystack) and needle_char == haystack[hay_index+needle_index]):
#                 truthy+=1
#             if(truthy == len(needle)):
#                 print(hay_index)
#                 break
#     if(truthy == len(needle)):
#         break
# if(truthy != len(needle)):
#     print ("-1")