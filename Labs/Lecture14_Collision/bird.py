import game_framework
import random
from pico2d import *

import game_world
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Bird:

    def __init__(self):
        self.x, self.y = random.randint(100, 1500) // 2, random.randint(200, 500)
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('bird100x100x14.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = random.randint(80, 150)
        self.frame = 0
        self.event_que = []

    def get_bb(self):
        # fill here
        return 0, 0, 0, 0

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.velocity * game_framework.frame_time
        self.x = clamp(25, self.x, 1600 - 25)
        print(self.x)
        if self.x > 1500:
            print(self.velocity)
            self.velocity *= -1
            self.x = 1450
        elif self.x < 0:
            self.velocity *= -1
            self.x = 100
        # self.cur_state.do(self)
        # if len(self.event_que) > 0:
        #     event = self.event_que.pop()

    def draw(self):
        # if self.dir == 1:
        #     self.image.clip_draw(int(self.frame) * 100, 100, 100, 100, self.x, self.y)
        # else:
            self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        # self.cur_state.draw(self)
        # self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        #fill here
