import serial

# Replace 'COMX' with the correct serial port for your Arduino (e.g., '/dev/ttyACM0' on Linux or 'COM3' on Windows).
ser = serial.Serial('COM8', 115200)

try:
    while True:
        # Read data from the Arduino (readline() returns bytes)
        line = ser.readline()
        try:
            # Convert bytes to a string and strip any leading/trailing whitespace or newline characters
            data_str = line.decode().strip()
            # Convert the string to an integer (assuming it's a numerical value sent from the Arduino)
            data_value = int(data_str)
            # Print the received data
            print(data_value)
        except UnicodeDecodeError:
            # If there's a decoding error, print the raw bytes for debugging
            print("Received non-decodable data:", line)
        except ValueError:
            # If the data cannot be converted to an integer, print the raw string for debugging
            print("Received non-integer data:", 'Cannot convert to integer')
except KeyboardInterrupt:
    # Close the serial connection when the script is interrupted
    ser.close()
