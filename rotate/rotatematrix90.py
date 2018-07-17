matrix = [	[1,2,3,4,5,6],
			[2,1,2,5,4,5],
			[1,4,3,6,1,2],
			[0,9,8,7,4,5],
			[2,3,4,8,8,5],
			[7,8,5,2,7,4]
]
def rotatematrix90(matrix):
	length = len(matrix[0])
	i = 0
	first = 0
	last = length - 1
	loop = length - 1

 	# how many times we loop is dependent on how many layers there is, which is length/2
	while(i < length/2):
		for x in range(0, loop):
			# swapping values
			temp                   = matrix[first][first+x]
			matrix[first][first+x] = matrix[last-x][first]
			matrix[last-x][first]  = matrix[last][last-x]
			matrix[last][last-x]   = matrix[first+x][last]
			matrix[first+x][last]  = temp
		first = first + 1 # inner first index
		last = last - 1 # inner last index -1, cause we handle the last index in the beginning we don't have to handle it again
		loop = loop - 2 # how many times it loops, every time we go inward lenth decreases by two
		i = i + 1 # incrementing how many times we loop

rotatematrix90(matrix)
