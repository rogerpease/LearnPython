import pygame; 
import sys; 

(width, height) = (400, 300)
screen = pygame.display.set_mode((width, height))

WHITE  = (255,255,255)
BLUE   = (  0,  0,255)
YELLOW = (255,255, 32)
SILVER = (192,192,192)

screen.fill(WHITE)

flipRectangle = pygame.draw.rect(screen,YELLOW,(200, 50,100,50)) 
quitRectangle = pygame.draw.rect(screen,YELLOW,(200,150,100,50))
coinCircle    = pygame.draw.circle(screen,SILVER,(100,150),50)

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.

myfont = pygame.font.SysFont('Comic Sans MS', 30)
flipTextSurface = myfont.render("Flip", False, (0, 0, 0))
screen.blit(flipTextSurface,(210,60))
quitTextSurface = myfont.render("Quit", False, (255,0,0))
screen.blit(quitTextSurface,(210,160))
coinTextSurface = myfont.render("Heads", False, (255,0,0))

coinTextCorner = (78,138)
screen.blit(coinTextSurface,coinTextCorner)


pygame.display.flip()
while True: 
    for evnt in pygame.event.get():
      if evnt.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        print (pos)
        if flipRectangle.collidepoint(pos):
          coinTextSurface = myfont.render("Tails", False,(255,0,0))
          coinCircle    = pygame.draw.circle(screen,SILVER,(100,150),50)
          screen.blit(coinTextSurface,coinTextCorner)
        if quitRectangle.collidepoint(pos):
          print ("Quit") 
          sys.exit()

    pygame.display.flip()
    pass

# TODO: Add Tails/Heads
# TODO: Animate Tails/Heads or pull picture from internet of quarter. 
# 23 Jul 2019: Added Coin body and over-drew coin on reflip. 
   
