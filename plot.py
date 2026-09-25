import matplotlib.pyplot as plt
x=[0,20,40,60,80,100]
y=[0,20,40,60,80,100]
plt.xlabel("variable x")
plt.ylabel("variable y")
plt.title("plot")
fig = plt.figure()
patterns = ["o"]
plt.(color ='blue',linewidth=1,hatch = patterns)
plt.savefig("hi.png")
plt.show()
