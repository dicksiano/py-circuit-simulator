import pygame

class Bounds:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def to_tuple(self):
        return (self.x, self.y, self.width, self.height)

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

    def on_mouse_click(self, x, y, button):
        pass

    def on_mouse_enter(self):
        pass
    
    def on_mouse_exit(self):
        pass

    def get_bounds(self):
        return Bounds(self.x, self.y, self.width, self.height)

    # GAME LOOP
    def update(self, mouse):
        last_mouse_in_bounds = self._mouse_in_bounds

        bounds = self.get_bounds()
        if bounds.x <= mouse.x <= bounds.x + bounds.width \
            and bounds.y <= mouse.y <= bounds.y + bounds.height:
            mouse_in_bounds = True
        else:
            mouse_in_bounds = False

        self._mouse_in_bounds = mouse_in_bounds    
        
        if mouse_in_bounds and not last_mouse_in_bounds:
            self.on_mouse_enter()
        if not mouse_in_bounds and last_mouse_in_bounds:
            self.on_mouse_exit()
        
        if mouse_in_bounds:
            if mouse.left_button and not mouse.prev_left_button:
                self.on_mouse_click(mouse.x, mouse.y, mouse.BUTTON_LEFT)
            if mouse.right_button and not mouse.prev_right_button:
                self.on_mouse_click(mouse.x, mouse.y, mouse.BUTTON_RIGHT)

    def render(self, screen):
        pass