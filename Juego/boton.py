import pygame
import colores

ANCHO_VENTANA = 600
ALTO_VENTANA = 800


class Boton():

	def __init__(self,x,y,):
		self.imagen_rect = pygame.image.load("Juego\\bg.png")
		self.x = x
		self.y = y
		self.rect_boton = pygame.Rect((self.x,self.y),(300,60))

	def dibujar(self,ventana):
		
		#pygame.draw.rect(ventana,colores.COLOR_VERDE,self.rect_boton)
		ventana.blit(self.imagen_rect,self.rect_boton)

	def chequeo_click(self):
		if self.rect_boton.collidepoint(pygame.mouse.get_pos()):
			return True
		else:
			return False




	
		




