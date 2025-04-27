import pigpio
import time

pi = pigpio.pi()

# Mapping GPIOs to channels
channels = {
    'throttle': 17,
    'yaw': 18,
    'pitch': 27,
    'roll': 22
}

# Set all to middle (1500 us = neutre)
for ch in channels.values():
    pi.set_servo_pulsewidth(ch, 1500)

try:
    while True:
        # Example: Increase throttle slowly
        for pulse in range(1000, 2000, 10):
            pi.set_servo_pulsewidth(channels['throttle'], pulse)
            time.sleep(0.05)

except KeyboardInterrupt:
    print("Stopping")
    for ch in channels.values():
        pi.set_servo_pulsewidth(ch, 0)
    pi.stop()
