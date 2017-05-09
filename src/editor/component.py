class Component:
    """Abstract class for objects that are drawn on the screen and interact with the mouse"""

    # CONSTRUCTOR
    def __init__(self, x, y, width, height, editor):
        self.editor = editor
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.mouse_hover = False
        self._mouse_dragging = False

    # EVENT HANDLING
    def on_mouse_move(self, x, y):
        pass

    def on_mouse_click(self, x, y, button):
        pass

    def on_mouse_down(self, x, y, button):
        pass

    def on_mouse_up(self, x, y, button):
        pass

    def on_mouse_drag(self, x, y):
        pass

    def on_mouse_enter(self):
        pass
    
    def on_mouse_exit(self):
        pass

    # GAME LOOP
    def update(self, mouse):
        last_mouse_in_bounds = self.mouse_hover

        if self.x <= mouse.x < self.x + self.width \
            and self.y <= mouse.y < self.y + self.height:
            mouse_in_bounds = True
        else:
            mouse_in_bounds = False
        self.mouse_hover = mouse_in_bounds    
        
        if mouse_in_bounds and not last_mouse_in_bounds:
            self.on_mouse_enter()
        if not mouse_in_bounds and last_mouse_in_bounds:
            self.on_mouse_exit()
        
        if mouse_in_bounds:
            if mouse.left_button and not mouse.prev_left_button:
                self.on_mouse_down(mouse.x, mouse.y, mouse.BUTTON_LEFT)
            if mouse.right_button and not mouse.prev_right_button:
                self.on_mouse_down(mouse.x, mouse.y, mouse.BUTTON_RIGHT)

            if mouse.left_button and not mouse.prev_left_button:
                self.on_mouse_click(mouse.x, mouse.y, mouse.BUTTON_LEFT)
            if mouse.right_button and not mouse.prev_right_button:
                self.on_mouse_click(mouse.x, mouse.y, mouse.BUTTON_RIGHT)

            if not mouse.left_button and mouse.prev_left_button:
                self.on_mouse_up(mouse.x, mouse.y, mouse.BUTTON_LEFT)
            if not mouse.right_button and mouse.prev_right_button:
                self.on_mouse_up(mouse.x, mouse.y, mouse.BUTTON_RIGHT)
            
            if mouse.x != mouse.prev_x or mouse.y != mouse.prev_y:
                self.on_mouse_move(mouse.x, mouse.y)
            if (mouse.x != mouse.prev_x or mouse.y != mouse.prev_y) \
                and mouse.left_button and not mouse.dragging:
                self._mouse_dragging = True
                mouse.dragging = True

        if self._mouse_dragging:
            if (mouse.x != mouse.prev_x or mouse.y != mouse.prev_y) and mouse.left_button:
                self.on_mouse_drag(mouse.x, mouse.y)
            if not mouse.left_button:
                self._mouse_dragging = False
                mouse.dragging = False

    def render(self, screen):
        pass