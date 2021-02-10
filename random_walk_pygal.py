from random_walk import RandomWalk
import pygal

# Generate a random walk dataset with 10,000 points
rw_dataset = RandomWalk(10000)
rw_dataset.fill_walk()
# Helper function for generating xy_pairs from random walk dataset
def get_xy_pairs(random_walk, start, end):
	"""Generate a list comprehension from the xy-pairings in *random_walk* in _range(*start*, *end*)_"""
	xy_pairs = [(random_walk.x_values[n], random_walk.y_values[n]) for n in range(start, end)]
	return xy_pairs


# Display the dataset as a scatter plot and a line graph
line_chart = pygal.XY()
line_chart.title = "Data from a random walk of 10,000 steps"
#line_chart.x_labels
line_chart.add('Steps 0-999', get_xy_pairs(rw_dataset, 0, 1000))
line_chart.add('Steps 1,000-1,999', get_xy_pairs(rw_dataset, 1000, 2000))
line_chart.add('Steps 2,000-2,999', get_xy_pairs(rw_dataset, 2000, 3000))
line_chart.add('Steps 3,000-3,999', get_xy_pairs(rw_dataset, 3000, 4000))
line_chart.add('Steps 4,000-4,999', get_xy_pairs(rw_dataset, 4000, 5000))
line_chart.add('Steps 5,000-5,999', get_xy_pairs(rw_dataset, 5000, 6000))
line_chart.add('Steps 6,000-6,999', get_xy_pairs(rw_dataset, 6000, 7000))
line_chart.add('Steps 7,000-7,999', get_xy_pairs(rw_dataset, 7000, 8000))
line_chart.add('Steps 8,000-8,999', get_xy_pairs(rw_dataset, 8000, 9000))
line_chart.add('Steps 9,000-9,999', get_xy_pairs(rw_dataset, 9000, 10000))
line_chart.render_to_file('rw_walk_test.svg')

