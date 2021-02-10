import pygal
from die import Die

# Setup the dice
die_1 = Die()
die_2 = Die()

# Generate roll data
maximum_value = die_1.num_sides * die_2.num_sides
results = [die_1.roll() * die_2.roll() for x in range(1, 1001)]

# Analyze roll data
frequencies = [results.count(value) for value in range(1, maximum_value+1)]

# Visualize roll data
hist = pygal.Bar()
hist.title = "Results from rolling two D6 dice and multiplying"
hist.x_labels = [str(x) for x in range(1, maximum_value+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 * D6", frequencies)
hist.render_to_file('d6_mult_visual.svg')
