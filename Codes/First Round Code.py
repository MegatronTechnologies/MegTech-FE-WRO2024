from gpiozero import Motor, PWMOutputDevice, DistanceSensor, Servo, Button
from time import sleep

# Define GPIO pins for the left motor
left_in1 = 18
left_in2 = 17
left_en = 12

# Define GPIO pins for the right motor
right_in1 = 9
right_in2 = 10
right_en = 11

# Define GPIO pins for sensors and servo
FRONT_TRIG = 23
FRONT_ECHO = 24
LEFT_TRIG = 16
LEFT_ECHO = 19
RIGHT_TRIG = 5
RIGHT_ECHO = 6
BUTTON_PIN = 21

# Initialize servo with custom pulse range
servo = Servo(25, min_pulse_width=0.0005, max_pulse_width=0.0025)
servo.mid()

# Initialize left and right motors
left_motor = Motor(forward=left_in1, backward=left_in2)
right_motor = Motor(forward=right_in1, backward=right_in2)

# Initialize speed control for both motors
left_speed = PWMOutputDevice(left_en)
right_speed = PWMOutputDevice(right_en)

# Set initial motor speed
left_speed.value = 0.4
right_speed.value = 0.4

# Create DistanceSensor objects for the front, left, and right sensors
front_sensor = DistanceSensor(echo=FRONT_ECHO, trigger=FRONT_TRIG)
left_sensor = DistanceSensor(echo=LEFT_ECHO, trigger=LEFT_TRIG)
right_sensor = DistanceSensor(echo=RIGHT_ECHO, trigger=RIGHT_TRIG)

# Initialize button
button = Button(BUTTON_PIN)

# Allowable tolerance for sensor readings (in cm)
TOLERANCE = 35
Max_TOLERANCE = 78

# Flag for managing turns
turn_in_progress = False

# Function to maintain center position based on side sensors
def keep_center():
    global turn_in_progress
    
    # Exit if a main turn is in progress`
    if turn_in_progress:
        return
    
    left_distance = left_sensor.distance * 100  # Convert to cm
    right_distance = right_sensor.distance * 100  # Convert to cm
    
    if left_distance - right_distance > TOLERANCE and left_distance - right_distance < Max_TOLERANCE:  # Too close to the left wall
        servo.max()  # Turn right to center
        sleep(0.2)
        servo.mid()
    elif right_distance - left_distance > TOLERANCE and right_distance - left_distance < Max_TOLERANCE:  # Too close to the right wall
        servo.min()  # Turn left to center
        sleep(0.2)
        servo.mid()
        
    sleep(1)

# Function to perform one lap
def complete_lap():
    global turn_in_progress
    turns_made = 0  # Count the number of turns
    while turns_made < 4:
        left_motor.forward()
        right_motor.forward()
        keep_center()
        
        front_distance = front_sensor.distance * 100  # Distance in front
        
        if front_distance <= 98:  # Too close to obstacle
            turn_in_progress = True  # Start main turn
            servo.min()  # Turn left (adjust as needed)
            right_speed.value = 0.5
            left_speed.value = 0.7
            sleep(1.4)
            servo.mid()  # Return wheels to straight
            right_speed.value = 0.4
            left_speed.value = 0.4  # Restore speed
            turns_made += 1  # Increment turn counter
            turn_in_progress = False  # Finish turn  
        sleep(0.1)

# Main function to perform 3 laps
def start_race():
    for _ in range(3):  # Perform 3 laps
        complete_lap()
    left_motor.stop()
    right_motor.stop()
    left_speed.off()
    right_speed.off()

# Wait for button press to start
button.wait_for_press()
sleep(0.5)
start_race()
