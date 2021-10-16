# 1. Create a Morse code translator

"""We no longer use Morse code to transfer information, but that doesn't mean you can't use it in a code challenge. 
Write a function in Python that takes in a string that can have alphanumeric characters in lower or upper case.

The string can also contain any special characters handled in Morse code, 
including commas, colons, apostrophes, periods, exclamation marks, and question marks. 
The function should return the Morse code equivalent for the string."""

morse_code = {
    'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....',
    'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.',
    'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-',
    'y' : '-.--', 'z' : '--..', '.' : '.-.-.-', '?' : '..--..', ',' : '--..--', ' ' : '/', "&" : ".-...", 
    "'" : ".----.", "@" : ".--.-.", ")" : "-.--.-", "(" : "-.--.", ":" : "---...", "=" : "-...-", "!" : "-.-.--",
    "-" : "-....-", "+" : ".-.-.", "?" : "..--..", "/" : "-..-.", '"' : ".-..-.", "%" : "----- -..-. -----"
    }

def get_morse_translation(message):
    # return " ".join([morse_code[i] for i in message.lower()])

    try:
        return " ".join([morse_code[i] for i in message.lower()])
    except KeyError:
        return"Unfortunately we did not have a Morse Code translation for one of the characters you entered\nPlease try again"
    
print(get_morse_translation("hello wOrld!"))
print(get_morse_translation("hello wOrld!á"))