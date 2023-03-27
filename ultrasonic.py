import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)  # Use Broadcom pin numbers
GPIO_TRIGGER1 = 23      # Set the trigger pin for sensor 1
GPIO_ECHO1 = 24         # Set the echo pin for sensor 1
GPIO_TRIGGER2 = 17      # Set the trigger pin for sensor 2
GPIO_ECHO2 = 27         # Set the echo pin for sensor 2
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)  # Set trigger pin as output
GPIO.setup(GPIO_ECHO1, GPIO.IN)     # Set echo pin as input
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)  # Set trigger pin as output
GPIO.setup(GPIO_ECHO2, GPIO.IN)     # Set echo pin as input

# Define function to measure distance
def distance(GPIO_TRIGGER, GPIO_ECHO):
    # Send ultrasonic signal
    GPIO.output(GPIO_TRIGGER, True)     # Set trigger pin high
    time.sleep(0.00001)                 # Wait for 10 microseconds
    GPIO.output(GPIO_TRIGGER, False)    # Set trigger pin low

    # Record the time of signal sent and received
    start_time = time.time()            # Record start time
    stop_time = time.time()             # Record stop time

    # Get the start time of the signal return
    while GPIO.input(GPIO_ECHO) == 0:   # Wait for signal
        start_time = time.time()        # Record start time

    # Get the time of the signal return
    while GPIO.input(GPIO_ECHO) == 1:   # Wait for signal end
        stop_time = time.time()         # Record stop time

    # Calculate distance
    time_elapsed = stop_time - start_time  # Calculate time elapsed
    distance = (time_elapsed * 34300) / 2  # Calculate distance in cm

    return distance

# Main loop
try:
    while True:
        dist1 = distance(GPIO_TRIGGER1, GPIO_ECHO1)  # Measure distance for sensor 1
        dist2 = distance(GPIO_TRIGGER2, GPIO_ECHO2)  # Measure distance for sensor 2
        print("Distance 1: {:.1f} cm".format(dist1)) # Print distance for sensor 1
        print("Distance 2: {:.1f} cm".format(dist2)) # Print distance for sensor 2
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    # Clean up GPIO pins
    GPIO.cleanup()  # Reset GPIO settings to default

