def Fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return Fib(n-1)+Fib(n-2)

Fib(8)
print(Fib)


ko(8)
print(koko)

def koko(n):
   if n == 1:
      return 1
   elif n == 0:
      return 0
   else:
      return fib(n-1) + fib(n-2)

koko(8)
print(koko)