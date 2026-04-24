def SimsonOneByThree(a,b,n,f):
    h=(b-a)/n
    sol=f(a)+f(b)
    for i in range(1,n):
        if i%2==0:
            sol=sol+2*f(a+(i*h))
        else:
            sol=sol+4*f(a+(i*h))
    return ((h/3)*sol)

def f(x):
    return (1/(1+x))
def main():
    solutions=SimsonOneByThree(0,1,4,f)
    print(f"Solution: {solutions}")
if __name__=="__main__":
    main()