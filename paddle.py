import pygame
RED = (0,0,0)
class Paddle(pygame.sprite.Sprite):
	def __init__(self,color,width,height):
		super().__init__()


		self.image = pygame.Surface([width,height])
		self.image.fill(RED)
		self.image.set_colorkey(RED)

		#drawing the paddle
		pygame.draw.rect(self.image,color,[0,0,width,height])
		self.rect = self.image.get_rect()
	def moveUp(self,pixels):
		self.rect.y -= pixels
		#to check if the paddle does not go off the screen
		if self.rect.y < 0 :
			self.rect.y = 0
	def moveDown(self,pixels):
		self.rect.y += pixels
		#to check if the paddle does not go off the screen
		if self.rect.y > 620 :
			self.rect.y = 620
	def paddle_movement(self):
			keys = pygame.key.get_pressed()
			# Player A
			if keys[pygame.K_UP]:
				self.moveUp(15)
			if keys[pygame.K_DOWN]:
				self.moveDown(15)

