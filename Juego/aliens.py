import pygame
import colores
from nave_jugador import Nave
from balas import Bala
import random


class Alien:

    def __init__(self,x,y,imagen,score) -> None:

        self.imagen_alien = pygame.image.load(imagen)
        self.rect_alien = self.imagen_alien.get_rect()
        self.rect_alien.center = [x,y]
        self.balas = []
        self.velocidad = random.randrange(2,3,1)
        self.score = score
        self.sonido_disparo = pygame.mixer.Sound("Juego\laser.wav")


    def update_aliens(self):

        self.rect_alien.y += self.velocidad

    def disparar(self):
        bala = Bala(self.rect_alien.centerx,self.rect_alien.bottom,"Juego\\alien_bullet.png")
        self.balas.append(bala)
        self.sonido_disparo.play()
        self.sonido_disparo.set_volume(0.3)



    def dibujar_alien(self,ventana):
        #pygame.draw.rect(ventana,colores.COLOR_VERDE,self.rect_alien)
        ventana.blit(self.imagen_alien,self.rect_alien)


        for bala in self.balas:
            bala.dibujar_bala(ventana)




    


