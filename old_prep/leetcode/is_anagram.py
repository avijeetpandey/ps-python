def isAnagram(stringOne, stringTwo):
    if len(stringOne) != len(stringTwo):
        return False

    firstStringCounter = {}
    secondStringCounter = {}

    for char in stringOne:
        firstStringCounter[char] = firstStringCounter.get(char, 0) + 1

    for char in stringTwo:
        secondStringCounter[char] = secondStringCounter.get(char, 0) + 1

    for key, value in firstStringCounter.items():
        if key not in secondStringCounter or secondStringCounter[key] != value:
            return False

    return True


print(isAnagram("anagram", "nagaaram"))