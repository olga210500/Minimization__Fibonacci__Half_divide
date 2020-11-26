def func(x):
    return (x**5-5*x**3+10*x**2-5*x)

def half_divide(func, segment, eps):
    a=segment[0]
    b=segment[1]
    x1 = (a + b-eps) / 2
    x2=(a+b+eps)/2
    k=0
    while (b-a)>eps:
        if func(x1)<=func(x2):
            b=x2
            x1 = (a + b - eps) / 2
            x2 = (a + b + eps) / 2
        else:
            a = x1
            x1 = (a + b - eps) / 2
            x2 = (a + b + eps) / 2
        k= k + 1
        if k==50:
            break
        yield (a+b)/2


def n_Fibonacci_numb(n):
    a=1
    b=a
    count=1
    while count<n:
        temp=b
        a=b
        b= temp + a
        count= count + 1
    return a

def count_numb(n):
    a = 1
    b = a
    count = 0
    while a<=n:
        temp=a
        a=b
        b= temp + a
        count= count + 1
    return count

def Method_Fibonacci(func, segment, eps):
    a = segment[0]
    b = segment[1]

    count_n=(b - a) / eps
    n = count_numb(count_n)
    x1 = a + (n_Fibonacci_numb(n - 2) / n_Fibonacci_numb(n)) * (b - a)
    x2 = a + (n_Fibonacci_numb(n - 1) / n_Fibonacci_numb(n)) * (b - a)
    count=0
    while n_Fibonacci_numb(0) < ((b - a) / eps):

        if func(x1)<=func(x2):
            b = x2
            x2 = x1

            x1 = a + (n_Fibonacci_numb(n - count - 3) / n_Fibonacci_numb(n - count - 1)) * (b - a)
        else:
            a = x1
            x1 = x2
            x2= a + (n_Fibonacci_numb(n - count - 2) / n_Fibonacci_numb(n - count - 1)) * (b - a)
        count= count + 1
        yield ((a + b) / 2)


def find_line_segment(func, x, h):
    if func(x) < func(x + h):
        h = -1*h
    hi=h
    xi=x
    i=0
    while func(xi) > func(xi + hi):
        xi = xi + hi;
        hi = 2 * hi;
        i= i + 1
    xn=[]
    xn.append(xi + hi);
    xn.append(xi);
    xn.append(xi - (hi / 2));
    xn.append(xi + hi - hi / 2);
    a=0
    b=0
    if func(xn[0]) < func(xn[2]):
        a = min(xn[0], xn[1])
        b = max(xn[1], xn[0])
    if func(xn[0]) > func(xn[2]):
        a = min(xn[2], xn[3])
        b = max(xn[2], xn[3])
    segment=[]
    segment.append(a)
    segment.append(b)
    return segment




x0=-2
h=0.5
eps=0.00001
i=0
j=0



print("Line segment:", find_line_segment(func, x0, h) )
print("\nFibonacci method")

for x in Method_Fibonacci(func,find_line_segment(func, x0, h), eps):
    i = i + 1
    print("i=", i,"   x=", x,"                                      f(x)=", func(x))



print("Half divide method")

for xi in half_divide(func,find_line_segment(func, x0, h), eps):
    j = j + 1
    print("i=", j,"   x=", xi,"                                      f(x)=", func(xi))

