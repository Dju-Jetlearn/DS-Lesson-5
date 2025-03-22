import matplotlib.pyplot as plt
import numpy as np

equation = input("Do you want to do a linear, cubic, or quadratic equation\n")

if equation == "Linear" or equation == "linear":
    x = np.linspace(-1, 51, 50)
    m = 2
    c = 10
    y = m*x + c
    plt.plot(x, y, "r^", label = "Y = MX + C", linewidth = 4)
    plt.axis([0, 50, 0, 50])
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Linear Graph")
    plt.legend()
    plt.show()
elif equation == "Quadratic" or equation == "quadratic":
    x = np.linspace(-1, 51, 50)
    y = (x**2) + (3*x) + 5
    plt.plot(x, y, "r^", label = "Y = X^2 + 3X + 5", linewidth = 4)
    plt.axis([0,50, 0,50])
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Quadratic Graph")
    plt.legend()
    plt.show()
elif equation == "Cubic" or equation == "cubic":
    x = np.linspace(-1, 51, 50)
    y = (x**3) + (x**2) + (7*x) + 12
    plt.plot(x, y, "r^", label = "Y = X^3 + X^2 + 7X + 12")
    plt.axis([0, 50, 0, 50])
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Cubic Graph")
    plt.legend()
    plt.show()
else:
    print("That is not an equation I can do. Sorry.")