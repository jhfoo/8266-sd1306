import machine
from machine import Pin
import ssd1306
import font6
from writer import Writer


OLED_WIDTH = 128
OLED_HEIGHT = 64
PinScl = Pin(14)
PinSda = Pin(2)

i2c = machine.I2C(-1, PinScl, PinSda)
print ('')
print (i2c.scan())
oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)
wrtr = Writer(oled, font6)
Writer.set_textpos(oled, 0, 0)
wrtr.printstring("Hello World!")
Writer.set_textpos(oled, 15, 0)
wrtr.printstring("Line 2y")
Writer.set_textpos(oled, 30, 0)
wrtr.printstring("Line 3y")
Writer.set_textpos(oled, 45, 0)
wrtr.printstring("Line 4y")
oled.show()