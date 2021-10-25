import numpy as np
import matplotlib.pyplot as plt

x=[[1,2,3],[3,4,5],[5,6,7]]
print(x)

a = np.array(x)
print(a)

x = np.linspace(0,10,100)
y = x ** 2

plt.plot(x,y)
plt.show()
