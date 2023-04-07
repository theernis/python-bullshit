import pygame, math, random, collections

dis_width = 300
dis_height = 200
resolution = (dis_width, dis_height)
dis = pygame.display.set_mode(resolution)
pygame.display.set_caption('Random')

def f(displacement):
	f_list = []
	for a in range(dis_width):
		x = a/(dis_width-1)
		f_list.append(math.cos((x-displacement)*math.pi/4))
	value_min = min(f_list)
	for a in range(len(f_list)):
		f_list[a] = f_list[a] - value_min
	value_max = max(f_list)
	for a in range(len(f_list)):
		f_list[a] = f_list[a] / value_max
	return f_list

def P(width, f_list):
	value_sum = sum(f_list)
	return sum(f_list[:width+1]) / value_sum

def smooth(line, value):

	line2 = []

	for a in range(len(line) - 1):
		line2.append([(line[a][0] + line[a+1][0]) / 2, (line[a][1] + line[a+1][1]) / 2])
	

	if(value > 0):
		return smooth(line2, value - 1)
	else:
		return line2

def gameLoop():
	game_over = False
	black = (0, 0, 0)
	white = (255, 255, 255)
	red = (255, 0, 0)
	blue = (0, 0, 255)

	displacement = .5

	new_surface = pygame.Surface((dis_width,dis_height), flags=pygame.SRCALPHA)

	graph = f(displacement)

	for a in range(dis_width):
		new_surface.set_at((a, int(graph[a] * (dis_height - 1))), white)
		
	for a in range(dis_height):
		new_surface.blit(new_surface, (0, -a))

	random_values = []
	while not game_over:
		dis.fill(black)
		dis.blit(new_surface, (0, 0))

		P_list = []
		for a in range(dis_width):
			P_list.append(P(a, graph))
		P_list = list(dict.fromkeys(P_list))
	
		value = random.random()
		nearest = 0
		location = 0
		for a in range(len(P_list)):
			if (abs(P_list[a] - nearest) > abs(P_list[a] - value)):
				nearest = P_list[a]
				location = a
		random_values.append(location)
		random_values.sort()

		counter = collections.Counter(random_values)
		coordinates = list(counter.items())
		coordinates = [list(tup) for tup in coordinates]
		height = 0
		for a in coordinates:
			if a[1] > height:
				height = a[1]
		for a in range(len(coordinates)-1):
			try:
				pygame.draw.line(dis, red, (coordinates[a][0], (coordinates[a][1] - 1) / (height - 1) * (dis_height-1)), (coordinates[a+1][0], (coordinates[a+1][1] - 1) / (height - 1) * (dis_height - 1)))
			except:
				pass

		smooth_line = smooth(coordinates, height)
		smooth_line.insert(0, [0,0])
		smooth_line.append([dis_width - 1, 0])
		for a in range(len(smooth_line)-1):
			try:
				pygame.draw.line(dis, blue, (smooth_line[a][0], (smooth_line[a][1] - 1) / (height - 1) * (dis_height-1)), (smooth_line[a+1][0], (smooth_line[a+1][1] - 1) / (height - 1) * (dis_height - 1)), int(height ** .5))
			except:
				pass

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				import sys
				sys.exit()

		pygame.display.update()
		
gameLoop()