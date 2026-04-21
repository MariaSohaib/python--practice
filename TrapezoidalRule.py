def trapezoidalRule(a,b,n,f):
    h=(b-a)/n
    sol=f(a)+f(b)
    for i in range(1,n):
        sol=sol+(2*f(a+(i*h)))
    return sol*(h/2)
def f(x):
    return 1/x**2
def main():
    solution=trapezoidalRule(1,3,2,f)
    print(f"Solution: {solution}")
if __name__=="__main__":
    main()