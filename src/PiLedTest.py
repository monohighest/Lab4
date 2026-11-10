
import time
from hal import hal_led as led
from hal import hal_input_switch as switch

led.init()
switch.init()

start_time = None

try:
    while True:
        if switch.read_slide_switch() == 0:
            start_time = None
            delay = 0.1

        else:
            if start_time is None:
                start_time = time.monotonic()

            if time.monotonic() - start_time >= 5:
                led.set_output(0, 0)
                time.sleep(0.01)
                continue

            delay = 0.05

        led.set_output(0, 1)
        time.sleep(delay)
        led.set_output(0, 0)
        time.sleep(delay)

except KeyboardInterrupt:
    led.set_output(0, 0)
