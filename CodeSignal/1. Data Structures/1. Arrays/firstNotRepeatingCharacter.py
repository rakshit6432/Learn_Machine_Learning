def firstNotRepeatingCharacter(s):
    length = len(s)
    for i in range(length):
        if s[i] not in s[i + 1: length] and s[i] not in s[0: i]:
            return s[i]
    return '_'
