import os
import sys
import ctypes
from dynamixel_sdk import *  # Uses Dynamixel SDK library

# Control table address
ADDR_TORQUE_ENABLE = 512  # Address for the torque enable
ADDR_GOAL_POSITION = 564  # Address for the goal position
ADDR_PRESENT_POSITION = 580  # Address for the present position

# Protocol version
PROTOCOL_VERSION = 2.0

# Default setting
DXL_ID = 1  # Dynamixel ID
BAUDRATE = 57600  # Dynamixel default baudrate
DEVICENAME = 'COM3'  # Check which port is being used on your controller
TORQUE_ENABLE = 1  # Value for enabling the torque
TORQUE_DISABLE = 0  # Value for disabling the torque
DXL_MINIMUM_POSITION_VALUE = -251173  # Minimum position value
DXL_MAXIMUM_POSITION_VALUE = 251173  # Maximum position value
DXL_MOVING_STATUS_THRESHOLD = 20  # Dynamixel moving status threshold

COMM_SUCCESS = 0  # Communication Success result value
COMM_TX_FAIL = -1001  # Communication Tx Failed

# Initialize PortHandler instance
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    sys.exit()

# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    sys.exit()

# Enable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("Failed to enable torque: %s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("Torque enable error: %s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Torque enabled successfully")

while True:
    # Get user input for goal position
    user_input = input(
        f"Enter the goal position ({DXL_MINIMUM_POSITION_VALUE} to {DXL_MAXIMUM_POSITION_VALUE}) or 'exit' to quit: ")

    if user_input.lower() == 'exit':
        break

    try:
        goal_position = int(user_input)
        if goal_position < DXL_MINIMUM_POSITION_VALUE or goal_position > DXL_MAXIMUM_POSITION_VALUE:
            raise ValueError("Position out of range")
    except ValueError as e:
        print("Invalid input:", e)
        continue

    # Write goal position
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL_ID, ADDR_GOAL_POSITION, goal_position)
    if dxl_comm_result != COMM_SUCCESS:
        print("Failed to set goal position: %s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("Goal position error: %s" % packetHandler.getRxPacketError(dxl_error))
    else:
        print("Goal position set successfully")

    # Read present position
    dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL_ID,
                                                                                   ADDR_PRESENT_POSITION)
    if dxl_comm_result != COMM_SUCCESS:
        print("Failed to read present position: %s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("Present position read error: %s" % packetHandler.getRxPacketError(dxl_error))
    else:
        print("Present position: %d" % dxl_present_position)

# Disable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("Failed to disable torque: %s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("Torque disable error: %s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Torque disabled successfully")

# Close port
portHandler.closePort()
