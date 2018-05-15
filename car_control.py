import pygame
import socket
def send(speed,rot,log="00"):
    s = socket.socket()
    s.connect(('172.24.1.1', 1080))
    s.send('{}/{}/{}'.format(log,str(1500+int(speed)*5),str(int(rot))).encode("utf-8"))
    s.close()

pygame.init()
pygame.font.init()
run = True
size = width, height = 300,300
screen = pygame.display.set_mode(size)
center = width//2,height//2
clock = pygame.time.Clock()
spd = 0
deltaspd = 0
deltarot = 0
rot = 90
while run:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                deltaspd=-0.1
            if event.key == pygame.K_DOWN:
                deltaspd=0.1
            if event.key == pygame.K_LEFT:
                deltarot+=0.1
            if event.key == pygame.K_RIGHT:
                deltarot-=0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                deltaspd = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                deltarot = 0
    spd+=deltaspd
    if rot > 70 and rot < 150:
        rot+=deltarot
    if abs(spd) >30:
        spd = 30 if spd > 0 else -30
    send(spd,rot)
    font = pygame.font.SysFont("comicsansms", 20)
    screen.blit(font.render("Скорость: "+str(spd), True, pygame.Color("white")),(0,0))
    screen.blit(font.render("Поворот: " + str(rot), True, pygame.Color("white")), (0, 40))
    pygame.display.flip()
send(1500,90,"11")
