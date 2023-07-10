import pygame
import colores
import re
from funciones import dibujar_texto
from base_datos import *


pygame.init()


ANCHO_VENTANA = 600
ALTO_VENTANA = 800


ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("GAME OVER")
fondo_galaxia = pygame.image.load("Juego\\bg.png")

fuente = pygame.font.SysFont("Arial Narrow", 30)

def juego_perdido(score):

    running = True
    nombre = ""
    while running:

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
            
                if re.match("[A-Z]", event.unicode) and len(nombre) < 3 :
                    nombre += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                
                elif event.key == pygame.K_RETURN:
                    running = False

        
        if running == False:
            insertar_puntajes(nombre, score)
        

        
        ventana.blit(fondo_galaxia,(0,0))


        dibujar_texto("Perdiste :(",fuente,colores.COLOR_BLANCO,ventana,ANCHO_VENTANA/2,100)

        dibujar_texto("Ingresa tu nombre[3 letras mayusculas]:",fuente,colores.COLOR_BLANCO,ventana,ANCHO_VENTANA/2,250)
        dibujar_texto(nombre,fuente,colores.COLOR_BLANCO,ventana,ANCHO_VENTANA/2,300)

      
        pygame.display.flip()
