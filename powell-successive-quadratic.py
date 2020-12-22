from sympy import Symbol, lambdify
import sympy as sym
x = Symbol('x')


def successiveQuadratic(x1, delta):
    global x
    # fx = x**2 + (54/x)
    fx = x**2 + (16/x) - 1
    # fx = 2*sym.exp(x) - x**3 - 10*x
    fx = lambdify(x, fx)
    flag = 0
    x2 = x1 + delta
    fx1 = fx(x1)
    fx2 = fx(x2)
    if fx1 > fx2:
        x3 = x1 + (2*delta)
    else:
        x3 = x1 - delta
    fx3 = fx(x3)
    print("Itr\tx1\tx2\tx3\tfx1\tfx2\tfx3\tFmin\tXmin\ta0\ta1\ta2\tXbar\tfXbar\tfnDiff\tXDiff")
    i = 1
    while True:
        fx1 = fx(x1)
        fx2 = fx(x2)
        fx3 = fx(x3)
        Fmin = min(fx1, fx2, fx3)
        if Fmin == fx1:
            Xmin = x1
        elif Fmin == fx2:
            Xmin = x2
        else:
            Xmin = x3

        a0 = fx1
        a1 = (fx2-fx1)/(x2-x1)
        a2 = (1/(x3-x2))*(((fx3-fx1)/(x3-x1))-a1)

        Xbar = ((x1+x2)/2)-(a1/(2*a2))
        fXbar = fx(Xbar)

        fnDiff = abs(Fmin-fXbar)
        XDiff = abs(Xmin-Xbar)
        print("{}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.2f}\t{:.2f}\t{:.2f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}".format(
            i, x1, x2, x3, fx1, fx2, fx3, Fmin, Xmin, a0, a1, a2, Xbar, fXbar, fnDiff, XDiff))

        arr = [abs(Xbar-x1), abs(Xbar-x2), abs(Xbar-x3)]
        # Xarr = [x1,x2,x3,Xbar]
        # print(Xarr)

        if not arr[2] == min(arr):
            if Xbar <= x2:
                temp = x2
                x2 = Xbar
                x3 = temp
            else:
                x3 = Xbar
        else:
            if Xbar <= x3:
                x1 = x2
                x2 = Xbar
            else:
                x1 = x2
                x2 = x3
                x3 = Xbar

        if x1 > x2 or x2 > x3:
            flag = 1

        if fnDiff < 0.001:
            break

        i += 1

        # print(arr)
    if flag == 0:
        print("Success")
    else:
        print("Check x values")
    return


def main():
    print("\nMake sure you have changed the function...")
    x1 = float(input("(initial value)x1: "))
    delta = float(input("(delta): "))
    successiveQuadratic(x1, delta)


if __name__ == "__main__":
    main()
