import pandas as pd


tabla_arboles = pd.read_csv('./data/Siembras.csv')

#Query para mostrar siembras de más de 250 Arboles en Santa Fe de Antioquia
tabla_santa_fe = tabla_arboles.query('Arboles > 250 and Ciudad == "Santa Fe de Antioquia"')
 
#Filtrar todos los datos de Caucasia // FALTA INTERPRETAR ESTADISTICAS
tabla_caucasia = tabla_arboles.query('Ciudad == "Caucasia"')

#Query Belmira
tabla_belmira = tabla_arboles.query('Vereda == "Rio Arriba"')
tabla_belmira1 = tabla_arboles.query('Vereda == "La Salazar"')

#Query para mostrar los datos de la Vereda "Mallarino" de la ciudad de Yarumal
tabla_yarumal = tabla_arboles.query('Ciudad == "Yarumal" and Vereda == "Mallarino"')

#Query para mostrar siembras de más de 100 Arboles en Caramanta
tabla_caramanta = tabla_arboles.query('Arboles > 100 and Ciudad =="Caramanta"')


tabla_datos = tabla_arboles.describe()

print(tabla_datos)
print(tabla_santa_fe)	
print(tabla_yarumal)
print(tabla_caramanta)
print(tabla_caucasia)
print(tabla_belmira)
print(tabla_belmira1)















































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