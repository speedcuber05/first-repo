# things to add 
# log
# trigo
# M+ M- and stuff


print("operator codes")
print('enter 1 for n1 + n2')
print('enter 2 for n1 - n2')
print('enter 3 for n1 * n2')
print('enter 4 for n1 ** n2')
print('enter 5 for n1 / n2')
print('enter 6 for n1 // n2')
print('enter 7 for n1 % n2')
print('enter 8 for n1 > n2')
print('enter 9 for n1 < n2')
op=int(input("enter the operator code "))
n1=int(input("enter n1  "))
n2=int(input("enter n2  "))

def calculator(n1,n2):
    global ans
    global op
    if op==1:   
        ans=n1+n2
        print(ans)
    if op==2:   
        ans=n1-n2
        print(ans)
    if op==3:   
        ans=n1*n2
        print(ans)
    if op==4:   
        ans=n1**n2
        print(ans)
    if op==5:   
        ans=n1/n2
        print(ans)
    if op==6:   
        ans=n1//n2
        print(ans)
    if op==7:   
        ans=n1%n2
        print(ans)
    if op==8:
        ans=n1>n2
        print(ans)
    if op==9:
        ans=n1<n2
        print(ans)
calculator(n1,n2)
while 1==1:
    con=input("do you want to continue with operations? y/n  ")
    if con=='n':
        break
    else:
        if op<8 and op>0:
            n1=ans
        op=int(input("enter the operator code "))
        n2=int(input("enter next number  "))
        calculator(n1,n2)
