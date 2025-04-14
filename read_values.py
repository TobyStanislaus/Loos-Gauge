import time
import RPi.GPIO as GPIO
from hx711 import HX711

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

hx = HX711(5, 6)  # DOUT = GPIO 5, SCK = GPIO 6

hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(1)  # You’ll need to calibrate this later

hx.reset()
hx.tare()

print("Tare done. Start reading values...")

while True:
    try:
        val = hx.get_weight(5)
        print(f"Weight: {val} grams")
        time.sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        GPIO.cleanup()
        break
