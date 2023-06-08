import pandas as pd
from helpers.tablasHTML import crearTabla
from helpers.graficas import graficar_veredas
from helpers.graficaTorta import graficar_torta
from fpdf import FPDF


tabla_arboles = pd.read_csv('./data/Siembras.csv')

#Query para mostrar siembras de más de 250 Arboles en Santa Fe de Antioquia
tabla_santa_fe = tabla_arboles.query('Arboles > 250 and Ciudad == "Santa Fe de Antioquia"')

#Filtrar datos estadísticos de Caucasia
tabla_caucasia = tabla_arboles.query('Ciudad == "Caucasia"')
estadistica_caucasia = tabla_caucasia.describe().round()

#Query Belmira
tabla_belmira = tabla_arboles.query('(Vereda== "Rio Arriba") | (Vereda=="La Salazar")')

#Query para mostrar los datos de la Vereda "Mallarino" de la ciudad de Yarumal
tabla_yarumal = tabla_arboles.query('Ciudad == "Yarumal" and Vereda == "Mallarino"')

#Query para mostrar siembras de más de 100 Arboles en Caramanta
tabla_caramanta = tabla_arboles.query('Arboles > 100 and Ciudad =="Caramanta"')

#tabla bello 
tabla_bello = tabla_arboles.query('Ciudad == "Bello" and Vereda == "Quitasol"').describe().round()
est_bello = tabla_bello.describe().mean().round

tabla_datos = tabla_arboles.describe()

#print(tabla_datos)
#print(tabla_santa_fe)	
#print(tabla_yarumal)
#print(tabla_caramanta)
#print(estadistica_caucasia)
#print(est_bello)
print(tabla_bello)
#print(tabla_belmira)

# Generacion de tablas 

#crearTabla(tabla_yarumal, "Vereda Mallarino")
#crearTabla(estadistica_caucasia, "Estadistica Caucasia")
#crearTabla(tabla_caramanta, "Arboles Caramanta")
#crearTabla(tabla_bello, "QuitasolBello")
#crearTabla(tabla_belmira, "La Salazar")


#Graficas 

#graficar_veredas(tabla_santa_fe, 'Vereda', 'Arboles', 'SiembrasSantaFe')
#graficar_veredas(tabla_caramanta, 'Vereda', 'Arboles', 'SiembrasMayoresa100')
#graficar_veredas(tabla_arboles, 'Vereda', 'Arboles', 'MediaQuitasolBello')
#graficar_veredas(tabla_belmira, 'Vereda', 'Arboles', 'VeredasBelmira')
#graficar_veredas(tabla_caucasia, 'Ciudad', 'Arboles', 'datosCaucasia')
#graficar_veredas(tabla_bello, 'Ticket', 'Arboles', 'Hectareas')


#graficar_torta(tabla_caucasia, [20, 40, 60, 80], 'Arboles', 'Hectareas',estadistica_caucasia)

columnas_deseadas = ['Ticket','Arboles', 'Hectareas']
tabla_nueva = tabla_bello[columnas_deseadas]

#Crear instancia de la clase FPDF
pdf = FPDF()
# Agregar página
pdf.add_page()
# Establecer fuente y tamaño de letra
pdf.set_font("Arial", size=12)
# Establecer color de línea
pdf.set_draw_color(0, 0, 0)  # Color negro	
pdf.set_top_margin(10)
# Dibujar título de la tabla
pdf.cell(200, 40, txt="Vereda Quitasol Bello", ln=1, align="C")
# Obtener los datos de la tabla analistas1
tabla_texto  = tabla_nueva.to_string()	
# Dividir los datos en filas
filas = tabla_texto.split("\n")
ancho_celda = 30
# Dibujar filas y columnas de la tabla
for fila in filas:
    columnas = fila.split()
    for columna in columnas:
        pdf.cell(ancho_celda, 10, txt=columna, border=3)  # Dibuja celda con borde
    pdf.ln()  # Cambia de línea al final de cada fila
# Agregar espacio adicional después de la tabla
pdf.ln(10)
# Guardar archivo PDF
pdf.output("./pdf/archivoBello.pdf")
