# MegTech FE WRO2024

----------------------------------------------------------------------------------Autonomous Vehicle for Competition Challenge------------------------------------------------------------------------------------------

Introduction
This repository contains the code and design specifications for an autonomous vehicle designed to participate in a multi-stage competition. The vehicle is equipped with various electromechanical components and advanced sensors to navigate between walls, avoid obstacles, and park between designated areas. The project combines AI-based navigation with real-time sensor feedback, ensuring precision and adaptability to different racing conditions.

The competition consists of four races, where points are awarded based on the vehicle’s performance in completing laps. Each race includes three laps, and the environment becomes progressively more challenging. In the final two races, the vehicle must avoid obstacles of various colors and demonstrate its ability to park accurately. The vehicle that accumulates the most points wins the competition.

---

------------------------------------------------------------------------------------------------Vehicle Overview--------------------------------------------------------------------------------------------------------

The vehicle is powered by a 6000 mAh battery, which ensures it can complete all the races on a single charge with ample energy remaining. The propulsion system consists of two DC motors mounted on the rear axle, controlled by an L298N motor driver capable of handling high voltage and current. The steering is handled by a servo motor on the front axle, allowing precise turns when navigating obstacles or making sharp adjustments.

To ensure efficient navigation, the vehicle is equipped with a Raspberry Pi 5 and a camera module that processes real-time video data for AI-based obstacle detection and pathfinding. Additionally, three ultrasonic sensors are strategically positioned on the front, left, and right sides of the vehicle. These sensors help the vehicle maintain a central position between walls and detect when to turn or adjust its course.

A button is installed to start and stop the vehicle's operation, allowing easy control during competition.

Key Components:
6000 mAh Battery: Provides sufficient power for the entire competition.
Raspberry Pi 5: The main processing unit responsible for AI and sensor data interpretation.
DC Motors: Mounted on the rear axle for propulsion, connected to the L298N motor driver.
Servo Motor: Mounted on the front axle for steering.
L298N Motor Driver: Controls the DC motors, handles high voltage and current.
Ultrasonic Sensors: Positioned on the front, left, and right sides for distance measurement and obstacle detection.
Camera: Mounted on the vehicle for real-time video processing and AI navigation.
Button: Manually starts and stops the vehicle.

---

-------------------------------------------------------------------------------------------------Software Structure----------------------------------------------------------------------------------------------------
The software consists of several modules that work together to control the vehicle’s movement and decision-making processes.

Main Modules:
Movement Control Module: Handles the movement of the vehicle by controlling the DC motors and steering servo motor. This module receives input from the ultrasonic sensors to adjust speed and direction based on the vehicle’s surroundings. The gpiozero library is used to manage the motors and sensors.

Obstacle Detection Module: Processes input from the camera and ultrasonic sensors to detect obstacles in the vehicle’s path. It distinguishes between red, green, and purple cubes and determines the appropriate action based on the color:

Red Cube: The vehicle must avoid the obstacle by turning right.
Green Cube: The vehicle must avoid the obstacle by turning left.
Purple Cube: The vehicle identifies the space between two purple cubes as a parking zone.
AI Navigation Module: Utilizes the camera feed to calculate the vehicle’s direction and adjust its path accordingly. This module integrates image processing with AI algorithms to identify and track obstacles, ensuring the vehicle navigates accurately even in complex environments.

Ultrasonic Sensor Module: Responsible for processing data from the three ultrasonic sensors. These sensors measure the distance between the vehicle and surrounding objects (walls or obstacles). The vehicle maintains a central position between walls using input from the left and right sensors. If an object is detected within 10-15 cm in front of the vehicle, the software will adjust speed and direction to avoid a collision.

Button Control Module: Monitors the button input to start, stop, and restart the vehicle's operation. This ensures the vehicle can be controlled manually during the competition, and the system resets after each completed task.

---

----------------------------------------------------------------------------------------------Competition Task Breakdown-------------------------------------------------------------------------------------------
Races 1 and 2: Navigating Between Walls
In the first two races, the vehicle must complete three laps around a square arena with elevated inner walls. The ultrasonic sensors measure the distance from the walls, keeping the vehicle centered as it makes four turns per lap. The AI navigation module ensures the vehicle maintains a steady course while avoiding any potential collisions with the walls.

Races 3 and 4: Obstacle Avoidance and Parking
In the final two races, obstacles appear in the arena in the form of colored cubes:

Red Cubes: The vehicle must navigate around red cubes by turning right.
Green Cubes: The vehicle must navigate around green cubes by turning left.
Purple Cubes: When the vehicle detects two purple cubes, it identifies the area between them as a parking zone and must stop in that space.
Points are awarded based on the vehicle's ability to successfully navigate the arena, avoid obstacles, and park in designated areas.

---
