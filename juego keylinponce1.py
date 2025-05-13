





#sudo dpkg --configure -a
#sudo apt-get install python3-pygame

import math
import random
import pygame

from pygame import mixer

# inicio del juego
pygame.int()

# se crea el fondo de pantalla
screen = pygame.display.set_mode((10000,800))

# fondo de pantalla 
backgroud = pygame.image.load('/home/computadora-12/Descargas/juego 1 keylin ponce/fondo1.png.jpg')

# sonido de fondo
mixer.music.load('/home/computadora-12/Descargas/juego 1 keylin ponce/UTF-8background.wav')
mixer.music.play(-1 )

# titulo y icono
pygame.display.set_caption("perdidos en ")
icon = pygame.image.load('/home/computadora-12/Descargas/juego 1 keylin ponce/enemigo1-removebg-preview.png')
pygame.display.set_icon(icon)

# jugador 
PlayerImg=pygame.image.load('/home/computadora-12/Descargas/juego 1 keylin ponce/personaje-removebg-preview.pn')
playerX= 370
playery= 480
playerX_change=0

# enemigos
enemyImg=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
num_of_enemies= 20

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('/home/computadora-12/Descargas/juego 1 keylin ponce/enemigo2-removebg-preview.png'))
    enemyx.append(random.randint(0.736))
    enemyy.append(random.randint(50,150))
    enemyx_change.append(4)
    enemyy_change.append(40)

# disparo

armaImg= pygame.image.load('/home/computadora-12/Descargas/juego 1 keylin ponce/bala.png-removebg-preview.png')
armax=0
armayy=480
armax_change=0
armay_change=10
arma_estado="ready"

# puntaje

score_value=0
font =pygame.font.font('freesansbold.ttf',32)


textx=10
texty=10

# juego terminado
over_font =pygame.font.font('freesansbold.ttf',64)

def show_puntuaje(x,y):
    score=font. render("score : "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
def gameover_text():
    over_text= over_font.render("GAME OVER", True,  (255, 255, 255))
def player(x, y):
    screen.blit(playerimg, (x, y))
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
def iniciar_disparo (x, y):
    global arma_estado
    arma_estado = "Fire"
    screen.blit(armaImg, (x+16,y+10))
def iscollison(enemyX,enemyY,armaX,armaY):
    distance = math.sqrt(math.pow(enemyX - armaX, 2) + (math.pow(enemyY-armaY,2)))
    if distance < 27:
        return True
    else:
        return False

# ciclo de juego
running = True 
while running: 
    screen.fill((0,0,0))
    # imagen de fondo
    screen.blit(backgroud, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running =False


            # si presiona 
            if event.type == pygame.KEYDOWN:

              if event.key == pygame.K_LEFT:
                playerX_change = -5
              if event.key == pygame.K_RIGHT:
                playerX_change = 5
              if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(armax, armayy)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyy[i] > 440:
            for j in range(num_of_enemies):
                enemyy[j] = 2000
            game_over_text()
            break

        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 4
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -4
            enemyy[i] += enemyy_change[i]

        # Collision
        collision = iscollision(enemyx[i], enemyy[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion.wav")
            explosionSound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyx[i] = random.randint(0, 736)
            enemyy[i] = random.randint(50, 150)

        enemy(enemyx[i], enemyy[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= armay_change

    player(playerX, playery)
    show_score(textx, testy)
    pygame.display.update()