from gpiozero import DistanceSensor
from time import sleep

# Define GPIO pins for HC-SR04 sensors
# These are the GPIO pins to which the HC-SR04 ultrasonic sensors are connected
TRIG_front = 23  # Trigger pin for the front sensor
ECHO_front = 24  # Echo pin for the front sensor
TRIG_left = 16   # Trigger pin for the left sensor
ECHO_left = 19   # Echo pin for the left sensor
TRIG_right = 5   # Trigger pin for the right sensor
ECHO_right = 6   # Echo pin for the right sensor

# Create DistanceSensor objects for each sensor
# The DistanceSensor class from gpiozero handles the timing and calculations to determine the distance
sensor_front = DistanceSensor(echo=ECHO_front, trigger=TRIG_front)  # Front sensor
sensor_left = DistanceSensor(echo=ECHO_left, trigger=TRIG_left)     # Left sensor
sensor_right = DistanceSensor(echo=ECHO_right, trigger=TRIG_right)  # Right sensor

try:
    # Infinite loop to continuously read the sensor values
    while True:
        # Read distance from the front sensor, in meters, then convert to centimeters
        distance_front = sensor_front.distance * 100  # Multiply by 100 to convert from meters to centimeters

        # Read distance from the left sensor, in meters, then convert to centimeters
        distance_left = sensor_left.distance * 100  # Convert to centimeters

        # Read distance from the right sensor, in meters, then convert to centimeters
        distance_right = sensor_right.distance * 100  # Convert to centimeters

        # Print the distances to the console with two decimal places
        print(f"Front Distance: {distance_front:.2f} cm, Left Distance: {distance_left:.2f} cm, Right Distance: {distance_right:.2f} cm")

        # Pause for 1 second before the next measurement
        sleep(1)

except KeyboardInterrupt:
    # When the user interrupts the program (Ctrl + C), the loop stops and this message is printed
    print("Measurement stopped by User")
