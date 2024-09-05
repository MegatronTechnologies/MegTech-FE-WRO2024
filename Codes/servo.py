from gpiozero import Servo
from time import sleep

# Create a Servo object on GPIO pin 25 with a custom pulse width range
# The pulse width range determines how much the servo can move
# The min_pulse_width and max_pulse_width define the minimum and maximum positions of the servo
# For example, min_pulse_width=0.0005 means 0.5 ms pulse (minimum position), max_pulse_width=0.0025 means 2.5 ms pulse (maximum position)
servo = Servo(25, min_pulse_width=0.0005, max_pulse_width=0.0025)

# Infinite loop to continuously move the servo between its maximum, mid, and minimum positions
while True:
    # Move the servo to the maximum position
    servo.max()  # This corresponds to the maximum pulse width, turning the servo to its full range in one direction
    sleep(2)     # Wait for 2 seconds before the next command

    # Move the servo to the middle (neutral) position
    servo.mid()  # This corresponds to the middle of the servo's range
    sleep(2)     # Wait for 2 seconds before the next command

    # Move the servo to the minimum position
    servo.min()  # This corresponds to the minimum pulse width, turning the servo to its full range in the opposite direction
    sleep(2)     # Wait for 2 seconds before the next command

    # Return the servo to the middle position
    servo.mid()  # Back to the middle (neutral) position
    sleep(2)     # Wait for 2 seconds before repeating the loop
