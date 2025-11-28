"""
Este conjunto de datos corresponde a un corte de un conjunto de datos de
tomografía. Esto hace que la visualización de imágenes sea apropiada debido a
la familiaridad con este tipo de conjuntos de datos.
"""

data = np.load("../data/2d_exercise.npy")

plt.figure()
plt.imshow(data, cmap="bone")
