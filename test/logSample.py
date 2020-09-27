# coding: utf-8

"""
logSample.py logs CAN traffic to a file on disk.
    logSample.py can0
    
logs a maximum of 10,000 messages.
uses the bitrate of 250,000 specified for NMEA2000
"""

import os
import can

def main():
    os.system('sudo ip link set can0 up type can bitrate 250000')
    can0 = can.interface.Bus(channel = 'can0', bustype = 'socketcan', bitrate=2500000)
    print(f'can0 channel info {can0.channel_info}\n')
    os.system('sudo ip -details -statistics link show can0')
    print('\n')

    # set up a buffer to store the messages from the bus
    reader = can.BufferedReader()
    notifier = can.Notifier(can0,[reader])

    # open a log file for the messages
    print('Open log file')
    logFile = open('~/rkr-logger/CANLog.txt', 'w')

    numberOfMessagesRead = 0
    while numberOfMessagesRead < 10000:
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

if __name__ == "__main__":
    main()
    
    
