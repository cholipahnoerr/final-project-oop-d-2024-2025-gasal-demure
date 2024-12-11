import pygame as pg
from abc import ABC, abstractmethod

class AnimatedSprite(pg.sprite.Sprite, ABC):
    def __init__(self, scale_factor):
        super(AnimatedSprite, self).__init__()
        self.img_list = self.load_images(scale_factor)
        self.image_index = 0
        self.image = self.img_list[self.image_index]
        self.rect = self.image.get_rect(center=(100, 100))
        self.anim_counter = 0

    @abstractmethod 
    def load_images(self, scale_factor):
        pass

    def play_animation(self):
        if self.anim_counter == 5:
            self.image = self.img_list[self.image_index]
            self.image_index = 1 - self.image_index
            self.anim_counter = 0
        self.anim_counter += 1

class Bird(AnimatedSprite):
    def __init__(self, scale_factor):
        super(Bird, self).__init__(scale_factor)
        self.y_velocity = 0
        self.gravity = 10
        self.flap_speed = 250
        self.update_on = False

    def load_images(self, scale_factor):
        return [
            pg.transform.scale_by(pg.image.load("assets/birdup.png").convert_alpha(), scale_factor),
            pg.transform.scale_by(pg.image.load("assets/birddown.png").convert_alpha(), scale_factor)
        ]

    def update(self, dt):
        if self.update_on:
            self.play_animation()
            self.apply_gravity(dt)
            self.check_boundaries()

    def apply_gravity(self, dt):
        self.y_velocity += self.gravity * dt
        self.rect.y += self.y_velocity

    def flap(self, dt):
        self.y_velocity = -self.flap_speed * dt

    def check_boundaries(self):
        if self.rect.y <= 0 and self.flap_speed == 250:
            self.rect.y = 0
            self.flap_speed = 0
            self.y_velocity = 0
        elif self.rect.y > 0 and self.flap_speed == 0:
            self.flap_speed = 250

    def reset(self):
        self.rect.center = (100, 100)
        self.y_velocity = 0
        self.update_on = False