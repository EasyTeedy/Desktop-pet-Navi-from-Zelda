import random
import tkinter as tk
from screen_parameter import get_screen_resolution

# Absoluter Pfad zu den Bildern
impath = 'C:\\Users\\Cedric Rissi\\Desktop\\Zelda_NAVI\\NAVI_Projekt\\Navi_gifs\\'

# Startvariablen
x = int
y = int
start_range = 1
end_range = 6
x_moving_steps=1
y_moving_steps=2
cycle = 0
check = 1
event_number = 1
idle_mode = 0
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
idle_up_arr = [1]
idle_down_arr = [2]

idle_up_right_arr = [3]
idle_down_right_arr = [4]

idle_up_left_arr = [5]
idle_down_left_arr = [6]



# Start 20, Stop 59, Schritte 1s
print(f"{event_number} first select")

# NOCH nicht emplementiiert !!! 
# funktioniert auch nicht weil immer zwischen zwei zahlen gewechselt wird
def Abwechslung(event_number):
    global old_event_number
    global switch
    if event_number == old_event_number:
        switch+=1
        if switch >= 5:
            new_event_number = old_event_number - random.randrange(start_range,end_range)
            if new_event_number <=0:
                if new_event_number == 0:
                    new_event_number= random.randrange(start_range,end_range)
                else:
                    event_number = new_event_number*(-1)
            else:
                event_number = new_event_number
            switch = 0
        else:
            pass
    else:
        pass
        

# Transferiere eine zufällige Nummer zu einem Event
def event(cycle, check, event_number, x, y):
    # Idle Navi
    #Moving:
    #up
    if event_number in idle_up_arr:
        check = 1 
        y-=y_moving_steps
        window.after(80, update, cycle, check, event_number, x, y)
    #down
    elif event_number in idle_down_arr:
        check = 2 
        y+=y_moving_steps
        window.after(80, update, cycle, check, event_number, x, y)
    #Right:
    elif event_number in idle_up_right_arr:
        check = 3 
        y-=y_moving_steps
        x+=x_moving_steps
        window.after(80, update, cycle, check, event_number, x, y)
    elif event_number in idle_down_right_arr:
        check = 4
        y+=y_moving_steps
        x+=x_moving_steps
        window.after(80, update, cycle, check, event_number, x, y)
    #Left:
    elif event_number in idle_up_left_arr:
        check = 5 
        y-=y_moving_steps
        x-=x_moving_steps
        window.after(80, update, cycle, check, event_number, x, y)
    elif event_number in idle_down_left_arr:
        check = 6
        y+=y_moving_steps
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
        if i/5 >= 2:
            event_number = random.randrange(start_range, end_range, 1)
            print("und los")
            i=0

        frame = idle[cycle]
        cycle, event_number, x, y = gif_work(cycle, idle, event_number, 2, 2, x, y)
    elif check == 2:
        if i/5 >= 2:
            event_number = random.randrange(start_range, end_range, 1)
            print("und los")
            i=0

        frame = idle[cycle]
        cycle, event_number, x, y = gif_work(cycle, idle, event_number, 1, 1, x, y)
        i+=1
        
    #right
    elif check == 3:
        if i/5 >= 2:
            event_number = random.randrange(start_range, end_range, 1)
            print("und recht los")
            i=0
        frame = idle[cycle]
        cycle, event_number, x, y = gif_work(cycle, idle, event_number, 4, 4, x, y)   
    
    elif check == 4:
        if i/5 >= 2:
            event_number = random.randrange(start_range, end_range, 1)
            print("und recht los")
            i=0
        frame = idle[cycle]
        cycle, event_number, x, y = gif_work(cycle, idle, event_number, 3, 3, x, y)
        i+=1

    #left
    elif check == 5:
        if i/5 >= 2:
            event_number = random.randrange(start_range, end_range, 1)
            print("und links los")
            i=0
        frame = idle[cycle] 
        cycle, event_number, x, y = gif_work(cycle, idle, event_number, 6, 6, x, y)   
    
    elif check == 6:
        if i/5 >= 2:
            event_number = random.randrange(start_range, end_range, 1)
            print("und links los")
            i=0
        frame = idle[cycle]
        cycle, event_number, x, y = gif_work(cycle, idle, event_number, 5, 5, x, y)
        i+=1
        



    # Fenstergröße und Position
    window.geometry('120x100+' + str(x) + "+" + str(y))
    label.configure(image=frame)
    window.after(5, event, cycle, check, event_number, x, y)
    print(event_number)

window = tk.Tk()

# Lade GIFs
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
