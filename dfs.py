import pygame
import math
from queue import Queue

def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()

def dfs(current, visited, came_from, end, draw, start):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	if current == end:
		reconstruct_path(came_from, end, draw)
		end.make_end()
		return True

	for neighbor in current.neighbors:
		if(neighbor in visited):
			continue
		came_from[neighbor] = current
		visited.add(neighbor)
		neighbor.make_open()
		if dfs(neighbor,visited,came_from,end, draw, start):
			return True
		

	draw()

	if current != start:
		current.make_closed()

	return False


def algorithm(draw, grid, start, end):
	visited = {start}
	came_from = {}
	return dfs(start,visited,came_from, end, draw, start)
	





