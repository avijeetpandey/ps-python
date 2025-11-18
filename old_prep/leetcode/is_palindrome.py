st = "A man, a plan, a canal: Panamaa"

def isPalindrome(s):
    cleaned_string = ''.join(c.lower() for c in st if c.isalnum())
    return cleaned_string == cleaned_string[::-1]

print(isPalindrome(st))