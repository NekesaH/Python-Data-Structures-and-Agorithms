# def Urlify(str1, length):
#     output = []
#     for i in range(length):
#         i = str1[i]
#         if i == ' ':
#             output.append('%20')
#             continue
#         output.append(i)
#     return ''.join(output)


# print(Urlify("Mr John Smith   ", 13))


# def urlify_2(string, length):
#     char_list = list(string)
#     new_index = len(string)
    
#     for i in reversed(range(length)):
#         char = string[i]
#         if char == ' ':
#             char_list[new_index -3: new_index] = '%20'
#             new_index -= 3
#         else:
#             char_list[new_index-1] = char_list[i]
#             new_index -= 1

#     return ''.join(char_list) 


def urlify(string, n):
    # To store the number of spaces in the original string. 
    s = list(string)
    count = 0
    for i in range(0, n):
        if(s[i] == " "):
            count += 1
    
    # Now we find the total length required. 
    # We can directly use len(s), but what if the original string has additional spaces.
    index = n + (count * 2)
    
    for i in reversed(range(0, n)):
        if(s[i] == ' '):
            s[index-1] = '0'
            s[index-2] = '2'
            s[index-3] = '%'
            index -= 3
        else:
            s[index-1] = s[i]
            index -= 1   
    return ''.join(s)
s = "Mr John Smith  "
n = 13
print(urlify(s, n))