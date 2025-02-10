import time
print(time.time())                               #tells current time in seconds
print(time.gmtime())                             #converts seconds into non proper format UTC
print(time.ctime())                              #converts seconds into proper format local
print(time.localtime())                          #converts seconds into non proper format local
a=time.gmtime()
print(time.mktime(a))                            #converts non proper format into seconds
print(time.strftime("%a, %d %b %Y %H:%M:%S",a))  #converts non proper format into proper format customizable
print(time.asctime(a))                           #converts non proper format into proper format non customizable
b=time.strftime("%a, %d %b %Y %H:%M:%S",time.gmtime())
print(time.strptime(b,"%a, %d %b %Y %H:%M:%S"))  #converts proper format into non proper format
for i in range(4):
	time.sleep(1)
	print(i)