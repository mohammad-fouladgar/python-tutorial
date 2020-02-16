def f(n):

    if (n < 2):
        return 1
    
    return f(n-1) + f(n-2)

def fibo(n):
    a,b =0,1
    result = []
    while a < n:
        result.append(a)
        a , b =b, a +b
    
    return result

print(fibo(5))
# print(f(5))