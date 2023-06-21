import pygame
import colores

class Bala:

    def __init__(self,x,y,imagen) -> None:

        self.imagen_bala = pygame.image.load(imagen)
        self.rect_bala = self.imagen_bala.get_rect()
        self.rect_bala.center = [x,y]
        
        
        self.velocidad_disparo = 5

    def update_bala_jugador(self):

        self.rect_bala.y -= self.velocidad_disparo

    def update_bala_enemigo(self):

        self.rect_bala.y += self.velocidad_disparo


    def dibujar_bala(self, ventana):
        pygame.draw.rect(ventana, colores.COLOR_ROJO, self.rect_bala)
        ventana.blit(self.imagen_bala,self.rect_bala)


