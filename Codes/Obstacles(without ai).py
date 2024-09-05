from gpiozero import Motor, PWMOutputDevice, DistanceSensor, Servo, Button
from time import sleep

# Define GPIO pins for motor control and sensors
in1 = 18  # GPIO pin for motor forward direction
in2 = 17  # GPIO pin for motor backward direction
en = 12   # GPIO pin for motor speed (PWM control)

# Define GPIO pins for ultrasonic sensors
FRONT_TRIG = 23  # Trigger pin for the front ultrasonic sensor
FRONT_ECHO = 24  # Echo pin for the front ultrasonic sensor
LEFT_TRIG = 16   # Trigger pin for the left ultrasonic sensor
LEFT_ECHO = 19   # Echo pin for the left ultrasonic sensor
RIGHT_TRIG = 5   # Trigger pin for the right ultrasonic sensor
RIGHT_ECHO = 6   # Echo pin for the right ultrasonic sensor
BUTTON_PIN = 21  # GPIO pin for the button

# Initialize servo motor on GPIO pin 25
# Custom pulse width is set for full servo motion
servo = Servo(25, min_pulse_width=0.0005, max_pulse_width=0.0025)
servo.mid()  # Set servo to its middle (neutral) position

# Initialize motor with forward and backward GPIO pins
motor = Motor(forward=in1, backward=in2)

# Initialize PWM output for motor speed control
speed = PWMOutputDevice(en)

# Set initial motor speed to 70% (0.7 out of 1.0)
speed.value = 0.7

# Create DistanceSensor objects for front, left, and right sensors
# These sensors measure distance by sending a pulse (trigger) and listening for an echo
front_sensor = DistanceSensor(echo=FRONT_ECHO, trigger=FRONT_TRIG)
left_sensor = DistanceSensor(echo=LEFT_ECHO, trigger=LEFT_TRIG)
right_sensor = DistanceSensor(echo=RIGHT_ECHO, trigger=RIGHT_TRIG)

# Initialize the button for starting the race
button = Button(BUTTON_PIN)

# Allowable tolerance in distance difference between left and right sensors (in cm)
TOLERANCE = 10

# Flag to indicate if a turn is in progress (prevents corrections while turning)
turn_in_progress = False

# Function to maintain the car's central position between two walls
def keep_center():
    global turn_in_progress
    
    # Do not adjust the car's position if a turn is already in progress
    if turn_in_progress:
        return
    
    # Get distances from left and right walls (convert sensor readings to centimeters)
    left_distance = left_sensor.distance * 100
    right_distance = right_sensor.distance * 100
   
    # If the car is too close to the left wall
    if left_distance - right_distance > TOLERANCE:
        servo.max()  # Turn the wheels to the right
        speed.value = 0.5  # Slow down to avoid over-correction
        sleep(1)  # Pause to allow the car to adjust
        servo.mid()  # Return the wheels to the center
        speed.value = 0.7  # Resume normal speed
    # If the car is too close to the right wall
    elif right_distance - left_distance > TOLERANCE:
        servo.min()  # Turn the wheels to the left
        speed.value = 0.5  # Slow down for better control
        sleep(1)  # Allow time for the car to adjust
        servo.mid()  # Return wheels to the center position
        speed.value = 0.7  # Resume normal speed

# Function to complete one lap around the course
def complete_lap():
    global turn_in_progress
    turns_made = 0  # Counter for the number of turns made during the lap
    
    # The lap consists of four turns, continue until four turns are completed
    while turns_made < 4:
        motor.forward()  # Move the car forward
        keep_center()  # Adjust the car's position to stay centered between walls
       
        front_distance = front_sensor.distance * 100  # Measure distance to obstacle in front
       
        if front_distance <= 80:  # If an obstacle is detected at less than 80 cm
            speed.value = 0.5  # Slow down the car
        if front_distance <= 70:  # If the obstacle is very close (less than 70 cm)
            turn_in_progress = True  # Set flag to indicate a turn is starting
            servo.min()  # Turn the wheels to the left to start a turn
            sleep(2.4)  # Time to complete the turn (this may require adjustment)
            servo.mid()  # Return wheels to the center after the turn
            speed.value = 0.7  # Resume full speed
            turns_made += 1  # Increment the number of turns completed
            sleep(1)  # Brief pause before resuming
            turn_in_progress = False  # Reset turn flag after the turn is complete
        sleep(0.1)  # Small delay for smoother sensor readings

# Function to start the race and complete 3 laps
def start_race():
    for _ in range(3):  # Repeat the lap 3 times (for a total of 3 laps)
        complete_lap()
    motor.stop()  # Stop the motor after completing the laps
    speed.off()  # Turn off the speed control (PWM)

# Wait for the button press to start the race
button.wait_for_press()
start_race()  # Start the race after the button is pressed
