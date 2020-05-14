def sum(n):
    sum=0
    while n>0:
            sum=sum+n
            n=n-1
    return sum
a=int(input("enter a positive no upto which you want to find sum: "))
b=sum(a)
print("sum of positive integers upto "+str(a)+" = " +str(b))