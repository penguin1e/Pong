import pygame, sys, random
from pygame.locals import QUIT



pygame.init()
clock = pygame.time.Clock()
screens = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
paddle=pygame.Rect(10,115,10,60)
paddle2=pygame.Rect(379,115,10,60)
ball=pygame.Rect(187,135,10,10)
paddletopboundary=(0)
paddlebottomboundary=(240)
balltopboundary=(0)
ballbottomboundary=(290)
balleftboundary=(0)
ballrightboundary=(390)
ballup=True
balleft=True
run=True
paddlespeed=2
s1=0
s2=0
winner=""
font=pygame.font.SysFont("arial",30)
scoretext=font.render("0 | 0",False,(0,0,0))
winnertext=font.render(winner+" wins",False,(0,0,0))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys=pygame.key.get_pressed()
    if run:
        if keys[pygame.K_UP]:
            paddle2.y-=paddlespeed
            if paddle2.y<=paddletopboundary:
                paddle2.y=paddletopboundary
        if keys[pygame.K_DOWN]:
            paddle2.y+=paddlespeed
            if paddle2.y>=paddlebottomboundary:
                paddle2.y=paddlebottomboundary
        if keys[pygame.K_w]:
            paddle.y-=paddlespeed
            if paddle.y<=paddletopboundary:
                paddle.y=paddletopboundary
        if keys[pygame.K_s]:
            paddle.y+=paddlespeed
            if paddle.y>=paddlebottomboundary:
                paddle.y=paddlebottomboundary
    else:
        if keys[pygame.K_SPACE]:
            paddle.y=(115)
            paddle2.y=(115)
            ball.x=(187)
            ball.y=(135)
            run=True
    
        
    screens.fill("white")
    pygame.draw.rect(screens,"black",paddle)
    pygame.draw.rect(screens,"black",paddle2)
    pygame.draw.rect(screens,"black",ball)
    if run:
        scoretext=font.render(f"{s1} | {s2}",False,(0,0,0))
        screens.blit(scoretext,(150,0))
        # move y
        if ballup==True:
            ball.y-=2
        if ballup==False:
            ball.y+=2
        # move down
        if ball.y<=balltopboundary:
            ballup=False
            ball.y=balltopboundary
        # move up
        if ball.y>=ballbottomboundary:
            ballup=True
            ball.y=ballbottomboundary
        # move x
        if balleft==True:
            ball.x-=2
        if balleft==False:
            ball.x+=2
        # move left wall
        if ball.x<=balleftboundary:
            balleft=False
            ball.x=balleftboundary
            run=False
        if ball.x>=ballrightboundary:
            ball.x=ballrightboundary
            run=False
        
        # collide ball with paddles
        if ball.colliderect(paddle):
            balleft=False
        if ball.colliderect(paddle2):
            balleft=True
        # score
        if ball.x<=balleftboundary:
            s2+=1
        if ball.x>=ballrightboundary:
            s1+=1       
        if s1==10 or s2==10:
            run=False
        # winner
    else:
        if s1>=10 and s1>s2:
            winner="Player 1"
            print(winner+" wins.")
            winnertext=font.render(winner+" wins",False,(0,0,0))
            screens.blit(winnertext,(100,40))

        if s2>=10 and s2>s1:
            winner="Player 2"
            print(winner+" wins.")
            winnertext=font.render(winner+" wins.",False,(0,0,0))
            screens.blit(winnertext,(100,40))

        screens.blit(scoretext,(150,0))
        


    
    pygame.display.update()
    clock.tick(60) 
