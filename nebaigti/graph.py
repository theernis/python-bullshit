import pygame
import math


pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

size = int(input("screen size (int 300): "))
line_width = int(input("line width (int 5): "))
pixel_size = float(input("pixel value (float 1): "))

dis_width = size * 2 + 1
dis_height = size * 2 + 1
resolution = (dis_width, dis_height)
dis = pygame.display.set_mode(resolution)
pygame.display.set_caption('Graph')

is_hacking = False

def hack_lol(a):
	global is_hacking
	if not is_hacking:
		print("hacking lol")
		is_hacking = True
	return math.pi*math.sqrt(size)*math.sin(a)

def draw_graph(values):

	surface = pygame.Surface((dis_width,dis_height), flags=pygame.SRCALPHA)
	
	for a in range(dis_width):
		for b in range(dis_height):
			try:
				x = (a - size - 1) * pixel_size
				y = (b - size - 1) * pixel_size
				c = eval(values[0])
				d = eval(values[1])
				if abs(c-d) < line_width * pixel_size:
					surface.set_at((a, b), red)
			except:
				print("calculation error")
	
	global is_hacking
	is_hacking = False
	return surface


def game_loop():
	game_over = False

	graph = pygame.Surface((dis_width,dis_height), flags=pygame.SRCALPHA)

	while not game_over:
		
		dis.fill(black)
		pygame.draw.line(dis, white, (0, size), (size * 2 + 1, size), line_width)
		pygame.draw.line(dis, white, (size, 0), (size, size * 2 + 1), line_width)

		dis.blit(graph, (0, 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				import sys
				sys.exit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 3:

					equation = input("equation: ")
					values = equation.split("=")
					if len(values) != 2:
						print("impossible equation")
						values = ["0", "size"]

					graph = draw_graph(values)

		pygame.display.flip()


game_loop()