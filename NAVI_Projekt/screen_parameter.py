import ctypes

def get_screen_resolution():
    user32 = ctypes.windll.user32
    width = user32.GetSystemMetrics(0)  # 0 entspricht der Breite des primären Bildschirms
    height = user32.GetSystemMetrics(1)  # 1 entspricht der Höhe des primären Bildschirms
    return width, height

if __name__ == "__main__":
    screen_width, screen_height = get_screen_resolution()
    print(f"Screen Width: {screen_width}px")
    print(f"Screen Height: {screen_height}px")