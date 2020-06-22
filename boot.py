import machine
from machine import Pin, Timer
import ssd1306
import font6
from writer import Writer


OLED_WIDTH = 128
OLED_HEIGHT = 64
PinScl = Pin(14)
PinSda = Pin(2)

def page2(tim):
    tim.deinit()
    oled.fill(0)
    Writer.set_textpos(oled, 15, 0)
    wrtr.printstring("Line 2y")
    Writer.set_textpos(oled, 30, 0)
    wrtr.printstring("Line 3y")
    Writer.set_textpos(oled, 45, 0)
    wrtr.printstring("Line 4y")
    oled.show()
    tim.init(period=3 * 1000, mode=Timer.ONE_SHOT, callback=page3)
    
def page3(tim):
    oled.poweroff()
    tim.init(period=3 * 1000, mode=Timer.ONE_SHOT, callback=page4)

def page4(tim):
    oled.poweron()
    tim.init(period=3 * 1000, mode=Timer.ONE_SHOT, callback=page5)
    # tim.init(period=3 * 1000, mode=Timer.ONE_SHOT, callback=page4)

def page5(tim):
    oled.invert(1)
    tim.init(period=3 * 1000, mode=Timer.ONE_SHOT, callback=page6)

def page6(tim):
    oled.poweroff()

i2c = machine.I2C(-1, PinScl, PinSda)
print ('')
print (i2c.scan())
oled = ssd1306.SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)
wrtr = Writer(oled, font6)
Writer.set_textpos(oled, 0, 0)
wrtr.printstring("Hello World!")
oled.show()
tim = Timer(-1)
tim.init(period=3 * 1000, mode=Timer.ONE_SHOT, callback=page2)
