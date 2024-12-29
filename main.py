import pygame, sys
from player import Player
from bullet import Bullets
from utils import draw_text

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('bullet game')
        self.screen = pygame.display.set_mode((800, 800))
        self.display = pygame.surface.Surface((400, 400))
        self.clock = pygame.time.Clock()
        self.mpos = [0,0]
        self.player = Player((155, 110), (23,28), self)
        self.assets = {
            'player' : pygame.image.load('images\Logo.png'),
            'gun' : pygame.image.load('images\Gun.png').convert_alpha(),
            'bullet' : pygame.image.load('images\Bullet.png')
        }
        self.bullets = Bullets(self)
        self.text_font = pygame.font.SysFont('Arial', 100)


    
        
    def run(self):
        while True:
            self.display.fill((255, 255, 255))
            draw_text(self.player.get_bullet_num(), self.text_font, (0, 0, 0), 150, 140, self.display)
            self.mpos = list(pygame.mouse.get_pos()) 
            
            self.bullets.render(self.display)
            self.bullets.update()
            self.player.draw(self.display, self.mpos)
            self.player.update()
            if self.player.rect.y > 450:
                self.reset_game()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # self.player.applay_recoil(self.mpos)
                    if self.player.player_bullets != 0:
                        self.player.applay_recoil(self.mpos)
                        self.player.player_bullets -= 1
                
            


            self.clock.tick(60)


            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
    def reset_game(self):
        self.player = Player((155, 110), (23,28), self)
        self.bullets = Bullets(self)
                


game = Game()
game.run()