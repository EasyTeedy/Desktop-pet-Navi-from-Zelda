from pynput import mouse

class MouseListener:
    def __init__(self):
        self.left_button_pressed = False

    def on_click(self, x, y, button, pressed):
        if button == mouse.Button.left:
            self.left_button_pressed = pressed
            print(f"Left button {'pressed' if pressed else 'released'} at ({x}, {y})")


mouse_listener = MouseListener()

with mouse.Listener(on_click=mouse_listener.on_click) as listener:
	listener.join()

