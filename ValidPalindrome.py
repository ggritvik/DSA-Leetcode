s = "A man, a plan, a canal: Panama"
new_s = ""
for i in s:
    if i.isalnum():
        new_s += i.lower()

if new_s == new_s[::-1]:
    print(True)
else:
    print(False)