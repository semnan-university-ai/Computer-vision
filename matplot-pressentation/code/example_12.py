# from mpl_toolkits import mplot3d
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
# y = x.copy().T 
# z = np.cos(x ** 2 + y ** 2)

# fig = plt.figure()
# ax = plt.axes(projection='3d')

# ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none')
# ax.set_title('Surface plot')
# plt.show()










import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from scipy.stats import multivariate_normal

x, y = np.mgrid[-1.0:1.0:30j, -1.0:1.0:30j]

xy = np.column_stack([x.flat, y.flat])

mu = np.array([0.0, 0.0])

sigma = np.array([.5, .5])
covariance = np.diag(sigma**2)

z = multivariate_normal.pdf(xy, mean=mu, cov=covariance)

z = z.reshape(x.shape)

fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')



ax.plot_surface(x,y,z)

plt.show()