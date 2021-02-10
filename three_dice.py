import pygal
from die import Die

# Setup the dice
die_1 = Die()
die_2 = Die()
die_3 = Die()

def get_dice_roll(d1, d2, d3):
	return d1.roll() + d2.roll() + d3.roll()
# Generate roll data
maximum_value = die_1.num_sides + die_2.num_sides + die_3.num_sides
results = [get_dice_roll(die_1, die_2, die_3) for x in range(1, 1001)]

# Analyze roll data
frequencies = [results.count(value) for value in range(3, maximum_value+1)]

# Visualize roll data
hist = pygal.Bar()
hist.title = "Results from rolling three dice"
hist.x_labels = [str(x) for x in range(3, maximum_value+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D6 + D6", frequencies)
hist.render_to_file('three_dice_visual.svg')
