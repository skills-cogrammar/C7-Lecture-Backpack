#Please make sure you have
#Python, NumPy, Pandas, 
#Matplotlib, Seaborn and Jupyter Notebook
#before Tutorial session

import matplotlib.pyplot as plt
import numpy as np
#########################################
#Bar plots
#x,y for 1st and 2nd barplots
x1 = np.array(["cats", "dogs", "rabbits", "goldfish"])
y1 = np.array([3, 8, 2, 10])
x2 = np.array(["tiger", "lion", "cheetah", "leopard"])
y2 = np.array([4, 2, 1, 6])

#Subplot, parameters(rows, columns, index of current plot)
plt.subplot(2,1,1)
plt.bar(x1, y1, color = 'g', width=0.3)
plt.subplot(2,1,2)
plt.barh(x2, y2, color = '#800080', height=0.2)
plt.show()

#########################################
#Pie charts
y = np.array([20, 35, 30, 15])
mylabels = ['Blueberry', 'Pineapple','Apple', 'Kiwi']
mycolors = ['b', 'y', 'r', 'g']
myexplode = [0, 0, 0, 0.2]

plt.pie(y, labels = mylabels, colors = mycolors, 
        explode = myexplode, shadow = True)
plt.legend(loc='center left',title = "Four Fruits:")
plt.show() 

#########################################
#Lineplots
pi = np.pi
# Creating x axis with range 
#and y axis with sine/cosine
x = np.arange(0, 4*pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

#Plotting sine/cosine on the same plot
plt.plot(x,y1, label='Sine', ls='--')
plt.plot(x,y2, label='Cosine', lw=2, c='crimson')

#x-axis, y-axis label, and plot title
plt.xlabel('x')
plt.ylabel('y=f(x)')
plt.title('Sine and Cosine functions')

#Legend for the two curves
plt.legend()
plt.show() #plt.savefig('sine.png')

#########################################
#Scatter plot and histogram
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)

plt.hist(x, color='cornflowerblue', alpha=0.5)
plt.show()

plt.scatter(x, y, c=colors)
plt.colorbar()
plt.show()