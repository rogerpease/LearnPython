import pygame; 

(width, height) = (400, 300)
screen = pygame.display.set_mode((width, height))
WHITE=(255,255,255)
BLUE=(0,0,255)
YELLOW = (255,255,32)
screen.fill(WHITE)

flipRectangle = pygame.draw.rect(screen,YELLOW,(200, 50,100,50)) 
quitRectangle = pygame.draw.rect(screen,YELLOW,(200,150,100,50))

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.

myfont = pygame.font.SysFont('Comic Sans MS', 30)
flipTextSurface = myfont.render("Flip", False, (0, 0, 0))
screen.blit(flipTextSurface,(210,60))
quitTextSurface = myfont.render("Quit", False, (255,0,0))
screen.blit(quitTextSurface,(210,160))
coinTextSurface = myfont.render("Heads", False, (255,0,0))
screen.blit(coinTextSurface,(100,150))


pygame.display.flip()
while True: 
    for evnt in pygame.event.get():
      if evnt.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        print (pos) 
    pygame.display.flip()
    pass






#coinCircle = pygame.draw.circle(screen,YELLOW,(200,50),40)
#       if (pos[0] > 200): 
#         print ("Right side")
#	else 
#         print ("Left side")
#        if quitRectangle.collidepoint(pos):
#          print ("Quit") 
