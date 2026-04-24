def SimsonsThreeByEight(a,b,n,f):
    h=(b-a)/n
    sol=f(a)+f(b)
    for i in range(1,n):
        if i%3==0:
            sol=sol+(2*f(a+(i*h)))
        else:
            sol=sol+(3*f(a+(i*h)))
    return (((3*h)/8)*sol)
def f(x):
    return (1/(1+x))
def main():
    solution=SimsonsThreeByEight(0,1,6,f)
    print(f"Solution: {solution}")
if __name__=="__main__":
    main()