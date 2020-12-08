import pygame, sys, cte,os
from pygame.locals import *

class ObjetoMovil:
    def __init__(self, x=0, y=0, dx=4, dy=0, ancho=40, largo=40, color=cte.GREEN):
        self.imagen = ""
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.ancho = ancho
        self.largo = largo
        self.color = color

    def mueve_x(self):
        self.x += self.dx

    def mueve_y(self):
        self.y += self.dy

    def dibuja_rect(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.ancho, self.largo], 0)

    def check_fuera_pantalla(self):
        if self.x + self.ancho > cte.SCREEN_WIDTH or self.x < 0:
            self.x -= self.dx


def main():
    pygame.init()
    pygame.display.set_caption('Prueba de juego')  # nombre de la pantalla

    # La pantalla esta oculta, le damos dimensiones (tupla, no son dos args, solo es uno)
    global screen
    screen = pygame.display.set_mode((cte.SCREEN_WIDTH, cte.SCREEN_HEIGTH))
    screen.fill(cte.COLORFONDO)
    clock = pygame.time.Clock()  # creamos un reloj para asegurarse que nuestro prog se actualiza a una v fija

    # image_path = os.path.join('img','suelo.png')
    # fondo = pygame.image.load(image_path)
    os.environ['SLD_VIDEO_CENTERED'] = '1'

    # Creamos un objeto que se mueva para el jugador
    player = ObjetoMovil(900, 550, 0, 0, 70, 140, cte.RED)
    player.dibuja_rect()
    pygame.display.update()

    #llenamos es array de estanterias
    for i in range(cte.CUENTA_ESTANTERIAS):
        cte.ESTANTERIAS.append([0, cte.EST_Y])
        cte.EST_Y += cte.EST_ALTO + cte.ESPACIO

    '''el bucle principal del juego'''

    running = True
    while running:
        '''posibles entradas de teclado y mouse'''
        # screen.blit(fondo,(0,0))
        pygame.display.update()

        # Draw the stripes
        for i in range(cte.CUENTA_ESTANTERIAS):
            pygame.draw.rect(screen, cte.BROWN, [cte.ESTANTERIAS[i][0], cte.ESTANTERIAS[i][1], cte.EST_ANCHO, cte.EST_ALTO])
        # Move the stripes
        for i in range(cte.CUENTA_ESTANTERIAS):
            print(cte.ESTANTERIAS[i][1])
            cte.ESTANTERIAS[i][1] += 1
            if cte.ESTANTERIAS[i][1] > cte.SCREEN_HEIGTH:
                cte.ESTANTERIAS[i][1] = -500 - cte.EST_ALTO

        for event in pygame.event.get():
            pulsa = pygame.key.get_pressed()  # capturamos o evento
            if pulsa[K_LEFT] and player.x > 20:  # móvese a esquerda ata un borde da ventana
                player.x  -= player.dx
            if pulsa[K_RIGHT] and player.x < 950:  # moves a dereita ata o borde da ventana
                player.x += player.dx
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    main()
