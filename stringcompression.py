def string_compression(strng_one: str) -> bool:
    dic = {}
    str1 = ""
    for i in strng_one:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] == 1

    res =(dic[i] + dic.keys())
    
    