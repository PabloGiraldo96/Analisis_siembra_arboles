import matplotlib.pyplot as plt 

def graficar_veredas(dataFrame, columnX, columnY, nombre):

	colores = ['green', 'red']
	
	cuenta_arboles = dataFrame.groupby(columnX)[columnY].count()

	plt.bar(cuenta_arboles.index, cuenta_arboles, color = colores)
	plt.xlabel("Veredas")
	plt.ylabel("Arboles")
	plt.title("Siembras mayores a 250")
	plt.xticks(rotation=45, ha='right')	

	# Guardamos la grafica 

	plt.savefig(f"./assets/img/{nombre}.png", dpi = 250)


