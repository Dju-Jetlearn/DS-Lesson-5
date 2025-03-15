import matplotlib.pyplot as plt
import numpy as np

# GRAPHS

#y = x graph
x = [1,2,3,4,5]
y = [1,2,3,4,5]

plt.plot(x,y)
plt.show()

#these all change how the graph is represented

#this makes it red and have dots
plt.plot(x,y, "ro")
plt.show()

#this makes it red and be a dotted line
plt.plot(x, y, "r--")
plt.show()

#this makes it green and have triangles
plt.plot(x, y, "g^")
plt.show()

#this makes it blue and be a line
plt.plot(x, y, "b-")
plt.show()

#this makes it blue and be a dotted line
plt.plot(x, y, "b--")
plt.show()

#you can also just have a colour, or just have a graph type
plt.plot(x, y, "r")
plt.show()

#this sets the graph to be preset, so it doesn't change based on x and y
plt.plot(x, y, "r")
plt.axis([0, 10, 0, 200])
plt.show()

#this line makes it a red dotted line, makes a label on the graph, saying Y = X, and says that the width of the line is 4
plt.plot(x, y, "r--", label = "Y = X", linewidth = 4)

#this gives it pre-determined axes
plt.axis([0, 10, 0, 50])

#these two label the x axis and the y axis
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

#this gives the whole graph the title of "Sample Graph"
plt.title("Sample Graph")

#and legend gives it a key
plt.legend()

plt.show()

#multiple plots

x = np.arange(0, 11, 0.2)
y1 = x**2
y2 = x**3

plt.plot(x, y1, "r^", x, y2, "go")
plt.show()

# y = mx + c
x = np.linspace(-5, 5, 100)
m = 3
c = 45
y = m*x + c

plt.plot(x, y, "ro", label = "Y = MX + C")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Y = MX + C")

plt.show()

# Bar Graphs

# x = position of bar
# y = length of bar

x = [1,3,5,7]
y = [2,6,4,9,]
plt.bar(x, y, color = "b")
plt.show()

#does the same thing, but now, there's two in one
plt.bar([1,3,5,7],[2,6,4,9], color = "b")
plt.bar([2,4,6,8],[3,1,5,8], color = "r")
plt.show()

plt.bar(["Male", "Female"], [90, 95])
plt.show()
