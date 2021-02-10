import matplotlib.pyplot as plt

# Data and call to scatter
x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, s=40, c=y_values, cmap=plt.cm.Reds)

# Graph formatting
plt.title("Cubes", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([1, 5000, 1, 125000000000])

plt.show()
