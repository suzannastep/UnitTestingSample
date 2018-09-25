# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
Suzanna Stephenson
Volume 1 Labs
9/18/18
"""

import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def var_of_means(n):
    """Constructs a random matrix A with values drawn from the standard normal
    distribution. Calculates the mean value of each row, then calculate the
    variance of these means. Returns the variance.

    Parameters:
        n (int): The number of rows and columns in the matrix A.

    Returns:
        (float) The variance of the means of each row.
    """
    A = np.random.normal(size = (n, n))
    x = A.mean(axis = 1)
    return x.var()


def var_of_means_plot():
    """Creates an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    array = np.array([var_of_means(n) for n in range(100, 1100, 100)])
    xaxis = np.array([n for n in range(100, 1100, 100)])
    plt.plot(xaxis, array)
    plt.show()
    return array



def trigplotter():
    """Plots the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi].
    """
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    sinx = np.sin(x)
    cosx = np.cos(x)
    arctanx = np.arctan(x)
    plt.plot(x, sinx)
    plt.plot(x, cosx)
    plt.plot(x, arctanx)
    plt.show()
    return


def functionplotter():
    """Plots the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    def f(x):
        return 1/(x-1)
    x1 = np.linspace(-2, 1, 100)
    x2 = np.linspace(1, 6, 100)
    plt.plot(x1[:-1], f(x1[:-1]), 'm--', lw = 4) #don't include teh last element in x1 to avoid div by 0 error
    plt.plot(x2[1:], f(x2[1:]), 'm--', lw = 4) #don't include the 0 element in x1 to avoid div by 0 error
    plt.xlim(-2, 6)
    plt.ylim(-6, 6)
    plt.show()
    return


def subplots():
    """Plots the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi].
        1. Arrange the plots in a square grid of four subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    x = np.linspace(0, 2*np.pi, 100)
    plt.suptitle("Stretching and Shrinking Functions")

    plt.subplot(221)
    plt.axis([0, 2*np.pi, -2, 2])
    plt.title("sin(x)")
    plt.plot(x, np.sin(x), "g-")

    plt.subplot(222)
    plt.axis([0, 2*np.pi, -2, 2])
    plt.title("sin(2x)")
    plt.plot(x, np.sin(2*x), "r--")

    plt.subplot(223)
    plt.axis([0, 2*np.pi, -2, 2])
    plt.title("2sin(x)")
    plt.plot(x, 2*np.sin(x), "b--")

    plt.subplot(224)
    plt.axis([0, 2*np.pi, -2, 2])
    plt.title("2sin(2x)")
    plt.plot(x, 2*np.sin(2*x), "m:")

    plt.show()
    return



def FARSviz():
    """Visualizes the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    crashdata = np.load('FARS.npy')
    timeofday = crashdata[:,0]
    longitude = crashdata[:,1]
    lattitude = crashdata[:,2]

    plt.subplot(121)
    plt.title("Crash Locations")
    plt.plot(longitude, lattitude, "k,", markersize=1)
    #plt.axis("equal")
    plt.axis([-175, -50, 0, 80])
    plt.xlabel("Longitude")
    plt.ylabel("Lattitude")

    plt.subplot(122)
    plt.title("When Crashes Happen")
    plt.hist(timeofday, 24)
    #plt.axis([0, 23, 0, 10000])
    plt.xlim(0, 23)
    plt.ylim(0, 10000)
    plt.xlabel("Time of Day")
    plt.ylabel("Number of Crashes")

    plt.show()
    return


def level_curve_heat_map():
    """Plot the function f(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of f, and one with a contour
            map of f. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Add a colorbar to each subplot.
    """
    #Create the values to plot
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = x.copy()
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X)*np.sin(Y)/X/Y

    #Heat map of g
    plt.subplot(121)
    plt.pcolormesh(X, Y, Z, cmap = 'magma')
    plt.colorbar()

    #Contour map of g
    plt.subplot(122)
    plt.contour(X, Y, Z, 10, cmap = 'magma')
    plt.colorbar()

    plt.show()
    return

if __name__ == "__main__":
    print(var_of_means_plot())
    trigplotter()
    functionplotter()
    subplots()
    FARSviz()
    level_curve_heat_map()
