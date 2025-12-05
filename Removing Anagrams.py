words = ["abba","baba","bbaa","cd","cd"]
i=0

while i < len(words)-1:
    if((sorted(words[i]) == (sorted(words[i+1])))):
        words.remove(words[i+1])
        continue
    i+=1

print(words)

