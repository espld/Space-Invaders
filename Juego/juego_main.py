import pygame
import colores
from nave_jugador import Nave
from balas import Bala
from aliens import Alien
import random

pygame.init()

#defino ancho y alto de la ventana
ANCHO_VENTANA = 600 
ALTO_VENTANA = 800

clock = pygame.time.Clock()
fps = 60

ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA)) #creo la ventana
pygame.display.set_caption("SPACE INVADERS")

fuente = pygame.font.SysFont("Arial Narrow",40) #defino la fuenta a usar

fondo_galaxia = pygame.image.load("Juego\\bg.png") #subo la imagen de fondo

jugador = Nave((ANCHO_VENTANA/2),ALTO_VENTANA - 100) #instancio al jugador



lista_aliens_enemigos = [] #creo una lista de enemigos

#evento de disparo del enemigo
disparo_enemigo = pygame.USEREVENT + 1
pygame.time.set_timer(disparo_enemigo, 2000)




score = 0 #defino el score en 0

nivel = 0 #defino nivel
vidas = 5 #defino vidas del jugador

cantidad_enemigos = 0

perdido = False
countdown_perdido = 0



#defino una funcion para dibujar sobre la ventana
def dibujar_en_ventana():
	#dibujo fondo
	ventana.blit(fondo_galaxia,(0,0))


	#dibujo alien
	for alien in lista_aliens_enemigos:
		alien.dibujar_alien(ventana)



	#defino los textos
	texto_nivel = fuente.render(f"Nivel: {nivel}",True,(colores.COLOR_BLANCO))
	texto_vidas = fuente.render(f"Vidas: {vidas}",True,(colores.COLOR_BLANCO))
	texto_perdiste = fuente.render("perdiste!!!!",True,(colores.COLOR_BLANCO))
	texto_score = fuente.render(f"Score: {score}",True,(colores.COLOR_BLANCO))
	#dibujo fuente
	ventana.blit(texto_nivel,(10,10))
	ventana.blit(texto_vidas,(ANCHO_VENTANA - 120,10))
	ventana.blit(texto_score,(ANCHO_VENTANA/4,10))

	if perdido:
		ventana.blit(texto_perdiste,(ANCHO_VENTANA/2,300))

	#dibujo nave
	jugador.dibujar_nave(ventana)

	pygame.display.update()
	



running = True
while running:

	clock.tick(fps)
	dibujar_en_ventana()

	if vidas <= 0:
		perdido = True
		countdown_perdido += 1

	if perdido:
		if countdown_perdido > fps * 3:
			running = False
		else:
			continue

	if len(lista_aliens_enemigos) == 0:
		nivel += 1
		cantidad_enemigos += 3
		#instancio enemigos
		for alien in range(cantidad_enemigos):
			alien1 = Alien(random.randrange(50,600-100),random.randrange(-1500, -100),"Juego\\alien1.png",100)
			alien2 = Alien(random.randrange(50,600-100),random.randrange(-1500, -100),"Juego\\alien2.png",200)
			alien3 = Alien(random.randrange(50,600-100),random.randrange(-1500, -100),"Juego\\alien3.png",300)

			lista_aliens_enemigos.append(alien1)
			lista_aliens_enemigos.append(alien2)
			lista_aliens_enemigos.append(alien3)

				

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				jugador.disparar() #dispara el jugador
		if event.type == disparo_enemigo:
				alien.disparar() #dispara el enemigo


	

		
	# dibujo los rectangulos y el movimiento balas del jugador
	# y las elimino en caso de que se pase del alto de ventana o haya colision con un enemigo.
	if len(jugador.balas) > 0:
		for bala in jugador.balas:
			bala.dibujar_bala(ventana)
			bala.update_bala_jugador()

			if bala.rect_bala.top < -10 :
				jugador.balas.remove(bala)
			else:
				for alien in lista_aliens_enemigos:
					if bala.rect_bala.colliderect(alien.rect_alien):
						explosion = pygame.mixer.Sound("Juego\explosion.wav")
						explosion.play()
						score += alien.score
						jugador.balas.remove(bala)
						lista_aliens_enemigos.remove(alien)

	# dibujo a los enemigos y su movimiento. Si pasa del largo de la ventana o hay colision con la nave del jugador
	# se elimina y el jugador pierde una vida. Lo mismo con las balas del enemigo.
	if len(lista_aliens_enemigos) > 0:

		for alien in lista_aliens_enemigos:
			alien.update_aliens()
			if alien.rect_alien.top > ALTO_VENTANA or alien.rect_alien.colliderect(jugador.rect_nave):
				vidas -= 1
				lista_aliens_enemigos.remove(alien)

			"""if random.randrange(0,120) == 1:
				alien.disparar()"""

				
			if len(alien.balas) > 0:
				for bala in alien.balas:
					bala.dibujar_bala(ventana)
					bala.update_bala_enemigo()

					if bala.rect_bala.top > 900:
						alien.balas.remove(bala)
					elif bala.rect_bala.colliderect(jugador.rect_nave):
						vidas -= 1
						alien.balas.remove(bala)
				
				
			

	
	
	#movimiento nave
	jugador.update_nave()

	score_final = score

	pygame.display.flip()

pygame.quit()