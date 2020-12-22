from sympy import Symbol, lambdify
import sympy as sym

x = Symbol('x')


def bisection():
    global x
    # fx = x**2 + (54/x)  # change the function here
    # fx = sym.exp(x) - x**3
    fx = x**4 - 9*x + 3
    fxD1 = fx.diff(x)
    fx = lambdify(x, fx)
    fxD1 = lambdify(x, fxD1)
    print("\nMake sure you have changed the function...")
    # step 1
    a = float(input("a: "))
    b = float(input("b: "))
    while fxD1(a) > 0 or fxD1(b) < 0:
        print("Enter correct values...")
        a = float(input("a: "))
        b = float(input("b: "))
    x1 = a
    x2 = b
    E = float(input("(epsilon) ϵ:"))
    i = 1
    print("Itr\t\tx1\t\tx2\t\tz\t\tf'(z)")
    while True:
        # step 2
        z = (x2+x1)/2
        fxD1z = fxD1(z)

        print("{}\t\t{:.4f}\t\t{:.4f}\t\t{:.4f}\t\t{:.4f}".format(
            i, x1, x2, z, fxD1z))

        # step 3
        if abs(fxD1z) <= E:
            break
        elif fxD1z < 0:
            x1 = z
        else:
            x2 = z

        i += 1

    return


if __name__ == "__main__":
    bisection()
