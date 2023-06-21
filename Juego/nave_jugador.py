import pygame
import colores
from balas import Bala

ANCHO_VENTANA = 600


class Nave:

    def __init__(self,x,y) -> None:
        
        self.imagen_nave = pygame.image.load("Juego\spaceship.png")
        self.rect_nave = self.imagen_nave.get_rect()
        self.rect_nave.center = [x,y]
        self.velocidad = 10
        self.balas = []
        self.sonido_disparo = pygame.mixer.Sound("Juego\laser.wav")


    def update_nave(self):

        tecla = pygame.key.get_pressed()

        if tecla[pygame.K_a] and self.rect_nave.left > 0:
            self.rect_nave.x -= self.velocidad	
        if tecla[pygame.K_d] and self.rect_nave.right < ANCHO_VENTANA:
            self.rect_nave.x += self.velocidad
        

    def disparar(self):
        bala = Bala(self.rect_nave.centerx,self.rect_nave.top,"Juego\\bullet.png")
        self.balas.append(bala)
        self.sonido_disparo.play()


        


    def dibujar_nave(self,ventana):
        #pygame.draw.rect(ventana,colores.COLOR_VERDE,self.rect_nave)
        ventana.blit(self.imagen_nave,self.rect_nave)

        for bala in self.balas:
            bala.dibujar_bala(ventana)


    
        



    




    






        
    







    

    





