from sympy import Symbol, lambdify
import sympy as sym
x = Symbol('x')


def computeX(xk, arr, fxD1k, fxD2k):
    arr.append(round(xk - (fxD1k/fxD2k), 4))
    return arr[len(arr)-1]


def newtonRaphson(x1, E):
    X = [x1]

    global x
    # fx = x**2 + (54/x)
    # fx = 0.65 - (0.75/(1+x**2)) - (0.65*x)*sym.atan(1/x)
    # fx = x**2 - 2*sym.sin(x) + 5
    # fx = ((1/2)*x**2) - sym.sin(x)
    # fx = x**2 - 3*x + 4
    fx = x**2
    fxD1 = fx.diff(x)
    fxD2 = fxD1.diff(x)
    # print(fxD1)
    fx = lambdify(x, fx)
    fxD1 = lambdify(x, fxD1)
    fxD2 = lambdify(x, fxD2)
    print("k\txk\t\tf'x(k)\t\tf''x(k)\t\tx(k+1)\t\tf'x(k+1)")
    # step 1
    k = 1
    # fx1D1 = fxD1(x1)
    while True:
        # step 2
        xk = X[k-1]
        fxD1k = fxD1(xk)
        fxD2k = fxD2(xk)
        xk1 = computeX(xk, X, fxD1k, fxD2k)
        fxD1k1 = fxD1(xk1)

        print("{}\t{:.3f}\t\t{:.3f}\t\t{:.3f}\t\t{:.3f}\t\t{:.3f}".format(
            k, xk, fxD1k, fxD2k, xk1, fxD1k1))

        if abs(fxD1k1) < E:
            break
        else:
            k = k+1
    print()
    for i in range(len(X) - 1):
        print("x{} = {:.3f}".format(i+1, X[i]), end=" | ")
    print("x{} = {:.3f}\nFunction value at x={:.3f} →  {:.4f}".format(
        len(X), X[len(X)-1], X[len(X)-1], fx(X[len(X)-1])))
    return


def main():
    print("\nMake sure you have changed the function...")
    x1 = float(input("(initial guess)x1: "))
    E = float(input("(epsilon) ϵ:"))
    newtonRaphson(x1, E)
    print("\n")
    return


if __name__ == "__main__":
    main()
