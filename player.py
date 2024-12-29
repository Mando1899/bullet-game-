import pygame, math
from utils import mag_vector

    

class Player:
    def __init__(self, pos, size, game):
        self.size = size
        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.game = game
        self.velocity = [0,0]
        self.recoil = [0, 0]
        self.gun_angle = 0
        self.player_bullets = 5
        
    def update(self):
        self.velocity[1] += 0.09
        self.velocity = self.recoil
        
        #frame_movement = [self.velocity[0], self.velocity[1]]
        
        self.rect.x += self.velocity[0]
        self.rect.y +=  self.velocity[1]
         
        if self.rect.x > 400 - self.size[0] + 5 :
            self.rect.x -= 2
            self.velocity[0] = -self.velocity[0]
        if self.rect.x < 0:
            self.velocity[0] = -self.velocity[0]
            self.rect.x += 2
            

    def draw(self, surf, mpos):
        surf.blit(pygame.transform.scale(self.game.assets['player'], (26, 31)), [self.rect.x, self.rect.y])
        gun_img = self.game.assets['gun']
        gun_img.set_colorkey((0,0,0))
        gun_img = pygame.transform.scale(gun_img, (100, 100))
        gun_img_offset = [11,24]
        distance = [(self.rect.centerx - mpos[0] / 2) , (self.rect.centery - mpos[1] / 2)]
        self.gun_angle = math.degrees(math.atan2(distance[0], distance[1])) + 90
        rotated_gun_img = pygame.transform.rotate(gun_img, self.gun_angle)
        surf.blit(rotated_gun_img, [self.rect.x + gun_img_offset[0] - rotated_gun_img.get_height() / 2, self.rect.y + gun_img_offset[1]- rotated_gun_img.get_width()/2])

    

    def applay_recoil(self, mpos):
        vector = [(self.rect.centerx - mpos[0] / 2) / 50, (self.rect.centery - mpos[1] / 2) / 50]
        self.recoil = mag_vector(vector, mag=2.5)

    def reset_player(self):
        self.player_bullets = 5
        self.velocity = [0,0]
        self.rect.x, self.rect.y =  155, 110

    def get_bullet_num(self):
        return str(self.player_bullets)
