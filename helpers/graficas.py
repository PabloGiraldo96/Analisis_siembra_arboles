import matplotlib.pyplot as plt 

def graficar_veredas(dataFrame, columnX, columnY, nombre):

	cuenta_arboles = dataFrame.groupby(columnX)[columnY].count()

	plt.bar(cuenta_arboles.index, cuenta_arboles)
	plt.xlabel("Veredas")
	plt.ylabel("Arboles")
	plt.title("")
	plt.xticks(rotation=45, ha='right')

	# Guardamos la grafica 

	plt.savefig(f"./assets/img/{nombre}.png", dpi = 250)


