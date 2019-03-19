# import numpy as np
import numpy as np
# import math
import math
#import matplotlib
import matplotlib.pyplot as plt

x= np.arange(0,4)
y_x = x
y_2x = 2 * x
y_x2 = x*x

# Adding graph title and labels
plt.title("Matplotlib x (red), 2x (green), x2 (blue) in the range [0, 4]")
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 

plt.plot(x,y_x,'r')
plt.plot(x,y_2x,'g')
plt.plot(x,y_x2,'b')

# plt.scatter(x, y_x)
# plt.scatter(x, y_2x)
# plt.scatter(x, y_x2)

plt.show()
