# Bring up the CANBus and receive one message.
# if no message received in 10 seconds, time out.
# Bring down the CANBus

import os
import can

os.system('sudo ip link set can0 up type can bitrate 250000')

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan', bitrate=250000)
print(f'can0 channel info {can0.channel_info}\n')
os.system('sudo ip -details -statistics link show can0')
print('\n')

try:
    msg = can0.recv(10.0)
    print (msg)
    if msg is None:
        print('Timeout occurred, no message.')
except can.CanError as e:
    print('Something went wrong')
    print(e)

os.system('sudo ifconfig can0 down')
