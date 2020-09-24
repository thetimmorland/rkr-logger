# Bring up the CANBus
# Set up a buffered reader for the messages
# Read ten messages from the buffer and log them to a file
# Bring down the CANBus

import os
import can

os.system('sudo ip link set can0 up type can bitrate 100000')

can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan', bitrate=1000000)
print(f'can0 channel info {can0.channel_info}\n')
os.system('sudo ip -details -statistics link show can0')
print('\n')

# set up a buffer to store the messages from the bus
reader = can.BufferedReader()
notifier = can.Notifier(can0,[reader])

# open a log file for the messages
print('Open log file')
logFile = open('testLogTen.txt', 'w')

numberOfMessagesRead = 0
while numberOfMessagesRead < 10:
    try:
        msg = reader.get_message()
    except can.CanError as e:
        print('Something went wrong')
        print(e)
    if not(msg == None):
        print('Read message: ' + msg.__str__())
        numberOfMessagesRead += 1
        logFile.write(msg.__str__() + '\n')

print('Close log file')
logFile.close()
notifier.stop()
can0.shutdown()