import os
import can

os.system('sudo ip link set can0 up type can bitrate 250000')

can0 = can.interface.Bus(bustype = 'socketcan', channel = 'can0', bitrate = 250000)
print(f'can0 channel info {can0.channel_info}\n')
os.system('ip -details -statistics link show can0')
print('\n')

# define some basic messages and print as examples
# create a default message with no parameters
# std_id_msg = can.Message(is_extended_id=False)
# print('Standard length arbitration ID message')
# print(std_id_msg)
# arbitration_id is the identifier used for arbitration on the bus
# not sure what we will need here if we send messages on the boat

# prepare a test message to send
msg_list = [can.Message(arbitration_id=0x9F10D0F, data=[0xFF, 0xFF, 0xFF, 0x7F, 0x1B, 0xFF, 0xFF, 0xFF]),
            can.Message(arbitration_id=0xDF11302, data=[0x00, 0x1C, 0x35, 0x00, 0x00, 0xFF, 0x7F, 0xFD]),
            can.Message(arbitration_id=0x9f11202, data=[0x00, 0x97, 0x04, 0xFF, 0x7F, 0xFF, 0x7F, 0xFD]),
            can.Message(arbitration_id=0xDF11902, data=[0x00, 0xFF, 0x7F, 0xA6, 0x00, 0x70, 0x00, 0xFF]),
            can.Message(arbitration_id=0xDF11402, data=[0x00, 0xC9, 0xFF, 0xFF, 0xFF, 0xFF, 0x7F, 0xFD]),
            can.Message(arbitration_id=0xDF50B23, data=[0xFF, 0xBB, 0x02, 0x00, 0x00, 0x00, 0x00, 0xFF]),
            can.Message(arbitration_id=0x9F10D0F, data=[0xFF, 0xFF, 0xFF, 0x7F, 0x1B, 0xFF, 0xFF, 0xFF]),
            can.Message(arbitration_id=0x9FD0210, data=[0xB2, 0x8C, 0x02, 0x0B, 0x7A, 0xFA, 0xFF, 0xFF]),
            can.Message(arbitration_id=0x9F10D0F, data=[0xFF, 0xFF, 0xFF, 0x7F, 0x1B, 0xFF, 0xFF, 0xFF]),
            can.Message(arbitration_id=0xDF11302, data=[0x00, 0x93, 0x4F, 0x00, 0x00, 0xFF, 0x7F, 0xFD])]

for test_msg in msg_list:
    try:
        print(test_msg)
        can0.send(test_msg)
    except can.CanError as e:
        print('Test message not sent')
        print(e)

print('\n\n')
os.system('sudo ifconfig can0 down')
os.system('ip -details -statistics link show can0')
print('\n')
