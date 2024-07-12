# Pyhon Dynamixel Read Write

## Table of Contents
- [Description](#description)
- [Table of Contents](#table-of-contents)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Operations](#operations)
- [Author](#author)
- [License](#license)

## Description
This script is used to control a Dynamixel motor using the Dynamixel SDK library. It allows the user to set the motor's goal position and read the current position.


## Requirements
- Python 3.12
- Dynamixel SDK library

## Installation
To install the required libraries, follow these steps:

1. Clone the repository:
   git clone https://github.com/username/project_name.git
2. Navigate to the project directory:
   cd project_name
3. Install the Dynamixel SDK library:
   pip install dynamixel-sdk
   
## Usage
To run the script, follow these steps:
1. Ensure that the Dynamixel motor is connected to the computer on port COM3 (or modify the DEVICENAME variable in the code if you are using a different port).
2. Run the script:
   python script_name.py
3. Follow the instructions displayed in the terminal to enter the motor's goal position.

## Operations

The script performs the following operations:

1. Opens the communication port.
2. Sets the communication speed (baud rate).
3. Enables the motor's torque.
4. Allows the user to enter the motor's goal position.
5. Sends the goal position to the motor.
6. Reads and displays the current motor position.
7. Disables the motor's torque after operation.
8. Closes the communication port.

## Author
Tymon Stankiewicz

##License 
Academic Free License
