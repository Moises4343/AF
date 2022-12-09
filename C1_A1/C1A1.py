import requests
from bs4 import BeautifulSoup
import pandas as pd
import tkinter


def obtenerURL():
    url = cajaTexto.get()
    r = requests.get(url)

    


    html = requests.get(url).content
    df_list = pd.read_html(html)

    df = df_list[-1]
    print(df)
    df.to_csv('TABLAS_ENCONTRADAS.csv')


ventana = tkinter.Tk()
ventana.geometry("400x300")
etiqueta = tkinter.Label(ventana, text="Ingresar Link")
etiqueta.pack()
cajaTexto = tkinter.Entry(ventana)
cajaTexto.pack()
boton1 = tkinter.Button(ventana, text="Enviar",
                        command=obtenerURL, width=10, height=2)
boton1.pack()
ventana.mainloop()
obtenerURL()
