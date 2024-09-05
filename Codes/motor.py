from gpiozero import Motor, PWMOutputDevice
from time import sleep

# Define GPIO pins for motor control
in1 = 17  # GPIO pin for forward direction
in2 = 18  # GPIO pin for backward direction
en = 12   # GPIO pin for enabling PWM (speed control)

# Initialize the Motor object with defined GPIO pins
# 'forward' corresponds to the pin that makes the motor move forward
# 'backward' corresponds to the pin that makes the motor move backward
motor = Motor(forward=in1, backward=in2)

# Create a PWMOutputDevice object for speed control on the enable pin (en)
# PWM allows control over the motor's speed by adjusting the duty cycle
speed = PWMOutputDevice(en)

# Set the default motor speed to 25% (value between 0 and 1)
speed.value = 0.25

# Display instructions for the user
print("\nThe default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit\n")

# Start an infinite loop to take user input and control the motor
while True:
    # Take user input (stripping any extra spaces)
    x = input().strip()

    # Check user input to determine motor action
    if x == 'r':
        # Run the motor in the forward direction
        print("run")
        motor.forward()  # Motor starts moving forward
    elif x == 's':
        # Stop the motor
        print("stop")
        motor.stop()  # Motor stops
    elif x == 'f':
        # Set the motor to move forward
        print("forward")
        motor.forward()  # Motor runs forward
        print("Motor running forward")
    elif x == 'b':
        # Set the motor to move backward
        print("backward")
        motor.backward()  # Motor runs backward
        print("Motor running backward")
    elif x == 'l':
        # Set motor speed to low (25% of max speed)
        print("low")
        speed.value = 0.25  # Low speed
        print("Speed set to low")
    elif x == 'm':
        # Set motor speed to medium (60% of max speed)
        print("medium")
        speed.value = 0.6  # Medium speed
        print("Speed set to medium")
    elif x == 'h':
        # Set motor speed to high (100% of max speed)
        print("high")
        speed.value = 1  # High speed (full speed)
        print("Speed set to high")
    elif x == 'e':
        # Exit the loop and stop the motor
        print("Exiting and cleaning up GPIO")
        motor.stop()  # Stop the motor
        break  # Exit the loop and stop the program
    else:
        # Handle invalid input
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
