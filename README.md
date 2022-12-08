# P7-Humedad
##Introducción
La finalidad de esta práctica es implementar un programa que sea capaz de mostrar al usuario el estado de una planta de forma práctica y sin complicaciones. 

##Componentes
Para realizar esta práctica, hemos utilizado el sensor de humedad de suelo que viene junto con un módulo comparador modelo [LM393](https://github.com/clases-julio/p7-humedad-rsanchez2021/blob/main/lm393-datasheet.pdf). En total, hemos uilizado:
- Sensor de humedad
- Módulo comparador
- [Liquid Crystal Display](https://www.arduino.cc/documents/datasheets/LCDscreen.PDF)
- [Potenciómetro](http://www.datasheet.es/PDF/866979/RV24AF-10-15R1-B1K-pdf.html)

## Circuito
Para conectar el sensor con el módulo y la placa se ha seguido las espicificaciones del enuncuiado, en específiuco, el pin VCC se ha conectado a 5V, el GND a tierra y se ha utilizado en pin DO que se ha conectado a un GPIO. La señal  que nos vierte el pin DO es de 1 o 0 en función de si la humedad sensada supera el umbral determiado, el cual se puede modificar en el  módulo comparador girando una pieza. 

Además, hemos querido añadir un display donde se muestren dos mensajes dependiendo de la humedad: en el caso de tener mucha humedad se muestra el mensaje "Me ahogo :)" y por el contrario, si no tiene suficiente agua se muestra "Dame más agua :(", como se muestra en la siguiente imagen: 

![Mensaje display](https://github.com/rsanchez2021/Image/blob/main/p7%20display.PNG)

## Circuito y programación
Para conectar el display a la placa y su programación se ha seguido la siguiente [página web](https://pimylifeup.com/raspberry-pi-lcd-16x2/) donde se explica detalladamente los pasos a seguir, que en resumen es descargar la librería [**Adafruit_Python_CharLCD**](https://github.com/pimylifeup/Adafruit_Python_CharLCD.git) e implementarla en el código de la siguiente manera:
```python
import Adafruit_CharLCD as LCD
```

Además, es la misma página, se muestra el código necesario para que funcione y las conexiones del display con la placa, según la siguiente imágen: 

![Circuito display](https://cdn.pimylifeup.com/wp-content/uploads/2016/09/Raspberry-Pi-LCD-16x2-Circuit-Diagram-v1.png)

En cuanto al sensor de humedad, lo más sencillo que nos ha parecido es realizarlo como si fuese un input, es decir, si el pin recibe señal (1) se refiere a que hay humedad y se muestra el mensaje correspondiente, por el contrario, si no recibe señal (0) se reconoce como que no hay humedad y se muestra el mensaje correspondiente. Tener en cuenta también, que para este programa el pin del sensor se ha declarado como:
```python
d0_input = DigitalInputDevice(15)
```

Finalmente, ya que en la práctica se pedía hacer el ejercicio lo más sencillo para el usuario, hemos añadido que nada más encender la placa o reiniciarla se ejecute el programa solo, para ello, hemos encotnrado varios métodos representados en esta [página](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/). El más común es mediante el archivo rc.local, pero no conseguimos hacerlo, así pues, utilizamos l método .bashrc . Este se basa en editar el archivo .bashrc de la placa y añadir al final de todo lo siguiete:
```bash
echo Running at boot
sudo python /home/pi/p7-humedad-rsanchez2021/ejercicio1.py
```
Una vez guardado, cada vez que se encienda la placa o se reinicie el programa se ejecutará solo. Para poder pararlo bastará con abrir la terminal y hacer Ctrl+C. 

## Casos de uso

Algunas veces, el display muestra caracteres raros hasta que se carga del todo el programa, la solución es un sleep de varios segundos para que le de tiempo a cargar del todo.

El display lleva además un potenciómetro para la intensidad de la pantalla, si este está totalmente girado en el display no aparecen los mensajes y habría que calibrar el potenciómetro. 
