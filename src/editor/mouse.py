
class Mouse:
    """Stores the state of the mouse, including position and button states"""

    def __init__(self):
        # CONSTANTS
        self.BUTTON_LEFT = 1
        self.BUTTON_RIGHT = 3
        self.SCROLL_UP = 4
        self.SCROLL_DOWN = 5

        # CURRENT STATE
        self.x = 0
        self.y = 0
        self.left_button = False
        self.right_button = False
        self.dragging = False

        # PREVIOUS STATE
        self.prev_x = 0
        self.prev_y = 0
        self.prev_left_button = False
        self.prev_right_button = False

    def on_mouse_move(self, x, y):
        self.x = x
        self.y = y

    def on_mouse_down(self, x, y, button):
        self.x = x
        self.y = y
        if button == self.BUTTON_LEFT:
            self.left_button = True
        elif button == self.BUTTON_RIGHT:
            self.right_button = True

    def on_mouse_up(self, x, y, button):
        self.x = x
        self.y = y
        if button == self.BUTTON_LEFT:
            self.left_button = False
        elif button == self.BUTTON_RIGHT:
            self.right_button = False
    
    def update(self):
        self.prev_x = self.x
        self.prev_y = self.y
        self.prev_left_button = self.left_button
        self.prev_right_button = self.right_button