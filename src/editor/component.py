import pygame

class Component:
    # CONSTRUCTOR
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self._mouse_in_bounds = False

    # EVENT HANDLING
    def on_mouse_move(self, x, y):
        pass

    def on_mouse_click(self, x, y, is_rmb):
        pass

    def on_mouse_enter(self):
        pass
    
    def on_mouse_exit(self):
        pass

    def get_bounds(self):
        return (self.x, self.y, self.width, self.height)

    # GAME LOOP
    def update(self, mouse_pos):
        last_mouse_in_bounds = self._mouse_in_bounds

        bounds = self.get_bounds()
        if bounds[0] <= mouse_pos[0] <= bounds[0] + bounds[2] \
            and bounds[1] <= mouse_pos[1] <= bounds[1] + bounds[3]:
            self._mouse_in_bounds = True
        else:
            self._mouse_in_bounds = False
        
        if self._mouse_in_bounds and not last_mouse_in_bounds:
            self.on_mouse_enter()

        if not self._mouse_in_bounds and last_mouse_in_bounds:
            self.on_mouse_exit()

    def render(self, screen):
        pass