import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from grass import Grass
from ball import Ball


name = "MainState"

boy = None
grass = None

def enter():
    global boy
    boy = Boy()
    grass = Grass()
    game_world.add_object(grass, 0)
    game_world.add_object(boy, 1)


def exit():
    global boy, grass
    del boy
    del grass
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()
    # boy.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    # grass.draw()
    # boy.draw()
    update_canvas()







