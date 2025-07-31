import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


Encuesta = pd.read_csv("encuesta_bienestar.csv") 
print(Encuesta.head())  

#datos nulos 
print(Encuesta.isnull().sum()) # No hay nulos.

#duplicados
print(Encuesta.duplicated().sum()) # No hay datos duplicados.

print(Encuesta.dtypes) # Las variables estan bien expresadas.

# voy a pasar todas las variables de tipo texto a minuscula.
Encuesta["gender"] = Encuesta["gender"].str.lower()
Encuesta["country"] = Encuesta["country"].str.lower()
Encuesta["income_bracket"] = Encuesta["income_bracket"].str.lower()

""" Viendo el histograma del tiempo frente a pantallas, se puede observar intervalos negativos. Lo cual,
es imposible porque el tiempo no puede ser negativo. """

#Busqueda de filas con valores negativos en el tiempo frente a pantallas
print("VALORES NEGATIVOS EN HORAS FRENTE A PANTALLAS")
print(Encuesta[Encuesta["screen_time"]<0])
print("CANTIDAD DE VALORES NEGATIVOS EN LA COLUMNA SCREEN_TIME")
print((Encuesta["screen_time"]<0).sum())
""" Se registraron 8 filas con valores negativos, como representan solo el 0,8% del total de registros, decidí 
eliminarlos para que no afecten la calidad del análisis. """

#Eliminacion de registros negativos
Encuesta = Encuesta[Encuesta["screen_time"] >= 0]


Encuesta.to_csv("EncuestaBienestarLimpio.csv", index=False) #Guardé los cambios.


#¿Cuántas horas duermen, en promedio, los enuestados?
promedio_horas_sueño = Encuesta["hours_sleep"].mean()
print(f"En promedio duermen: {promedio_horas_sueño} horas")
""" En promedio duermen: 6.969799999999999 horas """

sns.histplot(data=Encuesta, x='hours_sleep', bins=10, kde=True, color='skyblue')
plt.title("Distribucion de las horas de sueño")
plt.xlabel("Horas de sueño")
plt.ylabel("Cantidad de personas")
plt.savefig("HistogramatHorasDeSueño.png")
plt.show()
""" En este histograma se puede observar que la mayoria de las personas duermen entre 6 y 8 horas en promedio """

# Edad promedio de los encuestados 
edad_promedio = Encuesta["age"].mean()
print(f"La edad promedio de los encuestados es: {edad_promedio}")
""" La edad promedio de los encuestados es: 40.986 """
print("MAXIMO Y MINIMO DE EDAD")
print(Encuesta["age"].min())
print(Encuesta["age"].max())
""" Edas máxima: 64 años.
Edad mínima: 18 años. """

# Tiempo frente a pantallas.
tiempo_en_pantallas = Encuesta["screen_time"].mean()
print(f"El tiempo promedio frente a las pantallas es: {tiempo_en_pantallas}")
""" El tiempo promedio frente a las pantallas es: 6.029 """


#Histograma correcto
#con esta gráfico pude darme cuenta que habia un error en los datos (valores negativos en el tiempo de pantalla)
#es por eso, que antes de seguir elimine las filas con datos negativos ya que solo representaban el 0,8% de la muestra.
sns.histplot(data=Encuesta, x='screen_time', bins=10, kde=True, color='skyblue')
plt.title("Distribución del tiempo frente a pantallas")
plt.xlabel("Horas frente a pantallas")
plt.ylabel("Cantidad de personas")
plt.savefig("TiempoPantallas.png")
plt.show()

#Histograma de frecuencia acumulada
plt.hist(Encuesta["screen_time"], bins=10, cumulative=True, color='skyblue', edgecolor='black')
plt.title("Frecuencia acumulada del tiempo frente a pantallas")
plt.xlabel("Horas frente a pantallas")
plt.ylabel("Frecuencia acumulada")
plt.grid(True)
plt.savefig("FrecuenciaAcumuladaTiempoPantallas.png")
plt.show()

print("MEDIANA")
print(Encuesta["screen_time"].median())
""" 
Teniendo en cuenta la mediana, (que tambien se puede observar en el grafico de frecuencias acumuladas anterior)
se puede confirmar que el 50% de las personas encuestadas pasa 6 o mas horas frente a las pantallas. """


#Nivel de estrés.
nivel_estres = Encuesta["stress_level"].mean()
print(f"El nivel promedio de estres es: {nivel_estres}")
""" El nivel promedio de estres es: 5.496 """

