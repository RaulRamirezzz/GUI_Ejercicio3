from tkinter import *
from tkinter import ttk 

raiz=Tk()
raiz.title("Ejercicio 2")
raiz.geometry("1340x800")

# definir estilo para el Frame 1
estiloGris = ttk.Style()
estiloGris.configure('gris.TFrame', background='#333333')
estiloNegro = ttk.Style()
estiloNegro.configure('negro.TFrame', background='black')
estiloAzul = ttk.Style()
estiloAzul.configure('azul.TFrame', background='#097479')


#------------------------------------------------ FRAME 0 ----------------------------------------------------------------------------
Frame0 = ttk.Frame(raiz, padding="10 5 1192 5", style='azul.TFrame')
Frame0.grid(column=0, row=0, padx=0, pady=0)

imagenBarras = PhotoImage(file="barra.png")
etqImagenBarras = ttk.Label(Frame0)
etqImagenBarras.grid(sticky=(W), column=0, row=0, padx=0, pady=0)
etqImagenBarras.config(background='#097479')
etqImagenBarras['image'] = imagenBarras

ttk.Label(Frame0, text="SPAI 4.0", font=("arial", 14), background="#097479",
           foreground='white').grid(column=1, row=0, padx=0, pady=20, sticky=(W))

#------------------------------------------------ FRAME 1 ----------------------------------------------------------------------------
Frame1 = ttk.Frame(raiz, padding="10 10 10 10", style='negro.TFrame')
Frame1.grid(column=0, row=1, padx=0, pady=0)

#------------------------------------------------ FRAME 2 ----------------------------------------------------------------------------
Frame2 = ttk.Frame(Frame1, padding="10 0 10 10", style='negro.TFrame')
Frame2.grid(column=0, row=0, padx=0, pady=0)

#------------------------------------------------ FRAME 3 ----------------------------------------------------------------------------
Frame3 = ttk.Frame(Frame1, padding="0 0 0 0", style='gris.TFrame')
Frame3.grid(column=1, row=0, padx=0, pady=0, sticky=(N))
ttk.Label(Frame3, text="Produccion", font=("arial", 14, 'bold'), background='#333333',
           foreground='#0fbcc4').grid(column=0, row=0, padx=10, pady=10, sticky=(W))
ttk.Label(Frame3, text="Piezas producidas: 50", font=("arial", 12), background='#333333',
           foreground='white').grid(column=0, row=2, padx=10, pady=20)
ttk.Label(Frame3, text="Piezas defectuosas: 12", font=("arial", 12), background='#333333',
           foreground='white').grid(column=0, row=3, padx=10, pady=10)

imagenGrafica = PhotoImage(file="grafica.png")
etqImagenGrafica = ttk.Label(Frame3)
etqImagenGrafica.grid(sticky=(W), column=0, row=1, padx=0, pady=20)
etqImagenGrafica.config(background='#333333')
etqImagenGrafica['image'] = imagenGrafica

#------------------------------------------------ FRAME 4 ----------------------------------------------------------------------------
Frame4 = ttk.Frame(Frame2, padding="0 0 0 0", style='negro.TFrame')
Frame4.grid(column=0, row=0, padx=0, pady=0, sticky=(N, W))

#------------------------------------------------ FRAME 5 ----------------------------------------------------------------------------
Frame5 = ttk.Frame(Frame2, padding="0 0 0 0", style='negro.TFrame')
Frame5.grid(column=0, row=1, padx=0, pady=0, sticky=(N, E))

#------------------------------------------------ FRAME 6 ----------------------------------------------------------------------------
Frame6 = ttk.Frame(Frame4, padding="10 0 10 0", style='gris.TFrame')
Frame6.grid(column=0, row=0, padx=10, pady=0, sticky=(N))

ttk.Label(Frame6, text="Produccion", font=("arial", 14, 'bold'), background='#333333',
           foreground='#0fbcc4').grid(column=0, row=0, padx=0, pady=10, sticky=(W))

ttk.Label(Frame6, text="Linea 1: ", font=("arial", 12), background='#333333',
           foreground='white').grid(column=0, row=1, padx=0, pady=10, sticky=(W))
ttk.Label(Frame6, text="Linea 2: ", font=("arial", 12), background='#333333',
           foreground='white').grid(column=0, row=2, padx=0, pady=10, sticky=(W))
ttk.Label(Frame6, text="Linea 3: ", font=("arial", 12), background='#333333',
           foreground='white').grid(column=0, row=3, padx=0, pady=10, sticky=(W))
ttk.Label(Frame6, text="Gabinete: ", font=("arial", 12), background='#333333',
           foreground='white').grid(column=0, row=4, padx=0, pady=10, sticky=(W))
ttk.Label(Frame6, text="Alarma: ", font=("arial", 12), background='#333333',
           foreground='white').grid(column=0, row=5, padx=0, pady=10, sticky=(W))
ttk.Label(Frame6, text="Alarma 2: ", font=("arial", 12), background='#333333',
           foreground='white').grid(column=0, row=6, padx=0, pady=10, sticky=(W))

ttk.Label(Frame6, text="On", font=("arial", 12, 'bold'), background='#333333',
           foreground='white').grid(column=1, row=1, padx=0, pady=10, sticky=(W))
ttk.Label(Frame6, text="On", font=("arial", 12, 'bold'), background='#333333',
           foreground='white').grid(column=1, row=2, padx=0, pady=10, sticky=(W))
ttk.Label(Frame6, text="On", font=("arial", 12, 'bold'), background='#333333',
           foreground='white').grid(column=1, row=3, padx=0, pady=10, sticky=(W))
