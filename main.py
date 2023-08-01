import matplotlib.pyplot as plt
import numpy
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
import random

def testcalc(initprice, reqamount):
    random.seed(10)
    tokenprice = initprice #146.14
    topurchasetokens = reqamount #1724
    liquidity = 90367
    tokens = 0
    totalspend = 0
    iteration = 0
    while tokens < topurchasetokens:
        canpurchase = liquidity / tokenprice
        if canpurchase + tokens > topurchasetokens:
            topurchaseiteration = topurchasetokens - tokens
        else:
            topurchaseiteration = canpurchase

        tokens += topurchaseiteration
        spent = topurchaseiteration * tokenprice
        totalspend += spent
        if canpurchase > 2:
            tokenprice = tokenprice * 1.02
            #liquidity = liquidity * 0.98

        #print("iteration: " + str(iteration) + "\t tokens: " + str(tokens) + "\t spend: " + str(spent) + "\t price: " + str(tokenprice) + "\t topurchaseiteration: " + str(topurchaseiteration))
        iteration += 1

    return totalspend

def calc(X,Y):
    print(X)
    Z = [[0]*len(X) for i in range(len(X[0]))]
    for a in range(len(X)):
        for b in range(len(X)):
            Z[a][b] = testcalc(X[a][b], Y[a][b])
    return Z

def graph():
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    X = np.arange(0.87, 146.14, 0.72635)  # Token price
    Y = np.arange(100, 1724, 8.12069)  # Token amount

    X, Y = np.meshgrid(X, Y)

    Z = calc(X, Y)
    # Plot the surface
    Z = np.array(Z)
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    # ax.set_zlim(-1.01, 1.01)
    # ax.zaxis.set_major_locator(LinearLocator(10))
    # A StrMethodFormatter is used automatically
    ax.zaxis.set_major_formatter('{x:.02f}')

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

def arraytesting():
    A = np.arange(0, 10, 1)
    B = np.arange(10, 20, 1)
    A,B = np.meshgrid(A,B)
    Z = [[69] * len(A) for i in range(len(A[0]))]

    for x in range(len(A)):
        for y in range(len(A[x])):
            Z[x][y] = A[x][y] * B[x][y]
    G = A*B
    print(np.array_equal(G,Z))

def averagepricegraph():
    tokenamounts = np.arange(100, 300000, 1)
    averages = []
    for x in range(len(tokenamounts)):
        averages.append(testcalc(10.87, tokenamounts[x]) / tokenamounts[x])
    print(averages)
    fig, ax = plt.subplots()
    ax.set_ylabel("Average price per token in USD")
    ax.set_xlabel("Amount of tokens purchased")
    ax.plot(tokenamounts,averages)
    plt.show()

averagepricegraph()