print("MINIMO Y MAXIMO")
print(Encuesta["stress_level"].min())
print(Encuesta["stress_level"].max())

#Grafico de barras con nivel de estres del 1 al 10
sns.countplot(x="stress_level", data=Encuesta)
plt.title("Nivel de estres")
plt.savefig("Nivel de estres.png")
plt.show()




#Nivel de felicidad 
nivel_felicidad = Encuesta["happiness_level"].mean()
print(f"El nivel promedio de felicidad es: {nivel_felicidad}")
""" El nivel promedio de felicidad es: 5.538 """

print("MAXIMO Y MINIMO EN NIVEL DE FELICIDAD")
print(Encuesta["happiness_level"].min())
print(Encuesta["happiness_level"].max())

#Grafico de barras con nivel de felicidad del 1 al 10
sns.countplot(x="happiness_level", data=Encuesta)
plt.title("Nivel de felicidad")
plt.savefig("NivelDeFelicidad.png")
plt.show()

#Dias de ejercicios.
cantidad_de_dias_de_ejercicios = Encuesta["exercise_days"].mean()
print(f"En promedio se ejercitan: {cantidad_de_dias_de_ejercicios} dias")
""" En promedio se ejercitan: 3.142 dias """
#Gráfico para observar la frecuencia de la actividad física
sns.countplot(x="exercise_days", data=Encuesta)
plt.title("Actividad Física")
plt.savefig("ActividadFisica.png")
plt.show()
""" Se observa que al menos el 25% de los encuestados tiene una actividad física inexistente o mínima (1 día) """



#Comparaciones por género y país.
print("AGRUPADO POR PAÍS")
print(Encuesta.groupby("country")[["hours_sleep", "age", "screen_time", "stress_level", "happiness_level", "exercise_days"]].mean())
""" 
AGRUPADO POR PAÍS
           hours_sleep        age  screen_time  stress_level  happiness_level  exercise_days
country
argentina     7.048750  43.625000     6.026875      5.750000         5.912500       3.318750
chile         6.960870  40.478261     6.090217      5.543478         5.576087       3.195652
colombia      7.204380  39.620438     5.796350      5.445255         5.759124       3.021898
mexico        6.908284  41.059172     5.995266      5.313609         5.615385       3.195266
peru          7.004469  41.759777     6.039665      5.692737         5.117318       3.061453
spain         6.742105  39.274854     5.858480      5.222222         5.333333       3.046784 """

print("AGRUPADO POR GÉNERO")
print(Encuesta.groupby("gender")[["hours_sleep", "age", "screen_time", "stress_level", "happiness_level", "exercise_days"]].mean())
""" 
AGRUPADO POR GÉNERO
            hours_sleep        age  screen_time  stress_level  happiness_level  exercise_days
gender
female         6.908157  41.102719     6.135952      5.534743         5.534743       3.063444
male           6.903858  41.222552     5.961424      5.682493         5.519288       3.183976
non-binary     7.098193  40.629518     5.828614      5.268072         5.560241       3.177711 """

#Grafico de barras para observar felicidad segun genero
felicidad_por_genero = Encuesta.groupby("gender")["happiness_level"].mean().reset_index()

sns.barplot(data=felicidad_por_genero, x="gender", y="happiness_level")
plt.title("Nivel de felicidad por genero")
plt.xlabel("Generos")
plt.ylabel("Promedio del nivel de felicidad")
plt.savefig("NivelDeFelicidadPorGenero.png")
plt.show()

#Nivel de estres segun genero
estres_por_genero = Encuesta.groupby("gender")["stress_level"].mean().reset_index()
sns.barplot(data=estres_por_genero, x="gender", y="stress_level")
plt.title("Nivel de estres por genero")
plt.xlabel("Generos")
plt.ylabel("Promedio del nivel de estres")
plt.savefig("NivelDeEstresPorGenero.png")
plt.show()

""" Observando los dos gráficos anteriores podemos ver que el nivel de felicidad no cambia mucho de acuerdo
al género, pero en cuando al estrés se observa que los hombres presentan un nivel de estres mas alto con un
promedio de 5,6 aproximadamente, seguidos por las mujeres con un promedio aproximado de 5,5 y por ultimo, 
con el nivel de estres mas bajo se encuentran las personas no binarias con un promedio de 5,2 aproximadamente. """

