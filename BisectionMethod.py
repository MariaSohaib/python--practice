def bisectionMethod(a,b,f,iterations=10):
    c=(a+b)/2
    if iterations==0:
        return [c]
    if(f(c)==0):
       return [c]
    else:
        if(f(a)*f(c)<0):
            return [c]+bisectionMethod(a,c,f,iterations-1)
        else:
            return [c]+bisectionMethod(c,b,f,iterations-1)

def f(x):
    return (x**2)-9

def main():
    root=bisectionMethod(0,1000,f,iterations=10)
    print("Approximate roots:",root)
if __name__=="__main__":
    main()