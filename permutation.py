# Given two strings, write a method to decide if one is a permutation of the other. 

# def Permutation(st1, st2):
#     st1 = "fast"
#     st2 =" tasf"

#     if len(st1) != len(st2):
#         return False
#     st1 = list(sorted[st1])
#     st2 = list(sorted[st2])
#     for i in range(len(st1)):
#         if st1[i] != st2[i]:
#             return False

#     return True


# def  Permutation(str1, str2):
#     if len(str1) != len(str2):
#         return False
#     dict_one = {}
 
#     for i in str1:
#         if i in dict_one.keys():
#             dict_one[i] += 1
#         else:
#             dict_one == 1

#     for i in str2:
#         if i not in dict_one.keys():
#             return False
#         dict_one[i] -=1
#         if dict_one[i] < 0:
#             return False

#     for count in dict_one.values():
#         if count > 0:
#             return False
#     return True

# print(Permutation("taro", "rato"))
# print(Permutation("leet", "teel"))
# print(Permutation("terp", "rato"))

        


# def Permutation(str1, str2):
#     if len(str1) != len(str2):
#         return False
#     count_one = {}
#     count_two = {}

#     for i in str1:
#         count_one[i] = 1 +  count_one.get(i, 0)
#     for i in str2:
#         count_two[i] = 1 +  count_two.get(i, 0)
    
#     return count_one == count_two
    




