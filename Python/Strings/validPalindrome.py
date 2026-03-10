s = s = ",; W;:GlG:;l ;,"
output = True

cleaned_string = ''.join(char for char in s if char.isalnum())
cleaned_string = cleaned_string.lower()
print(cleaned_string)
for i in range(int(len(cleaned_string)/2)):
    if(cleaned_string[i] == cleaned_string[len(cleaned_string)-1-i]):
        output = True
    else:
        output = False
        break

print(output)