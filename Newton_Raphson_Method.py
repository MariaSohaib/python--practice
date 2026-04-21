import math
def Newton_Raphson(f,x_initial,f_der,iterations=10):
    sol=x_initial-(f(x_initial)/f_der(x_initial))
    if iterations==0:
        return [sol]
    if f(sol)==0:
        return [sol]
    else:
        return [sol]+ Newton_Raphson(f,sol,f_der,iterations-1)

def f(x):
    return x+math.sin(x)
def f_der(x1):
    return 1+math.cos(x1)
def main():
    solutions=Newton_Raphson(f,5,f_der,iterations=10)
    print(solutions)
if __name__=="__main__":
    main()