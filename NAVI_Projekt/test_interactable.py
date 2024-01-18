from hit_her import MouseListener

if __name__ == "__main__":
    mouse_listener = MouseListener()
    mouse_listener.start_listener()

    # Hier kannst du auf die Variable 'clicked' zugreifen

    if mouse_listener.clicked:
        print("Linke Maustaste wurde geklickt!")
        mouse_listener.clicked = False  # Zurücksetzen für den nächsten Klick
        
    