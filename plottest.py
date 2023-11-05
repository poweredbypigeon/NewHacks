import matplotlib.pyplot as plt

user_data = [[1,2,3,4,5],[True,True,False,False,False],[True,False,True,True,False]]

plt.rcParams["figure.figsize"] = [5, 10]
plt.rcParams["figure.autolayout"] = True

data = user_data
fig = plt.figure()
ax = fig.add_subplot(111)
ax.imshow(data, aspect='auto', cmap="copper", interpolation='nearest')
plt.show()