#Primero importaremos las librerias
import tkinter as tk
import qrcode
from tkinter import PhotoImage, ttk
from tkinter import messagebox

#Creamos una variable para crear la ventana
a = tk.Tk()
a.title('QRcreator')
a.geometry('350x350')
a.resizable(False,False)
a.config(background='aqua')

#Creamos otra variable, pero esta vez para un boton
b = ttk.Button(text='Direccion del QR')
#Posicionamos el boton
b.place(x=20,y=20)

#Creamos la variable de la caja de texto
c = ttk.Entry()
c.place(x=20,y=48)

d = ttk.Button(text='Guardar como ')
d.place(x=20,y=80)

e = ttk.Entry()
e.place(x=20,y=108)

#Creamos una funcion para obtener el texto  que introducimos
def obtener():
    texto = c.get()
    #ESTE DE ABAJO ES EL SEGUNDO TEXTO INTRODUCIDO
    textoo = e.get()
    #Creamos Condiciones
    if texto.strip()in(''):
        messagebox.showerror(title='Error', message='Introduce al menos 1 caracter')
        #ESTE IF ESTABA MAL
    if textoo.strip()in(''):
        #Asi debe ESTAR
            messagebox.showerror(title='Error', message='Introduce al menos 1 caracter')
            return False
    else:
        qr = qrcode.QRCode(version=1,box_size=10,border=10)
        qr.add_data(texto)
        qr.make(fit=True)

        img = qr.make_image(fill='black', bg ='white')
        img.save(textoo + '.png')
        messagebox.showinfo(title='Buenas noticias', message='Su QR se ha generado y Guardado Exitosamente')


        #Creamos otra funcion 
def requerimientoI():
    messagebox.showinfo(title='Informacion', message='El programa solo funciona cuando se ejecuta directamente en PYTHON')

    #Creamos una variable para posicionar y añadir los botones
g = ttk.Button(text='Requerimiento', command=requerimientoI)
g.place(x=230,y=10)
    
f = ttk.Button(text='Crear QR', command=obtener)
f.place(x=45,y=150)

    #Añadimos lo mas importante
a.mainloop()
    #Pero antes arreglaremos unos errores

    #Y ejecutamos.
