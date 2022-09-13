# Micropython LCD1602/LCD2004-I2C Lib

This is a micropython library for using LCD1602 or LCD2004 screen with PCF8574 I2C chip attached. It is modified from a module of [micropython Chinese Community repository](https://github.com/micropython-Chinese-Community/mpy-lib/blob/master/lcd/I2C_LCD1602/mp_i2c_lcd1602.py), with the added feature of creating custom characters and increased efficiency (by about 5~10 times faster for LCD2004 screen).

## Usage
### Hardware connection
 * Connect your micropython device as follow (my tests uses WEMOS LOLIN32 Lite):
    * PCF8574 I2C chip GND - ESP32 GND
    * PCF8574 I2C chip VCC - ESP32 +5V
    * PCF8574 I2C chip SCL - ESP32 GPIO pin 26 (pick your own pin, then modify the GPIO pin number in the code)
    * PCF8574 I2C chip SDA - ESP32 GPIO pin 27 (pick your own pin, then modify the GPIO pin number in the code)
    * If your PCF8574 and LCD scrren comes separately, solder the PCF8574 I2C chip to the screen per the manual.

 * Power-up your ESP32 board, adjust the contrast pot on the I2C chip until you see a line of solid blocks and an empty line.

 * Write your code, name it main.py.
 * Upload main.py and lib_lcd1602_2004_with_i2c.py to your board. Reboot.


### Hello world

Call the `LCD` class with a `Pin` object of your SCL and SDA pin, then write character to the screen by using the `.puts()` method.

By default, `.puts(string)` writes to the left-top corner of the screen. You can designate the start position with `.puts(string, row, column)`.

You need to write each line separately.

```
from machine import Pin, SoftI2C
from lib_lcd1602_2004_with_i2c import LCD
scl_pin = 26 # write your own pin number
sda_pin = 27 # write your own pin number
lcd = LCD(SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000))
lcd.puts("Hello, World!")
```
<p align=center>
<img src="https://user-images.githubusercontent.com/18537705/155820147-1fcdcd3e-2edc-4942-b9d4-e727b0dae8e8.png" width="300">
</p>

`lcd.puts("Hello, World!",1)` will put the text in the second line.

`lcd.puts("Hello, World!",2,4)` will put the text in the third line, starts from the fifth column.

### Custom character
A custom character is defined with a 5×8 binary matrix, for example:
```
custom_char = [
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b00000,
  0b11111]
```
Then created with:
```
lcd.create_charactor(position,custom_char)
```
The position can only be between 0 and 7 (you can only create 8 custom characters). The new characters are treated as normal ASCII of 0x00~0x07. For example, if a custom character is created by calling `lcd.create_charactor(5,custom_char)`, a normal python string containing `chr(5)` will be rendered with the character you just defined in position 5.

Once created, rendering custom characters requires the same time as any other standard ASCII character.

Example file `main_Custom_Character_Example.py` will produce an animation then render the following screen:

<p align=center>
<img src="https://user-images.githubusercontent.com/18537705/155820648-2fa684ba-9e60-4b55-b46b-30901257c3ee.png" width="300">
</p>.

Here is another [more practical example](https://github.com/liyuanhe211/ESP32_LCD2004_with_5_AHT10_probes) of using custom characters to show a bar-chart for multiple temperature and humidity probes on a LCD2004 screen.

<p align=center>
<img src="https://user-images.githubusercontent.com/18537705/155855075-88fdf70e-0384-4318-a08b-0ea94824b8ea.png" width="300">
</p>.

