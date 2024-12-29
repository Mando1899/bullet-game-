import pygame, random

class Bullet:
    def __init__(self, game, pos, size):
        self.game = game
        self.size = size
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

    def render(self, surf):
        img = self.game.assets['bullet']
        img = pygame.transform.scale(img, self.size)
        surf.blit(img, (self.rect.x, self.rect.y))
    def check_col(self):
        if self.rect.colliderect(self.game.player.rect):
            self.game.player.player_bullets += 1
            return True
        else:
            return False

class Bullets:
    def __init__(self, game) :
        self.game = game
        self.bullets = self.spawn_bullets()

    def spawn_bullets(self, bullets_num=3):
        bullet_list = []
        for bullet in range(bullets_num):
            bullet_pos = [random.randrange(25, 375), random.randrange(25, 375)]
            bullet_list.append(Bullet(self.game, bullet_pos, [20, 25]))
        return bullet_list
    
    def update(self):
        for bullet in self.bullets:
            if bullet.check_col():
                
                self.bullets = self.spawn_bullets(random.randrange(3,5))

    def render(self, surf):
    
        for bullet in self.bullets:
            bullet.render(surf)
