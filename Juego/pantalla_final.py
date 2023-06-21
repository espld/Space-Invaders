import pygame
from juego_main import score_final

# Inicializar Pygame
pygame.init()

# Definir las dimensiones de la pantalla
ANCHO_VENTANA = 600
ALTO_VENTANA = 800

# Crear la pantalla
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

# Crear una variable para almacenar el puntaje total
score = score_final

# Crear una fuente de letra para el texto
font = pygame.font.Font(None, 36)

# Crear un objeto de texto a partir de la fuente y el puntaje total
text = font.render("Puntaje: " + str(score), True, (255, 255, 255))

# Dibujar el objeto de texto en la pantalla
screen.blit(text, (10, 10))

# Actualizar la pantalla
pygame.display.flip()

# Salir del juego
pygame.quit()