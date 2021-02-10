import matplotlib.pyplot as plt
import numpy as np
from die import Die

# Create the two 6-sided dice
die_1 = Die()
die_2 = Die()

# Generate the roll data
results = [die_1.roll() + die_2.roll() for x in range(1, 1001)]

# Group the roll data results by frequency
frequencies = [results.count(value) for value in range(2, 13)]

# Create and format the bar plot (histogram) to display the frequency of dice roll outcomes
# Using https://matplotlib.org/3.3.3/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py as a reference

x_axis_ticks = range(2, 13) # using range() instead of np.arrange() because values are integers
width = 0.50 # width of the bars

fig, ax = plt.subplots()
rectangles = ax.bar(x_axis_ticks, frequencies, width, label='Frequency of roll outcome')

ax.set_title('Outcome of rolling two 6-sided dice 1000 times')
ax.set_ylabel('Frequency of roll outcome')
ax.set_xlabel('Roll outcome')
ax.set_xticks(x_axis_ticks)
ax.legend()

def autolabel(rects):
	"""Assign a label above each bar in *rects*, displaying its height."""
	for rect in rects:
		height = rect.get_height()
		ax.annotate(str(height),
			xy=(rect.get_x() + rect.get_width() / 2, height),
			xytext=(0, 3), # 3 points of vertical offset
			textcoords="offset points",
			ha='center', va='bottom')

autolabel(rectangles)

fig.tight_layout()

plt.show()
