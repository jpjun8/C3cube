def foo(x: int, y: float, z: bool = True) -> str:
    if z:
        return str(x + y)
    else:
        return str(x - y)

x = 10
y = 20
a = "x * y"
print(eval(a))