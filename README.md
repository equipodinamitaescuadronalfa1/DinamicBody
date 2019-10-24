# Modelación de *De la Tierra a la Luna* de Julio Verne

## Ejecución

Para poder ejecutar el programa, se necesita instalar tqdm y matplotlib:
```sh
pip3 install tqdm
```
```sh
pip3 install matplotlib
```
Para ejecutar el programa, corre esta linea:
```sh
python3 DinamicBody.py
```
## Introducción 

¿Es posible enviar un proyectil a la luna? Fue lo que se preguntó Julio Verne en su libro *De la Tierra a la Luna* (1865), en él imagino una manera teórica de hacerlo con ayuda de unos parámetros explicados en su libro y funcionó. Pero, ¿Funcionaria en la vida real? ¿Qué tan acertado fue Verne?

Bueno eso fue lo que nos preguntamos así que simularemos el lanzamiento de un cohete con destino a la luna con los parámetros que Verne consideró. 

## Objetivo

Realizar la simulación de un cohete con destino a la luna con los parámetros descritos en el libro de Julio Verne “De la Tierra a la Luna” para ver si son correctos o no.

## Resultados

Estos son los resultados de la modelación por toda la duración de la trayectoria de la bala. Para motivos de visualización solo fueron graficadas las 57 primeras horas de la bala.
![alt text](https://github.com/equipodinamitaescuadronalfa1/DinamicBody/blob/master/Figure_1.png "Results")

## Concluciones

Dadas las condiciones iniciales proporcionadas a nosotros por Julio Verne, vemos que no es posible lanzar una bala de la Tierra a la Luna con esas condiciones. Después de 28 horas de viaje la bala alcanza su punto más cercano a la Luna a una distancia de 148,040,716m de la Tierra, eso es a 18,937,265m de distancia a la Luna.

Para mejorar el proyecto, se podría hacer una animación de la trayectoria de la bala para que quede más clara la visualización. También se podría hacer los calculos de la fuerza inicial de la bala necesaria para poder lograr alcanzar la Luna.
