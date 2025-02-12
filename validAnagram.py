s = "Anagram"
t = "nagaram"

def isAnagram(s,t):
    if len(s) != len(t):
        return False
    s = sorted(s.lower())
    t = sorted(t.lower())

    if s == t:
        return True
    else:
        return False


isAnagram = isAnagram(s,t)
print(isAnagram)