# import numpy as np

# # Create an empty array to store the stacked arrays
# stacked_arrays = np.empty((0, 3))  # shape (0, 3) means 0 rows and 3 columns

# # Loop over some arrays and add them to the stacked array
# for i in range(3):
#     arr = np.random.rand(1, 3)  # create a random 1x3 array
#     stacked_arrays = np.vstack((stacked_arrays, arr))  # add the array to the stacked array

# # Print the stacked array
# print(stacked_arrays)

# from machine import Pin
# from time import sleep

# pin = Pin("LED", Pin.OUT)

# while True:
#     pin.toggle()
#     sleep(1)
import serial

# Set the serial port and baud rate to match the Raspberry Pi Pico's settings
serial_port = "COM10"  # Update this to the correct port (Windows: "COMX", Mac/Linux: "/dev/ttyACMX")
baud_rate = 9600  # Update this to match the baud rate set on the Raspberry Pi Pico

def receive_data_from_pico():
    try:
        # ser = serial.Serial(serial_port)
        # x = ser.read()
        with serial.Serial(serial_port, 9600, timeout=1) as ser:
            x = ser.read()          # read one byte
            # s = ser.read(10) 
            print(ser.name)
            print(x)
        # Open the serial connection
        # with serial.Serial(serial_port, baud_rate) as ser:
        #     while True:
        #         # Read a line of data from the Raspberry Pi Pico
        #         line = ser.readline().decode().strip()
        #         print('reading line')

        #         # Process the data as needed
        #         if line:
        #             data_list = [float(val) for val in line.split(",")]
        #             # Now you have a list of floats from the Raspberry Pi Pico

        #             # Process the data further or perform any actions
        #             print("Received data:", data_list)
        #         print('no line')

    except serial.SerialException as e:
        print("Error:", e)

if __name__ == "__main__":
    receive_data_from_pico()
