strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    anagrams = {}
    for word in strs:
        sorted_word = "".join(sorted(word))
        print(word , sorted_word)
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    return list(anagrams.values())

print(groupAnagrams(strs))