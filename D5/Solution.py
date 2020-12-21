ie = open("List.txt").read().splitlines()
input = []

for i in ie:
	input += [[i[0:7], i[7:10]]]


def find_row(row):
	row_range = [0, 127]
	for ind, letter in enumerate(row):
		if ind != 6:
			if letter == "F":
				row_range[1] -= int(((row_range[1] + 1) - row_range[0]) / 2)
			elif letter == "B":
				row_range[0] += int(((row_range[1] + 1) - row_range[0]) / 2)
			continue
		if letter == 'F':
			ow = row_range[0]
		elif letter == 'B':
			ow = row_range[1]

	return ow


def find_column(column):
	column_range = [0, 7]

	for ind, letter in enumerate(column):
		if ind != 2:
			if letter == "L":
				column_range[1] -= int(((column_range[1] + 1) - column_range[0]) / 2)
			elif letter == "R":
				column_range[0] += int(((column_range[1] + 1) - column_range[0]) / 2)
			continue
		if letter == 'L':
			column = column_range[0]
		elif letter == 'R':
			column = column_range[1]

	return column


def seat_id(put):
	r = find_row(put[0])
	c = find_column(put[1])

	return 8 * r + c


def part1(inp):
	array = []
	for arr in inp:
		array += [seat_id(arr)]
	return max(array)


def part2(inp):
	array = []
	for arr in inp:
		array += [seat_id(arr)]

	array.sort()

	last = array[0]
	print(last)

	for ind, i in enumerate(array):
		if ind == 0:
			continue
		if i != last + 1:
			return last + 1
		last = i


print(part2(input))
