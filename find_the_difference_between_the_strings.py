# 6 Find the difference between the strings

"""Write a function in Python that accepts two string parameters. The first parameter will be a string of characters, 
and the second parameter will be the same string of characters, but they’ll be in a different order and have one extra character. 
The function should return that extra character.

For example, if the first parameter is "eueiieo" and the second is "iieoedue," then the function should return "d." """

def difference_in_strings(string1, string2):

    sorted_str1 = sorted(string1)
    sorted_str2 = sorted(string2)

    for count, i in enumerate(sorted_str1):

        if i != sorted_str2[count]:

            return sorted_str2[count]
        
        elif len(sorted_str1) == count + 1:

            return sorted_str2[count + 1]
    
    



print(difference_in_strings("eueiieo", "iieoezue" ))
print(difference_in_strings("eueiieo", "iieoedue" ))
