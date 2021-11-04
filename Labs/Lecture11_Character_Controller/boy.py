from pico2d import *

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, DASH_ON, DASH_OFF, SLEEP_TIMER, DASH_TIMER = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_RSHIFT): DASH_ON,
    (SDL_KEYDOWN, SDLK_LSHIFT): DASH_ON,
    (SDL_KEYUP, SDLK_RSHIFT): DASH_OFF,
    (SDL_KEYUP, SDLK_LSHIFT): DASH_OFF
}
# fill here
class IdleState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.timer = 1000

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)

class RunState:
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity = 1
        elif event == LEFT_DOWN:
            boy.velocity = -1
        elif event == RIGHT_UP:
            boy.velocity = -1
        elif event == LEFT_UP:
            boy.velocity = 1
        if boy.velocity > 1:
            boy.velocity //= 2
        elif boy.velocity < -1:
            boy.velocity = -(boy.velocity//-2)
        boy.dir = boy.velocity

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 - 25)

    def draw(boy):
        if boy.dir > 0:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)

class DashState:
    def enter(boy, event):
        if boy.dir > 0:
            boy.velocity = 2.5
        elif boy.dir < 0:
            boy.velocity = -2.5
        boy.timer = 130
        pass
    def exit(boy, event):
        pass
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        print(boy.timer)
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 800 - 25)
        if boy.timer == 0:
            boy.add_event(DASH_TIMER)
        pass
    def draw(boy):
        if boy.dir > 0:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)

class Boy:
    def __init__(self):
        self.x, self.y = 800 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.timer = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

# Boy States
class SleepState:

    def enter(boy, event):
        boy.frame = 0

    def exit(boy, event):
        pass

    def do(boy):
        boy.frame = (boy.frame + 1) % 8

    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100,
                                          3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100,
                                          -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)

# fill here

next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState,
                RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                SLEEP_TIMER: SleepState, DASH_ON: IdleState, DASH_OFF: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
               LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               DASH_ON: DashState, DASH_OFF: RunState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState,
                 LEFT_UP: RunState, RIGHT_UP: RunState, DASH_ON: SleepState, DASH_OFF: SleepState},
    DashState: {RIGHT_UP: IdleState, LEFT_UP: IdleState,
                LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
                DASH_TIMER: RunState, DASH_ON: DashState, DASH_OFF: RunState}
}