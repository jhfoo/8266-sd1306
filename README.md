# 8266-sd1306
Sample micropython working code to use the SD1306 display 

## User requirements
- Able to write simple micropython code
- Have working development environment to upload code to device
- Patience to read documents (not just this one)

## Installation
- Use your favourite uploader for the job; no specific requirements. I use pymakr extension on Visual Studio Code.
- Reboot

## Compile your own module
- Download the micropython git repo to your Linux machine (Debian tested supported).
- Compile [mpy-cross](https://github.com/micropython/micropython/tree/master/mpy-cross)
~~~sh
cd mpy-cross
make
~~~
- Compile any module you like. 'xtensa' is the architecture for ESP8266. Some fonts are available [here](https://github.com/peterhinch/micropython-font-to-py/tree/master/writer) for compiling.
~~~sh
mpy-cross -march=xtensa <module.py>
~~~

## Technical config/ specs
- SDA = GPIO02
- SCL = GPIO14
- OLED pixels (width x height) = 128 x 64

## References
- Hardware
  - [Board schematics - DISCLAIMER: not affiliated with site or seller](http://myosuploads3.banggood.com/products/20190510/20190510050818IOTESP8266V1.0Schematic.pdf)
  - [Development tools - YMMV](http://myosuploads3.banggood.com/products/20190730/20190730233053ESP8266-IOT-Tutorial.rar)
  - [Geekcreit® ESP8266 IoT Development Board +DHT11 Temperature and Humidity + Yellow Blue OLED Display SDK Programming Wifi Module](https://usa.banggood.com/Geekcreit-ESP8266-IoT-Development-Board-DHT11-Temperature-and-Humidity-Yellow-Blue-OLED-Display-SDK-Programming-Wifi-Module-p-1471313.html?cur_warehouse=CN)
- Software
  - [A very useful forum thread](https://forum.micropython.org/viewtopic.php?t=5589)
  - [Writer and Cwriter classes](https://github.com/peterhinch/micropython-font-to-py/blob/master/writer/WRITER.md)
  - [MicroPython font handling](https://github.com/peterhinch/micropython-font-to-py)
  - [SSD1306 driver module](https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py)
  - [MicroPython cross compiler](https://github.com/micropython/micropython/tree/master/mpy-cross)
  - [Micropython I2C class](https://docs.micropython.org/en/latest/library/machine.I2C.html)
