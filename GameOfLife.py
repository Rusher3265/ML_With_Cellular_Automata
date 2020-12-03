import pygame



pygame.init()#initalize game

screenwidth=1000
screenheight=1000
screen=pygame.display.set_mode((screenwidth,screenheight))
#Declare variables
cellsize=10

#define colors
borders=(255,255,255)
aliveCell=(0,255,0)
deadCell=(0,0,0)

#define background
def draw_screen():
    screen.fill(deadCell)
    pygame.draw.rect(screen,aliveCell,(100,100,10,10))

# Run until the user asks to quit
running = True
while running:
    draw_screen()
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
