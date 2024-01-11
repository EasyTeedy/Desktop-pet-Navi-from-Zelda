import random
import pyautogui
import tkinter as tk
from screen_parameter import get_screen_resolution

# Absoluter Pfad zu den Bildern
impath = 'C:\\Users\\Cedric Rissi\\Desktop\\Zelda_NAVI\\NAVI_Projekt\\Navi_gifs\\'

# Startvariablen
x = int
y = int
#Parameter für funktion Following Kurser:
follow_x = 2
follow_y = 1
#default Werte:
start_range = 1
end_range = 10
x_moving_steps=1
y_moving_steps=2
cycle = 0
check = 1
event_number = 1
i = int(0)


old_event_number = int(0)
switch = int(0)

#Config Start point
try:
    screen_width, screen_height = get_screen_resolution()
    x=int(screen_width-screen_width/2)
    y=int(screen_height-screen_height/2)
except:
    print("No Screen Parameter found")
    x=50
    y=50

#Choosing what to do
idle_arr = [1,2]
#idle_down_arr = [2]

idle_right_arr = [3,4,5,6]
#idle_down_right_arr = [4]

idle_left_arr = [7,8,9,10]
#idle_down_left_arr = [6]



# Start 20, Stop 59, Schritte 1s
print(f"{event_number} first select")

#gif ist bewegung nach up/down left/right ist Maus zeiger abhängig
def follow_curser(x,y):
    maus_x, maus_y = pyautogui.position()
    global follow_x
    global follow_y

    if(maus_y < y):
        y-=follow_y
    elif(maus_y > y):
        y+=follow_y

    if(maus_x - 30 <= x <= maus_x + 30):
        return x, y

    if(maus_x < x):
        x-=follow_x
    elif(maus_x > x):
        x+=follow_x

    print("maus_x:", maus_x, "maus_y:", maus_y)
    print("x:", x, "y:", y)  
    return x,y   

# Transferiere eine zufällige Nummer zu einem Event
def event(cycle, check, event_number, x, y):
    # Idle Navi
    #Moving:
    #up
    if event_number in idle_arr:
        check = 1 
        #y-=y_moving_steps
        window.after(80, update, cycle, check, event_number, x, y)
    #down
    
    #Right:
    elif event_number in idle_right_arr:
        check = 3 
        x+=x_moving_steps
        window.after(80, update, cycle, check, event_number, x, y)
        
    #Left:
    elif event_number in idle_left_arr:
        check = 5 
        x-=x_moving_steps
        window.after(80, update, cycle, check, event_number, x, y)

# Funktion für die GIF-Animation
def gif_work(cycle, frames, event_number, first_num, last_num, x, y):
    if cycle < len(frames) - 1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num + 1, 1)
    return cycle, event_number, x, y

# Funktion für die Aktualisierung des Fensters
def update(cycle, check, event_number, x, y):
    global i
    global end_range
    global start_range
    # Navi Idle
    if check == 1:
        frame = idle[cycle]
        cycle, event_number, x, y = gif_work(cycle, idle, event_number, start_range, end_range, x, y)
    
        
    #right
    elif check == 3:
        if i/5 >= 2:
            event_number = random.randrange(start_range, end_range, 1)
            print("und recht los")
            #i=0
        frame = idle[cycle]
        cycle, event_number, x, y = gif_work(cycle, idle, event_number, start_range, end_range, x, y)   
    
    elif check == 4:
        if i/5 >= 2:
            event_number = random.randrange(start_range, end_range, 1)
            print("und recht los")
            #i=0
        frame = idle[cycle]
        cycle, event_number, x, y = gif_work(cycle, idle, event_number, start_range, end_range, x, y)

    #left
    elif check == 5:
        if i/5 >= 2:
            event_number = random.randrange(start_range, end_range, 1)
            print("und links los")
            i=0
        frame = idle[cycle] 
        cycle, event_number, x, y = gif_work(cycle, idle, event_number, start_range, end_range, x, y)   
    
    elif check == 6:
        if i/5 >= 2:
            event_number = random.randrange(start_range, end_range, 1)
            print("und links los")
            i=0
        frame = idle[cycle]
        cycle, event_number, x, y = gif_work(cycle, idle, event_number, start_range, end_range, x, y)
        

    #Default UP/Down Idle
    if i <= 5:
        y+=y_moving_steps
        print("Down")
        i+=1
    elif i <=11:
        print("Up")
        y-=y_moving_steps
        i+=1
    elif i>11:
        i=1
        print("end up/down rotine")


    x,y = follow_curser(x,y)
    # Fenstergröße und Position
    window.geometry('120x100+' + str(x-60) + "+" + str(y-15))
    label.configure(image=frame)
    window.after(5, event, cycle, check, event_number, x, y)
    print(event_number)

window = tk.Tk()

# Lade GIF
idle = [tk.PhotoImage(file=impath + 'idle.gif', format='gif -index %i' % i) for i in range(5)]

window.config(highlightbackground='green')
window.config(background="green")
label = tk.Label(window, bd=0, bg='green')
window.overrideredirect(True)
window.attributes("-topmost", True)  # Immer im Vordergrund
window.wm_attributes('-transparentcolor', 'green')

# Starte die Schleife des Programms
window.after(1, update, cycle, check, event_number, x, y)
label.pack()
window.mainloop()
