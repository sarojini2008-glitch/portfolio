import matplotlib.pyplot as plt
fig = plt.figure()
patterns = ["/","\\","|","-","+","x","o","O",".","*"]
ax1 = fig.add_subplot(111)
for i in range(len(patterns)):
    ax1.bar(i,3,color ='blue',edgecolor = 'black',hatch = patterns[i])
plt.savefig("hi.png")
plt.show()
