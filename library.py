#V000717410 Ange Lena Moukete
ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"


def is_alpha(word):
    for letter in word: 
        if letter not in ASCII_LOWERCASE and letter not in ASCII_UPPERCASE:
            return False
    
    return True

(is_alpha("HELLO"))

def is_digit(s):
    for number in s: 
        if number not in DECIMAL_DIGITS:
            return False
        
    return True
(is_digit("1,2,3"))

def to_lower(s):
    for letter in s:
        if 'A' <= letter <= 'Z': 
            result += chr(ord(letter) + 32) 
    else:
        return letter
(to_lower("hello"))


def to_upper(s):
    for letter in s:
        if ord(letter) >= 97 and ord(s)<= 122:
            return chr(ord(s))
        
(to_upper("HELLO"))


def find_chr(s, char):
    for i in range(len(s)): 
        if s[i] == char:
            return i
        return -1
(find_chr('hello','l'))
    

def find_str(s, substr):
    for i in range(len(s) - len(substr) + 1):
        if s[i:i + len(substr)] == substr:
            return i
    return -1
(find_str('hello','lo'))

def replace_chr(s, old, new):
    result = ""
    for letter in s:
        if letter == old:
            result += new  
        else:
            result += letter  
    return result
(replace_chr("hello","h","H"))

def replace_str(s, old, new):
    result = ""
    i = 0
    while i < len(s):
        if s[i:i + len(old)] == old:  
            result += new  
            i += len(old)  
        else:
            result += s[i]  
            i += 1
    return result
print(replace_str('good','g','G'))

