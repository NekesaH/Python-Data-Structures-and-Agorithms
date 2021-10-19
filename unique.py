#implement an algorithm to determine if a string has all unique character3

#bruteforce method
def uniqueCharacters(str):
    for i in range(len(str)):
        for j in range(i + 1, len(str)):
            if(str[i] == str[j]):
                return False

    return True
# sort

def uniqueCharacters(strng):
    strng = sorted(strng)
    for i in range(len(strng)-1):
        if (strng[i] == strng[i+ 1]):
            return False
        return True



# using dictionary

def uniqueCharacters(st):
    check = {}

    for char in st:
        if (char in check.keys()):
           check[char] +=1
        else:
            check[char] = 1
    for char in check:
        if check[char] > 1:
            return False
    return True

   
print(uniqueCharacters("mugo"))



#Given a string, find the first non-repeating character 
# 
#in it and return it’s index. If it doesn’t exist, return -1.

# def uniqueCharacters(st):
#     check = {}

#     for i in st:
#         if i in check:

#             check[i] += 1
#         else:
#             check[i] = 1

#     for i in range(len(st)):
#         if check[st[i]] == 1:
#             return i
#     return -1
    
       
   
# print(uniqueCharacters("leetcode"))