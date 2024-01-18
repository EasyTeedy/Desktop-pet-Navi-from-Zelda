import pyautogui

# Koordinaten des Objekts festlegen
x = 500
y = 500

x


# Objekt anklicken (optional)
# pyautogui.click()

# Schleife, um das Objekt dem Mauszeiger folgen zu lassen
# Aktuelle Position des Mauszeigers abrufen
def follow_curser():
    maus_x, maus_y = pyautogui.position()

    if(maus_x < x):
        x+=4
    elif(maus_x > x):
        x-=4

    if(maus_y < y):
        y+=4
    elif(maus_y > y):
        y-=4

    print("maus_x:", maus_x, "maus_y:", maus_y)
    print("x:", x, "y:", y)


        # Objekt zum Mauszeiger bewegen
#    pyautogui.moveTo(objekt_x, objekt_y, duration=0.1)

    # Überprüfen, ob das Objekt erreicht wurde
 #   if maus_x == objekt_x and maus_y == objekt_y:
#      break
