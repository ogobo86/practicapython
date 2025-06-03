import pygame
import random
import math
from pygame import mixer


# Inicializar  pygame
pygame.init()

# Se asigna el tama de pantalla
pantalla = pygame.display.set_mode((800,600))

# Titulo e icono
pygame.display.set_caption("Invasion Espacial") # Modifica el nombre de pantalla. 
icono = pygame.image.load("C:\Curso\practicapython\Invasion\ovni.png") #ruta en donde se encuentra el icono
pygame.display.set_icon(icono) 
fondo = pygame.image.load("C:\Curso\practicapython\Invasion\space.jpg")

# Agregar musica
mixer.music.load('C:\Curso\practicapython\Invasion\MusicaFondo.mp3')
mixer.music.set_volume(0.3)
mixer.music.play(-1)


# Jugador
img_jugador = pygame.image.load("C:\Curso\practicapython\Invasion\\astronave.png")
jugador_x = 368
jugador_y = 520
jugador_x_cambio = 0

# Enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append (pygame.image.load("C:\Curso\practicapython\Invasion\enemigo.png"))
    enemigo_x.append (random.randint(0,736))
    enemigo_y.append (random.randint(50, 200))
    enemigo_x_cambio.append (0.4)
    enemigo_y_cambio.append (30)

# Bala
img_bala = pygame.image.load("C:\Curso\practicapython\Invasion\\bala.png")
bala_x = 0
bala_y = 520
bala_x_cambio = 0
bala_y_cambio = 0.9 
bala_visible = False

# Marcador 
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 34)
texto_x = 10
texto_y = 10

# Texto Final de juego
fuente_final = pygame.font.Font('freesansbold.ttf', 40)

def texto_final():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO", True, (255,255,255))
    pantalla.blit(mi_fuente_final, (200,200)) # X, Y



# Funcion mostrar puntaje
def mostrar_puntaje(x,y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255,255,255))
    pantalla.blit(texto, (x,y))

#  Funcion Jugador
def jugador(x,y):
    pantalla.blit(img_jugador, (x, y)) #Manda posicionamiento en pantalla

#  Funcion Enemigo
def enemigo(x,y, ene):
    pantalla.blit(img_enemigo[ene], (x, y)) #Manda posicionamiento en pantalla

# Funcion Disparar Bala
def disparar_bala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

# Funcion detectar Colicion
def hay_colision(x_1, y_1, x_2, y_2 ):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow (y_2 - y_1, 2)) # Calcula la distancia
    if distancia < 27:
        return True
    else:
        return False

# Loop del juego (eventos)
se_ejecuta = True
while se_ejecuta:
    # Importante tener esto al principio
    pantalla.blit(fondo, (0,0))

    # Iterar eventos
    for evento in pygame.event.get():
        # Evento para cerrar la pantalla.
        if evento.type == pygame.QUIT:  
            se_ejecuta = False
        
        # Evento de movimiento 
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.1 # se mueve a la izquierda
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.1 # se mueve a la derecha
            if evento.key == pygame.K_SPACE:# Movimiento de bala
                sonido_bala= mixer.Sound('C:\Curso\practicapython\Invasion\disparo.mp3')
                sonido_bala.play ()
                if not bala_visible: # Evita el redireccionamiento al presionar space rapido. 
                    bala_x = jugador_x # Toma el valor del jugador en pantalla
                    disparar_bala(bala_x, bala_y)

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0 # mantiene posicionamiento
            

    # Se asigna ubicacion del jugador
    jugador_x += jugador_x_cambio 

    # Limitar bordes jugador 
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x > 736:
        jugador_x = 736

    # Se asigna ubicacion del enemigo
    for e in range(cantidad_enemigos):

        # Fin del juego 
        if enemigo_y[e] > 500:
            for k  in range(cantidad_enemigos):
                enemigo_y[k]= 1000
            texto_final()
            break

        enemigo_x[e]+= enemigo_x_cambio [e]
        # Limitar bordes enemigo 
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] > 736:
            enemigo_x_cambio[e] = -0.1
            enemigo_y[e] += enemigo_y_cambio[e]
        # Colision
        colision = hay_colision (enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('C:\Curso\practicapython\Invasion\golpe.mp3')
            sonido_colision.play()
            bala_y = 500 # restablece la ubicacion de bala.
            bala_visible = False 
            puntaje += 1
            # Hace que vuelva a parecer un enemigo en pantalla.
            enemigo_x[e] = random.randint(0,736)
            enemigo_y[e] = random.randint(50, 200)
        enemigo (enemigo_x[e], enemigo_y[e], e)


    # Movimiento bala
    if bala_y <= -64:
        bala_y = 520
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    
    jugador(jugador_x, jugador_y)
    
    # Mostrar puntaje
    mostrar_puntaje(texto_x, texto_y)

    # Actulizar
    pygame.display.update()