import pygal
from die import Die

# Setup the two D8 dice
d8_1 = Die(8)
d8_2 = Die(8)

# Generate roll data
maximum_value = d8_1.num_sides + d8_2.num_sides
results = [d8_1.roll() + d8_2.roll() for x in range(1, 1001)]

# Analyze roll data
frequencies = [results.count(value) for value in range(2, maximum_value+1)]

# Visualize roll data
hist = pygal.Bar()
hist.title = "Results from rolling two D8 dice"
hist.x_labels = [str(x) for x in range(2, maximum_value+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D8 + D8", frequencies)
hist.render_to_file('d8s_visual.svg')
