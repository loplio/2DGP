import random
from pico2d import *

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)
class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
class Ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(100, 700), 599
        self.frame = 0
        self.speed = random.randint(3, 7)

    def update(self):
        self.y -= self.speed
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 21, 0, 21, 21, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()
grass = Grass()
# boy = Boy()
team = [ Boy() for i in range(11)]
balls = [ Ball() for i in range(20)]
running = True
# game main loop code
while running:

    handle_events()
    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()
    # clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()

    delay(0.02)
# finalization code