#Dias de ejercicios
actividad_fisica = Encuesta.groupby("exercise_days")["happiness_level"].mean().reset_index()
sns.barplot(data=actividad_fisica, x="exercise_days", y="happiness_level")
plt.title("Nivel de felicidad segun la actividad fisica")
plt.xlabel("Frecuenia de actividad fisica")
plt.ylabel("Promedio del nivel de felicidad")
plt.savefig("NivelDeFelicidadSegunActividad.png")
plt.show()

print("Cantidad de respuestas 0")
print(Encuesta["exercise_days"].value_counts().sort_index())

""" Luego de ver este gráfico, pude observar que el grupo que no realiza actividad fisica presenta un nivel 
incluso mayor que los que hacen ejercicio. Lo que me llevó a pensar que tal vez el grupo de personas que no realizan
actividad física era muy pequeño, es por eso que me fije en la cantidad de respuestas y no fue el caso. Por lo 
tanto, como no se evidencia una relacion lineal directa entre la cantidad de días de ejericios y el nivel 
de la felicidad en esta muestra, me lleva a pensar que la felicidad puede depender de una combinación mas 
compleja de hábitos.  
  
 """

#Nueva columna ratio screen/sleep
Encuesta["ratio_screen/sleep"] = Encuesta["screen_time"] / Encuesta["hours_sleep"]
print(Encuesta)

mas_pantalla_que_sueño = (Encuesta["ratio_screen/sleep"] > 1).sum()
total_encuestados = len(Encuesta)
porcentaje_mas_pantallas = (mas_pantalla_que_sueño / total_encuestados) * 100

print(f"{porcentaje_mas_pantallas:.2f}% de las personas pasan mas tiempo frente a pantallas que durmiendo")
""" 
37.80% de las personas pasan mas tiempo frente a pantallas que durmiendo.
 """

Encuesta["mas_pantalla_que_sueño"] = Encuesta["ratio_screen/sleep"] > 1
print(Encuesta)

#Boxplot para observar nivel de felicidad segun la relacion pantalla/sueño
sns.boxplot(data=Encuesta, x= "mas_pantalla_que_sueño", y= "happiness_level")
plt.title("Felicidad según la razon pantalla/sueño")
plt.xlabel("Mas tiempo en pantallas que durmiendo")
plt.ylabel("Nivel de felicidad")
plt.savefig("FelicidadSegunRazonPantallaTiempo.png")
plt.show()

""" En este gráfico no se observa un impacto significativo en el nivel de felicidad segun la relacion 
pantalla/sueño.
La mediana, en el grupo con mayor exposicion a las pantallas, tiende a estar un poquito mas baja pero no es 
mucha la diferencia. Esto nos podria insinuar que malos habitos en el sueño y pantallas tendrían un leve
impacto negativo en el nivel de felicidad"""

#Boxplot para observar nivel de estres segun relación pantalla/sueño
sns.boxplot(data=Encuesta, x= "mas_pantalla_que_sueño", y= "stress_level")
plt.title("Estres según la razon pantalla/sueño")
plt.xlabel("Mas tiempo en pantallas que durmiendo")
plt.ylabel("Nivel de Estres")
plt.savefig("EstresSegunRazonPantallaTiempo.png")
plt.show()

""" En este grafico se observa que la mediana del grupo con mayor exposicion de pantallas esta mas alta,
esto me indica que se observa mayor nivel de estres en las personas que pasan mas horas frente a una 
pantalla que durmiendo con respecto a las personas que duermen mas tiempo del que estan frente a una pantalla.
El grafico muestra que el 50% de los encuestados que pasan mas tiempo frente a una pantalla que durmiendo,
presentan un nivel de estres igual o superior a 6 puntos aproximadamente.
  """

#Grupos en riesgo
#Nueva columna
Encuesta["en_riesgo"] = ((Encuesta["screen_time"]>6) & (Encuesta["hours_sleep"]<7) & (Encuesta["stress_level"]>6))

total_en_riesgo = Encuesta["en_riesgo"].sum()
porcentaje_en_riesgo = (total_en_riesgo/len(Encuesta)) * 100
print(f"El {porcentaje_en_riesgo:2f}% de los encuestados están en riesgo")
""" 
El 10.483871% de los encuestados están en riesgo.

¿Que tuve en cuenta para considerar una persona en riesgo?
Usé los siguientes parámetros para encontrar personas en riesgo (obtuve esos valores de la media)
-tiempo de pantalla > 6
-horas de sueño < 7
-nivel de estres > 6
 """
Encuesta.to_csv("EncuestaBienestarLimpioActualizada.csv", index=False)

print(Encuesta["screen_time"].mean())