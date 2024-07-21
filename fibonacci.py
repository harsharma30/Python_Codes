import math
def isPerfectsquare(x):
    s=int(math.sqrt(x))
    return s*s==x
def isfibonacci(n):
    hh=(5*(n*n)+4)
    bb=(5*(n*n)-4)
    return(isPerfectsquare(hh) or isPerfectsquare(bb))
y=list(map(int,input("Enter the number:-").strip().split()))
for i in y[:]:
    if(isfibonacci(i)==True):
        print("this number",i,"belongs to fibonaci series")
    else:
        print("this number",i,"does not belongs to fibonacci series" )
