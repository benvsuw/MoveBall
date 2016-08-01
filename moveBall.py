# Move a Circle 
# Author Ben Vander Schaaf benvsuw@gmail.com
# MIT license
import pygame, sys
from pygame.locals import *

WINDOWWIDTH = 800
WINDOWHEIGHT = 600
BGCOLOR = (50,0,50)
BALLCOLOR = (0, 255, 0)
BALLRADIUS = 20
	
def main():
	global FPSCLOCK, DISPLAYSURF
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	DISPLAYSURF.fill(BGCOLOR) 

	ball = Ball()
	while True:
		DISPLAYSURF.fill(BGCOLOR) 
		ball.update()		
		pygame.display.update()
		pygame.time.wait(10)
		FPSCLOCK.tick()
	
class Ball:
	x  = 0
	y  = 0
	color  = None
	radius = 0
	border = 0
	pressed = {}

	def __init__(self):
		self.x  = int(WINDOWWIDTH / 2)
		self.y  = int(WINDOWHEIGHT / 2)
		self.color  = BALLCOLOR
		self.radius = BALLRADIUS
		self.border = 0
		self.pressed = {K_UP: False, K_DOWN: False, K_LEFT: False, K_RIGHT: False}
		
	def ev(self):
		events = pygame.event.get()
		for ev in events:
			if ev.type == QUIT:
				pygame.quit()
				sys.exit()
			elif ev.type == KEYDOWN and ev.key in list(self.pressed.keys()):
				self.pressed[ev.key] = True
			elif ev.type == KEYUP and ev.key in list(self.pressed.keys()):
				self.pressed[ev.key] = False
		
	def move(self):
		self.x += self.pressed[K_RIGHT] - self.pressed[K_LEFT]
		self.y += self.pressed[K_DOWN] - self.pressed[K_UP]
		self.x %= WINDOWWIDTH
		self.y %= WINDOWHEIGHT
				
	def draw(self):
		pygame.draw.circle(DISPLAYSURF, self.color, (self.x, self.y), self.radius, self.border)
		
	def update(self):
		self.ev() 
		self.move() 
		self.draw()
	
if __name__ == "__main__":
	main()