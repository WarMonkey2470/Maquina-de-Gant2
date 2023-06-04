# Maquina-de-Gant2
Tercera tarea del curso
# Simulador de mawuina de galton con 12 niveles y 3000 canicas

#Numaric python librery
import numpy as np

#Random number librery
import random

#Plotting library
from matplotlib import pyplot as plt

#Numaero de Canicas y obstaculos
n_canicas = 3000
n_obstaculos = 12
n_traslados = 12
# Probabilidad de ir a izquierda o derecha
pron = 50

# Define la funcion del paseo aleatorio. N es el numero de canicas y
# p es la probabilidad de avanzar o retroceder. 
def SimpleRandomwalk(N, p, line):  
    position = np.empty(N)
    position[0] = 0
    n_traslados = 0 

 #Array que contiene el rango completo del numero de posibles obstaculos esquivados.
obstaculos = np.arange(n_traslados)   

#Comienza el movimiento aleatorio.
for i in range(1,n_canicas):  
     #Genera un valor de probabilidad aleatorio entre 0 y 1  
    float = random.random()
    if float >= np: 
        n_traslados += 1
    else:
        n_traslados -= 1

    obstaculos[i] = n_traslados


#Generar un gráfico de la posición del caminante frente al número de pasos dados. Línea es una cadena que describirá el
#marcadores y tipo de línea utilizados para trazar la caminata aleatoria.
plt.plot(n_canicas, n_obstaculos, n_traslados)
plt.xlavel('Contenedores') 
plt.ylabel('Cantidad de canicas')
plt.title('Histograma de resultados de la maquina de gant')
plt.show()


# Parametros de la simulacion
n_canicas = 3000
n_obstaculos = 12

# Simulacion de la maquina de Galton
resultados = (n_canicas, n_obstaculos, n_traslados)  
