#------------------------------
#Ejercicio: Práctica p7 sensores y actuadores --> Sensor humedad
#Autores: Jorge Martín y Rebeca Sánchez
#Fecha límite de entrega: 7/12/22
#Objetivo: leer los valores del módulo FC-28
#------------------------------
#!/usr/bin/python
from gpiozero import DigitalInputDevice
import Adafruit_CharLCD as LCD #biblioteca display
import time


#establecer pines
d0_input = DigitalInputDevice(15)

# Raspberry Pi pin setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

lcd.clear()

while True:
    if (not d0_input.value):
        lcd.message('Dame más agua :(')
        print (d0_input.value)
        time.sleep(2)
        lcd.clear()
    else:
        lcd.message('Me ahogo :)')
        print (d0_input.value)
        time.sleep(2)
        lcd.clear()
		

