import pygame
import math
from queue import Queue

def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()

def algorithm(draw, grid, start, end):
	open_set = Queue()
	visited = {start}
	came_from = {}
	open_set.put(start)

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()

		if current == end:
			reconstruct_path(came_from, end, draw)
			end.make_end()
			return True

		for neighbor in current.neighbors:
			if(neighbor in visited):
				continue
			came_from[neighbor] = current
			visited.add(neighbor)
			open_set.put(neighbor)
			neighbor.make_open()

		draw()

		if current != start:
			current.make_closed()

	return False





