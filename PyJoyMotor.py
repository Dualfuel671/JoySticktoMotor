import pygame
import RPi.GPIO as GPIO

# Set up GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)  # PWM pin for motor

# Initialize Pygame joystick
pygame.init()
pygame.joystick.init()

# Set up joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Set up PWM
pwm = GPIO.PWM(11, 100)  # 100 Hz frequency
pwm.start(0)  # 0% duty cycle initially

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYAXISMOTION:
            # Get joystick values
            x_axis = joystick.get_axis(0)
            y_axis = joystick.get_axis(1)
            
            # Convert joystick values to motor speed and direction
            speed = abs(y_axis) * 100
            if y_axis < 0:
                direction = GPIO.HIGH  # Forward
            else:
                direction = GPIO.LOW  # Backward
            
            # Set motor speed and direction
            GPIO.output(11, direction)
            pwm.ChangeDutyCycle(speed)
            
        elif event.type == pygame.JOYBUTTONUP:
            # Stop motor when joystick button is released
            GPIO.output(11, GPIO.LOW)
            pwm.ChangeDutyCycle(0)
