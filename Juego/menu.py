import pygame
from juego_main import juego
from boton import Boton
import colores
import base_datos
import sys

pygame.init()

 
clock = pygame.time.Clock()

ANCHO_VENTANA = 600
ALTO_VENTANA = 800

pygame.display.set_caption("MENU PRINCIPAL")
ventana = pygame.display.set_mode((600, 800),0,32)

fondo_galaxia = pygame.image.load("Juego\\bg.png") #subo la imagen de fondo

 
fuente = pygame.font.SysFont("Arial Narrow", 60)

 
def dibujar_texto(texto, fuente, color, ventana, x, y):
    texto_obj = fuente.render(texto, 1, color)
    texto_rect = texto_obj.get_rect()
    texto_rect.center = [x,y]
    ventana.blit(texto_obj, texto_rect)
 
click = False
 
def main_menu():
    while True:
 
        ventana.blit(fondo_galaxia,(0,0))
        dibujar_texto("SPACE INVADERS", fuente, (colores.COLOR_BLANCO), ventana,(ANCHO_VENTANA/2),50)
 
        boton_1 = Boton((ANCHO_VENTANA/4),250)
        boton_2 = Boton((ANCHO_VENTANA/4),350)
        boton_3 = Boton((ANCHO_VENTANA/4),450)
        boton_1.dibujar(ventana)
        boton_2.dibujar(ventana)
        boton_3.dibujar(ventana)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_1.chequeo_click():
                    juego()
                elif boton_2.chequeo_click():
                    base_datos.obtener_datos()
                elif boton_3.chequeo_click():
                    pygame.quit()
                    
        dibujar_texto("JUGAR", fuente, (colores.COLOR_BLANCO), ventana,(ANCHO_VENTANA/2),280)
        dibujar_texto("PUNTAJES", fuente, (colores.COLOR_BLANCO), ventana,(ANCHO_VENTANA/2),380)
        dibujar_texto("SALIR", fuente, (colores.COLOR_BLANCO), ventana,(ANCHO_VENTANA/2),480)

 
        pygame.display.update()
        clock.tick(60)
 
def puntajes():
    running = True
    while running:
        
        ventana.blit(fondo_galaxia,(0,0))
        dibujar_texto("PUNTAJES", fuente, (colores.COLOR_BLANCO), ventana,(ANCHO_VENTANA/2),50)

        rectangulo_scores = pygame.Rect((ANCHO_VENTANA/6,(ALTO_VENTANA/5)),(400,500))
        pygame.draw.rect(ventana, (colores.COLOR_AZUL), rectangulo_scores,2)

        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
        
        pygame.display.update()
        clock.tick(60)

main_menu()