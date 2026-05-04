def fibonacci(x,y,c):
    b=x+y
    if x>c:
        return []
    return [x]+fibonacci(y,b,c)
def main():
    z=fibonacci(0,1,35)
    print(f"Fibonacci sequence: {z}")
if __name__=="__main__":
    main()