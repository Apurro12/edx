import matplotlib.pyplot as plt
import numpy as np


y, x = np.ogrid[-1:1:100j, -1:1:100j]
plt.contour(x.ravel(), 
            y.ravel(), 
            x**2 + y**2, 
            [1,2,3],
            colors='red',)
plt.axis('equal')
plt.show()
