import matplotlib.pyplot as plt


# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') 
# plt.axis([0, 6, 0, 20]) 
# plt.show()





# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r+')     # ditto, but with red plusses
# plt.axis([0, 6, 0, 20]) 
# plt.show()



# plt.plot([1, 2, 3, 4], [1, 4, 9, 16],'go--', linewidth=2, markersize=12)
# plt.axis([0, 6, 0, 20]) 
# plt.show()



# ypoints = [3, 8, 1, 10]
# plt.plot(ypoints, 'o:r')
# plt.show()


# ypoints = [3, 8, 1, 10]
# plt.plot(ypoints, marker = 'o', ms = 20)
# plt.show()

ypoints =[3, 8, 1, 10]
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r')
plt.show()