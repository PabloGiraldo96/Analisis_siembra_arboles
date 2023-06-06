import pandas as pd
import numpy as np
from helpers.tablasHTML import crearTabla
from helpers.graficas import graficar_veredas
from helpers.graficaTorta import graficar_torta


tabla_arboles = pd.read_csv('./data/Siembras.csv')


#Query para mostrar siembras de más de 250 Arboles en Santa Fe de Antioquia
tabla_santa_fe = tabla_arboles.query('Arboles > 250 and Ciudad == "Santa Fe de Antioquia"')


#Filtrar datos estadísticos de Caucasia
tabla_caucasia = tabla_arboles.query('Ciudad == "Caucasia"')
estadistica_caucasia = tabla_caucasia.describe().round()


#Query Belmira
#en este caso la condición Vereda == "Rio Arriba" y Vereda == "La Salazar" no puede ser verdadera al mismo tiempo para una misma fila, ya que una fila no puede tener dos valores diferentes en la misma columna "Vereda". En este caso, es posible que obtengas un DataFrame vacío como resultado.
#Si deseas obtener las filas que cumplen con ambas condiciones, es decir, aquellas donde la columna "Vereda" es igual a "Rio Arriba" y también es igual a "La Salazar", deberás utilizar el método de indexación booleana en lugar de la función query(). Aquí tienes un ejemplo:

tabla_belmira = tabla_arboles[(tabla_arboles['Vereda'] == 'Rio Arriba') & (tabla_arboles['Vereda'] == 'La Salazar')]


#Query para mostrar los datos de la Vereda "Mallarino" de la ciudad de Yarumal
tabla_yarumal = tabla_arboles.query('Ciudad == "Yarumal" and Vereda == "Mallarino"')


#Query para mostrar siembras de más de 100 Arboles en Caramanta
tabla_caramanta = tabla_arboles.query('Arboles > 100 and Ciudad =="Caramanta"')

#tabla bello 

tabla_bello = tabla_arboles.query('Ciudad == "Bello"')
est_bello = tabla_bello.describe()

tabla_bello = tabla_bello.replace('Valor_no_numerico', np.nan)  # Reemplazar 'Valor_no_numerico' con el valor no numérico en tus datos
tabla_bello = tabla_bello.dropna()

media_bello = tabla_bello.mean().round()



tabla_datos = tabla_arboles.describe()

#print(tabla_datos)
#print(tabla_santa_fe)	
#print(tabla_yarumal)
#print(tabla_caramanta)
#print(estadistica_caucasia)
#print(est_bello)
print(media_bello)
#print(tabla_belmira)
#print(tabla_belmira1)



# Generacion de tablas 

#crearTabla(tabla_yarumal, "Vereda Mallarino")
#crearTabla(estadistica_caucasia, "Estadistica Caucasia")
#crearTabla(tabla_caramanta, "Arboles Caramanta")


#Graficas 

#graficar_veredas(tabla_santa_fe, 'Vereda', 'Arboles', 'Siembras Mayores a 250')
#graficar_veredas(tabla_caramanta, 'Vereda', 'Arboles', 'SiembrasMayoresa100')


#graficar_torta(tabla_caucasia, [20, 40, 60, 80], 'Arboles', 'Hectareas',estadistica_caucasia)


#print(f"las barras han sido generada")
#print(f"la torta ha sido generada")

#print(f"se ha creado la tabla")










































#Crear instancia de la clase FPDF
#pdf = FPDF()
## Agregar página
#pdf.add_page()
## Establecer fuente y tamaño de letra
#pdf.set_font("Arial", size=12)
## Establecer color de línea
#pdf.set_draw_color(0, 0, 0)  # Color negro
## Dibujar título de la tabla
#pdf.cell(200, 10, txt="Tabla de analistas1:", ln=1, align="L")
## Obtener los datos de la tabla analistas1
#tabla_analistas1 = analistas1.to_string()
## Dividir los datos en filas
#filas = tabla_analistas1.split("\n")
## Dibujar filas y columnas de la tabla
#for fila in filas:
#    columnas = fila.split()
#    for columna in columnas:
#        pdf.cell(40, 10, txt=columna, border=1)  # Dibuja celda con borde
#    pdf.ln()  # Cambia de línea al final de cada fila
## Agregar espacio adicional después de la tabla
#pdf.ln(10)
## Guardar archivo PDF
#pdf.output("archivo.pdf")