# factorial using recursion

n = int(input("enter a number: "))
def fact(n):
    if n ==0:
        return 1
    return n*fact(n-1)



fact(n)
print(fact(n))
