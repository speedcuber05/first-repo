print('hello world')                     #both double and single quotations work
print(8)
print('')
print(2+3)
x=30
print(x)
print('10+20 is',x)
print('hello \'what are you doing\'')
print('hello',end='')                    #by default end='\n'
print('hello',x,'nice',sep=' -')         #by default sep=''
print(R"hello\t hello")                  #\t is ignored because r(or R) before the strings indicates it will be a raw string
print("""hello
nice 
            this is""")  


#\’	          Quote
#\\	          Backslash
#\n	          Newline
#\r	          Carriage Return
#\t	          Horizontal Tab
#\b	          Backspace
#\f	          Formfeed
#\v	          Vertical Tab
#\0	          Null Character
#\N{Name}	  Unicode character Database named lookup
#\uxxxxxxxx	  Unicode character with a 16-bit hex value
#\Uxxxxxxxx	  Unicode character with a 32-bit hex value
#\000	      Character with octal value ooo
#\xhh	      Character with hex value hh

# you can select multiples lines and then press ctrl + / to make them into comments
# or you can just make an empty string like this
"""

iska koi use nhi

"""