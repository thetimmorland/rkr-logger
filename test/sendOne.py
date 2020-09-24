import os
import can

os.system('sudo ip link set can0 up type can bitrate 100000')

can0 = can.interface.Bus(bustype = 'socketcan', channel = 'can0', bitrate = 1000000)
print(f'can0 channel info {can0.channel_info}\n')
os.system('ip -details -statistics link show can0')
print('\n')

# define some basic messages and print as examples
# create a default message with no parameters
default_msg = can.Message()
print('Default Message created with no parameter')
print(default_msg)
# is_extended_id controls the size of the arbitration_id
ext_id_msg = can.Message(is_extended_id=True)
print('Extended length arbitration ID message')
print(ext_id_msg)
std_id_msg = can.Message(is_extended_id=False)
print('Standard length arbitration ID message')
print(std_id_msg)
# arbitration_id is the identifier used for arbitration on the bus
# not sure what we will need here if we send messages on the boat
id_100_msg = can.Message(is_extended_id=False, arbitration_id=100)
print('Arbitration ID decimal 100 hex 64')
print(id_100_msg)
# data is an array of upto 8 bytes
max_data = bytearray([1, 2, 3, 4, 5, 6, 7, 8])
max_data_msg = can.Message(data=max_data)
print('Message with 8 byte payload')
print(max_data_msg)

# prepare a test message to send
test_msg = can.Message(is_extended_id=False, arbitration_id=100, data=[0x77, 0x77, 0x01, 0x01])
print('Test message to send')
print(test_msg)

try:
    print('Sending test message ...')
    can0.send(test_msg)
    print(f'Test message sent on {can0.channel_info}')
except can.CanError as e:
    print('Test message not sent')
    print(e)
    

os.system('sudo ifconfig can0 down')
