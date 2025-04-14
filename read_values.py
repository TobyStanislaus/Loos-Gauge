import time
import RPi.GPIO as GPIO
from hx711 import HX711

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

hx = HX711(5, 6)  # DOUT = 5, SCK = 6

# Reset and zero manually
hx.reset()

print("Start reading values from strain gauge (raw output)")

# You can capture a baseline (for "tare") manually if you like
baseline = hx.get_value(10)
print(f"Baseline (tare): {baseline}")

while True:
    try:
        val = hx.get_value(5)
        weight = val - baseline  # simulate tare
        print(f"Weight (raw adjusted): {weight}")
        time.sleep(0.1)
    except (KeyboardInterrupt, SystemExit):
        GPIO.cleanup()
        break
