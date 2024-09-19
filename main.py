import pygame
from constants import *
from player import Player
def main():
    

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 #meaning Delta Time    
    PLAYER1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    



    print("Starting asteroids!")
    print (f'Screen width: {SCREEN_WIDTH}')
    print (f'Screen height: {SCREEN_HEIGHT}')
   
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        PLAYER1.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        print(clock)













if __name__ == '__main__':
    main()