def vowels(s: str) -> str:
    # write your code here
    c=0
    for i in s:
        if i in "aeiouAEIOU":
            c+=1
    if c%2==0:
        return "yes"
    else:
        return "no"
    pass

a=vowels("xayyqez")
print(a)
b=vowels("ssty")
print(b)
