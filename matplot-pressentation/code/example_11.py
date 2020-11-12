from matplotlib import pyplot as plt
import numpy as np



fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
ax.pie(students, labels = langs,autopct='%1.2f%%')
plt.show()







# y = np.array([35, 25, 25, 15])
# mylabels = ["C", "C++", "Python", "Java"]
# myexplode = [0.2, 0, 0, 0]
# plt.pie(y, explode = myexplode , labels = mylabels)
# plt.show() 