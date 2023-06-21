import pygame

from asd import juego


pygame.init()

# Definir las dimensiones de la pantalla
width = 600
height = 800

# Crear la pantalla
screen = pygame.display.set_mode((width, height))

# Definir el color de fondo
bg_color = (255, 255, 255)

# Definir la fuente del texto
font = pygame.font.Font(None, 36)

# Crear el texto
text = font.render("Presione Enter para comenzar", True, (0, 0, 0))

# Obtener las dimensiones del texto
text_rect = text.get_rect()

# Centrar el texto en la pantalla
text_rect.center = (width // 2, height // 2)

# Mostrar el texto en la pantalla
screen.blit(text, text_rect)

# Actualizar la pantalla
pygame.display.flip()

# Esperar a que se presione la tecla Enter
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # Iniciar el juego
            juego()
            pygame.display.flip()

pygame.quit()