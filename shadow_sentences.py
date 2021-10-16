#7 Shadow sentences

"""For the purpose of this challenge, shadow sentences are sentences where every word is the same length and order
 but without any of the same letters. Write a function that accepts two parameters that may or may not be shadows of each other.
The function should return True if they are and False if they aren’t.

An example would be "they are round" and "fold two times," which are shadow sentences,
 while "his friends" and "our company" are not because both contain an n."""

def is_shadow_sentence(sentence1, sentence2):


    if len(sentence1) != len(sentence2):
        return False
    
    count1 = []
    count2 = []

    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")

    for count, word in enumerate(words1):

        for letter in word:

            if letter in words2[count]:   # checks for duplicate letter in parrelel word in other sentence
                return False
        
        count1.append(len(word))
        count2.append(len(words2[count]))
       
    if count1 != count2:
        return False

    return True


print(is_shadow_sentence("they are round", "fold two times"))
print(is_shadow_sentence("his friends",  "our company")) 
print(is_shadow_sentence("a big bag of stuff!", "i was not in where?"))




