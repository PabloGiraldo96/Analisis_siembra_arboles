import matplotlib.pyplot as plt
import pandas as pd 

def graficar_torta(dataFrame, rangos, columnaInteresRango, columnaPromediar, nombre): 
	
	plt.figure()

	dataFrame['rangoNuevo'] = pd.cut(dataFrame[columnaInteresRango], bins= rangos)

	arboles_por_hectarea = dataFrame.groupby('rangoNuevo')[columnaPromediar].sum()

	arboles = arboles_por_hectarea.values

	hectareas = arboles_por_hectarea.index

	plt.pie(arboles, labels= hectareas, autopct='%1.1f%%')

	plt.pie("Arboles por hectarea")

	plt.savefig(f'./assets/img/{nombre}.png', dpi= 250)