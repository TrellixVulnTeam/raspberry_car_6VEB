import pygame
import socket
def send(speed,rot):
    s.send(bytes('00/{}/{}'.format(str(1500+int(speed)*50),str(int(rot)))))
pygame.init()
pygame.font.init()
run = True
s = socket.socket()
s.connect(('172.24.1.1', 1080))
size = width, height = 300,300
screen = pygame.display.set_mode(size)
center = width//2,height//2
clock = pygame.time.Clock()
spd = 0
rot = 90
while run:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                spd+=1
            if event.key == pygame.K_DOWN:
                spd-=1
            if event.key == pygame.K_LEFT:
                rot+=1
            if event.key == pygame.K_RIGHT:
                rot-=1
    send(spd,rot)
    font = pygame.font.SysFont("comicsansms", 20)
    screen.blit(font.render("Скорость: "+str(spd), True, pygame.Color("white")),(0,0))
    screen.blit(font.render("Поворот: " + str(rot), True, pygame.Color("white")), (0, 0))
    pygame.display.flip()
s.close()