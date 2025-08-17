a=int(input("Enter a number:" ))

def fac(a):
    if a<2:
        return 1
    else:
        return a*fac(a-1)

ans=fac(a)
print('Factorial of',a,'is:',ans)
