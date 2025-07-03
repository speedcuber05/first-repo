user=input("are you devansh? ")
if user=="y":
    a=9
    b=10
    c=10
    d=8
    e=7
    f=9
    scg1 = (a*4.5 + b*4 + c*3.5 + d*3 + e*3 + f*1)/19

else:

    a=int(input("enter physics cg  "))
    b=int(input("enter engineering drawing cg  "))
    c=int(input("enter maths cg  "))
    d=int(input("enter manufacturing processes cg  "))
    e=int(input("enter professional communication cg  "))
    f=int(input("enter bootcamp cg  "))

    scg1 = (a*4.5 + b*4 + c*3.5 + d*3 + e*3 + f*1)/19

print("your scg1 is ",scg1)

g=int(input("enter EEE cg  "))
h=int(input("enter Chemistry cg  "))
i=int(input("enter maths cg  "))
j=int(input("enter C language cg  "))
k=int(input("enter Environmental cg  "))

scg2 = (g*4.5 + h*4 + i*3.5 + j*4 + k*2)/18

print ("your scg2 is ", scg2)

print("Final cg is ", (scg1+scg2)/2)