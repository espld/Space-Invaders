import pygame
from funciones import dibujar_texto
import colores
import base_datos



pygame.init()

 
clock = pygame.time.Clock()

ANCHO_VENTANA = 600
ALTO_VENTANA = 800

pygame.display.set_caption("PUNTAJES")
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

fondo_galaxia = pygame.image.load("Juego\\bg.png") #subo la imagen de fondo

 
fuente = pygame.font.SysFont("Arial Narrow", 60)






def puntajes():

    puntajes = base_datos.obtener_datos()



    running = True

    while running:
        
        ventana.blit(fondo_galaxia,(0,0))
        dibujar_texto("PUNTAJES MAXIMOS", fuente, (colores.COLOR_BLANCO), ventana,(ANCHO_VENTANA/2),50)

        for i, valor in enumerate(puntajes):
            texto = fuente.render(f"{valor[1]}     {valor[2]}", True, (colores.COLOR_BLANCO))
            rect_texto = texto.get_rect()
            rect_texto.center = (ANCHO_VENTANA/2, 250 + i * 65)
            ventana.blit(texto, rect_texto)


        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        clock.tick(60)