import pygame
from random import randint
BLACK = (0,0,0)
class Ball(pygame.sprite.Sprite):
	def __init__(self,color,width,height,v,u):
		super().__init__()


		self.image = pygame.Surface([width,height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)

		#drawing the ball
		pygame.draw.rect(self.image,color,[0,0,width,height])
		self.rect = self.image.get_rect()


		self.velocity = [v,u]

		# Fetch the rectangle object that has the dimensions of the image.
		self.rect = self.image.get_rect()


	def update(self):
			self.rect.x += self.velocity[0]
			self.rect.y += self.velocity[1]

	def bounce(self):
		self.velocity[0] = -self.velocity[0]
		self.velocity[1] = randint(-8, 8)

	def movement(self,player,p2,scoreA,scoreB):
		if self.rect.x >= 950:
			scoreA += 1
			self.velocity[0] = -self.velocity[0]
		if self.rect.x <= 0:
			scoreB += 1
			self.velocity[0] = -self.velocity[0]
		if self.rect.y > 710:
			self.velocity[1] = -self.velocity[1]
		if self.rect.y < 0:
			self.velocity[1] = -self.velocity[1]
		if pygame.sprite.collide_mask(self, player) or pygame.sprite.collide_mask(self, p2):
			self.velocity[0] = -self.velocity[0]
			self.velocity[1] = self.velocity[1]
