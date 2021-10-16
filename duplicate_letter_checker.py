# 10. Duplicate letter checker

"""Create a function in Python that accepts one parameter: a string that’s a sentence. 
This function should return True if any word in that sentence contains duplicate letters and False if not."""

def check_duplicate(sentence):
    
    duplicate = False
    words = sentence.lower().split(" ")
    
    for word in words:
        
        letters_used = ""

        for letter in word:

            if letter in letters_used:
                return True
            else:
                letters_used += letter
    return False

print(check_duplicate("A man ate some fish and chips for his tea"))
print(check_duplicate("A man ate some fish and chips for his dinner"))
print(check_duplicate("A lady went to the park"))
print(check_duplicate("A lady went to the zoo"))