ttk.Label(Frame6, text="Abierto", font=("arial", 12, 'bold'), background='#333333',
           foreground='white').grid(column=1, row=4, padx=0, pady=10, sticky=(W))
ttk.Label(Frame6, text="On", font=("arial", 12, 'bold'), background='#333333',
           foreground='white').grid(column=1, row=5, padx=0, pady=10, sticky=(W))
ttk.Label(Frame6, text="Off", font=("arial", 12, 'bold'), background='#333333',
           foreground='white').grid(column=1, row=6, padx=0, pady=10, sticky=(W))

imagenrojo = PhotoImage(file="rojo.png")
imagenverde = PhotoImage(file="verde.png")

etq1 = ttk.Label(Frame6)
etq1.grid(sticky=(W), column=2, row=1, padx=10, pady=10)
etq1.config(background='#333333')
etq1['image'] = imagenverde

etq2 = ttk.Label(Frame6)
etq2.grid(sticky=(W), column=2, row=2, padx=10, pady=10)
etq2.config(background='#333333')
etq2['image'] = imagenverde

etq3 = ttk.Label(Frame6)
etq3.grid(sticky=(W), column=2, row=3, padx=10, pady=10)
etq3.config(background='#333333')
etq3['image'] = imagenverde

etq4 = ttk.Label(Frame6)
etq4.grid(sticky=(W), column=2, row=4, padx=10, pady=10)
etq4.config(background='#333333')
etq4['image'] = imagenrojo

etq5 = ttk.Label(Frame6)
etq5.grid(sticky=(W), column=2, row=5, padx=10, pady=10)
etq5.config(background='#333333')
etq5['image'] = imagenrojo

etq6 = ttk.Label(Frame6)
etq6.grid(sticky=(W), column=2, row=6, padx=10, pady=10)
etq6.config(background='#333333')
etq6['image'] = imagenverde

#------------------------------------------------ FRAME 7 ----------------------------------------------------------------------------
Frame7 = ttk.Frame(Frame4, padding="10 0 10 30", style='gris.TFrame')
Frame7.grid(column=1, row=0, padx=0, pady=0, sticky=(N))

ttk.Label(Frame7, text="Produccion", font=("arial", 14, 'bold'), background='#333333',
           foreground='#0fbcc4').grid(column=0, row=0, padx=10, pady=10, sticky=(W))

ttk.Label(Frame7, text="Temperatura 1: ", font=("arial", 12, 'bold'), background='#333333',
           foreground='white').grid(column=0, row=1, padx=10, pady=10)
ttk.Label(Frame7, text="Temperatura 2: ", font=("arial", 12, 'bold'), background='#333333',
           foreground='white').grid(column=1, row=1, padx=10, pady=10)

imagentemp1 = PhotoImage(file="temp1.png")
etqImagentemp1 = ttk.Label(Frame7)
etqImagentemp1.grid(sticky=(W), column=0, row=2, padx=0, pady=10)
etqImagentemp1.config(background='#333333')
etqImagentemp1['image'] = imagentemp1

imagentemp2 = PhotoImage(file="temp2.png")
etqImagentemp2 = ttk.Label(Frame7)
etqImagentemp2.grid(sticky=(W), column=1, row=2, padx=0, pady=10)
etqImagentemp2.config(background='#333333')
etqImagentemp2['image'] = imagentemp2

ttk.Label(Frame7, text="Temp.Agua: ", font=("arial", 12), background='#333333',
           foreground='white').grid(column=0, row=3, padx=10, pady=20, sticky=(E))
ttk.Label(Frame7, text="Temp.Ambiente: ", font=("arial", 12), background='#333333',
           foreground='white').grid(column=0, row=4, padx=10, pady=20, sticky=(E))

ttk.Label(Frame7, text="58°C", font=("arial", 12, 'bold'), background='#333333',
           foreground='white').grid(column=1, row=3, padx=10, pady=20, sticky=(W))
ttk.Label(Frame7, text="32°C", font=("arial", 12, 'bold'), background='#333333',
           foreground='white').grid(column=1, row=4, padx=10, pady=20, sticky=(W))

#------------------------------------------------ FRAME 8 ----------------------------------------------------------------------------
Frame8 = ttk.Frame(Frame5, padding="30 43 75 35", style='gris.TFrame')
Frame8.grid(column=0, row=0, padx=10, pady=10, sticky=(N, W))

ttk.Label(Frame8, text="Velocidad bomba: ", font=("arial", 14, 'bold'), background='#333333',
           foreground='white').grid(column=0, row=0, padx=10, pady=10, sticky=(W))

imagenvelocidad = PhotoImage(file="velocidadBomba.png")
etqImagenvelocidad = ttk.Label(Frame8)
etqImagenvelocidad.grid(sticky=(W), column=0, row=1, padx=0, pady=0)
etqImagenvelocidad.config(background='#333333')
etqImagenvelocidad['image'] = imagenvelocidad

#------------------------------------------------ FRAME 9 ----------------------------------------------------------------------------
Frame9 = ttk.Frame(Frame5, padding="30 0 70 0", style='gris.TFrame')
Frame9.grid(column=1, row=0, padx=0, pady=10, sticky=(N, W))

ttk.Label(Frame9, text="Nivel de tanque", font=("arial", 14, 'bold'), background='#333333',
           foreground='#0fbcc4').grid(column=0, row=0, padx=10, pady=10, sticky=(W))

imagentanque = PhotoImage(file="nivelTanque.png")
etqImagentanque = ttk.Label(Frame9)
etqImagentanque.grid(sticky=(W), column=0, row=1, padx=0, pady=0)
etqImagentanque.config(background='#333333')
etqImagentanque['image'] = imagentanque













raiz.mainloop()