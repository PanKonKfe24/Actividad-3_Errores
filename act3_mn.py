"""
           Autor:
   Juan Pablo Buitrago Rios
   juanybrisagames@gmail.com
   Version 2.0 : 05/02/2025 11:20pm

"""

def calcular_errores(x, y, valor_real):
    diferencia = x - y #Calculamos la diferencia entre los 2 valores dados
    
    #Calculamos los errores con respecto al valor real 
    error_abs = abs(valor_real - diferencia) 
    error_rel = error_abs / abs(valor_real)
    error_pct = error_rel * 100
    error_cua = error_abs**2

    #Imprimimos los resultados
    print(f"Diferencia: {diferencia}")
    print(f"Error absoluto: {error_abs}")
    print(f"Error relativo: {error_rel}")
    print(f"Error porcentual: {error_pct}%")
    print(f"Error cuadratico: {error_cua}")

#Dentro de la matriz agregamos por segmentos los datos que vamos a comparar, siendo la estructura de x,y,resultante_real_entre_x-y
valores = [(1.0000001, 1.0000000, 0.0000001), (1.000000000000001, 1.000000000000000, 0.000000000000001)] #Instancia de la matriz valores

#Ciclo necesario para recorrer la matriz y comprar los conjuntos de datos 1 a 1
for x, y, real in valores:
    print(f"\nPara x={x}, y={y}:") #Mostramos los valores que se van a comparar
    calcular_errores(x, y, real) #Enviamos los datos den conjunto en turno a la función 