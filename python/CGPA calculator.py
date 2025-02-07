user=input("are you devansh? ")
if user=="y":
    a=9
    b=10
    c=10
    d=8
    e=7
    scg1 = (a*4.5 + b*4 + c*3.5 + d*3 + e*3)/18

else:

    a=int(input("enter physics cg  "))
    b=int(input("enter engineering drawing cg  "))
    c=int(input("enter maths cg  "))
    d=int(input("enter manufacturing processes cg  "))
    e=int(input("enter professional communication cg  "))

    scg1 = (a*4.5 + b*4 + c*3.5 + d*3 + e*3)/18

print("your scg1 is ",scg1)

f=int(input("enter EEE cg  "))
g=int(input("enter Chemistry cg  "))
h=int(input("enter maths cg  "))
i=int(input("enter C language cg  "))
j=int(input("enter Environmental cg  "))

scg2 = (f*4.5 + g*4 + h*3.5 + i*4 +j*2)/18

print ("your scg2 is ", scg2)

print("Final cg is ", (scg1+scg2)/2)