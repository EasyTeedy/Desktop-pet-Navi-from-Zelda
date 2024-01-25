import tkinter as tk

def farbe_aendern():
    # Ändern Sie hier die Farbe nach Bedarf
    neue_farbe = "red"
    hauptfenster.configure(bg=neue_farbe)

# Hauptfenster erstellen
hauptfenster = tk.Tk()
hauptfenster.title("Farbänderung Beispiel")

# Schaltfläche zum Ändern der Farbe hinzufügen
schaltflaeche = tk.Button(hauptfenster, text="Farbe ändern", command=farbe_aendern)
schaltflaeche.pack(pady=20)

# Das Hauptfenster starten
hauptfenster.mainloop()
