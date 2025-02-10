a='hello'
B='WORLD'
A=a.upper()
b=B.lower()
acap=a.capitalize()
print(A)
print(b)
print(acap)
c='#####hel#lo###'
cstrip=c.rstrip("#")
print(cstrip)
d="Hello Hello"
print(d.center(150,'.'))    #setting up the position of the string 
print(d.count('H'))
print(a.endswith("R",3,5))
e="He's name is Dan. He is an honest man."
print(e.find("is"))         #gives -1 if it can't find the substring
print(e.index("Dan"))
f="kasofaiew12"
print(f.isalnum())          #checks if either alphabet or number
g="Welcome"
print(g.isalpha())
h='cold coffee'
print(h.replace('cold','hot'))
# isdigit(),islower(),isprintable(),isspace(),istitle(),isupper(),startswith(),swapcase(),title(),split(), also exists