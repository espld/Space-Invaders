import pygame
import re

pygame.init()



def dibujar_texto(texto, fuente, color, ventana, x, y):
    texto_obj = fuente.render(texto, 1, color)
    texto_rect = texto_obj.get_rect()
    texto_rect.center = [x,y]
    ventana.blit(texto_obj, texto_rect)



def preguntar_nombre():

    flag = True

    while flag == True:

        opcion_elegida = input("ingrese su nombre [3 letras]: ")

        if re.match("[a-zA-Z]{3}$", opcion_elegida):
	    
            resultado = opcion_elegida
	    
            flag = False
	    
        else:
            resultado = print("Opcion no valida")

    return resultado




