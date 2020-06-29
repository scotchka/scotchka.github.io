y_2 = lambda fact: (lambda f: lambda n: fact(f(f))(n))(
    lambda f: lambda n: fact(f(f))(n)
)

fact = y_2(lambda f: lambda n: 1 if n < 2 else n * f(n - 1))
