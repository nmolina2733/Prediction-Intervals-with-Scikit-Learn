
import tkinter as tk

def creandoVentana():
    ventana = tk.Toplevel(app)
    
app = tk.Tk()
app.title("Este es un ejemplo de ventana")
app.geometry("500x500")
ejemploBoton = tk.Button(app, 
              text="Nuevo boton",
              command=creandoVentana)
ejemploBoton.pack()

app.mainloop()