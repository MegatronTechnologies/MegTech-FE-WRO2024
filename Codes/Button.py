from gpiozero import Button
from signal import pause

# Initialize a counter variable starting at 0
counter = 0

# Initialize a boolean system state variable
system = False

# Set up a button connected to GPIO 21
button = Button(21)

# Define a function that will be called every time the button is pressed
def increment_counter():
    global counter, system  # Use the global variables 'counter' and 'system'
    
    # Increment the counter by 1 each time the button is pressed
    counter += 1
    
    # Check if the counter is odd or even
    # If the counter is odd, set 'system' to True
    if counter % 2 != 0:
        system = True
    # If the counter is even, set 'system' to False
    elif counter % 2 == 0:
        system = False
    
    # Print the current state of the 'system' variable (True or False)
    print(system)

# Attach the 'increment_counter' function to the button's 'when_pressed' event
# This means the function will be called every time the button is pressed
button.when_pressed = increment_counter

# Pause the program to keep it running, waiting for the button press
# Without this, the program would exit immediately after starting
pause()
