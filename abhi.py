def max(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
    
p=input("enter any 3 integers: ")
q=input()
r=input()
m=max(p,q,r)
print("Max of three numbers is: "+str(m))