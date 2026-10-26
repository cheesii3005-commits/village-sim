import pygame
import sys
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        """Main game loop."""
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000.0  # Delta time for frame-independent movement
            self.events()
            self.update()
            self.draw()

    def events(self):
        """Handle user input and system events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

    def update(self):
        """Update game logic."""
        # TODO: Update entities, camera, and map logic here
        pass

    def draw(self):
        """Render the game to the screen."""
        self.screen.fill('black')  # Clear screen
        
        # TODO: Draw map, entities, and UI here
        
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()
