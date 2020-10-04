# Bring up the CANBus
# Set up a buffered reader for the messages
# Read ten messages from the buffer and log them to a file
# Bring down the CANBus

import os
import can
import datetime

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
date_today = datetime.datetime.today().strftime('%Y%m%d')
logFile = open('/home/pi/can-logs/' + date_today + 'Log.n2k', 'w')

number_of_messages_read = 0
# priority mask
priority_mask = int('0b11100000000000000000000000000',2)
# PGN mask
PGN_mask = int('0b00011111111111111111100000000',2)
# source mask
source_mask = int('0b00000000000000000000011111111',2)

while number_of_messages_read < 20000000:
    try:
        msg = reader.get_message()
        if not(msg == None):
            number_of_messages_read += 1
            if not(msg.is_extended_id):
                # This should never happen with NMEA 2000
                continue
            if msg.is_remote_frame:
                # We don't want to log remote requests
                # maybe offer this as an option later
                continue
            if msg.is_error_frame:
                # Ignore error frames
                continue

            msg_timestamp = datetime.datetime.fromtimestamp(msg.timestamp)
            # construct a byte string in hex for the message data
            # creates a leading , that I should like to get rid of
            data_string = ''
            for a in msg.data:
                b = hex(a)[2:].zfill(2)
                data_string = ','.join([data_string, b])
            # Create the row to write to the log file
            row = ','.join(
                [
                    # timestamp
                    # might need to strip the last 3 decimal places of the time
                    msg_timestamp.__str__(),
                    # priority (CAN Identification Field bits 26-28)
                    str((msg.arbitration_id & priority_mask) >> 26),
                    # PGN (CAN Identification Field bits 08-24)
                    str((msg.arbitration_id & PGN_mask) >> 8),
                    # source (CAN Identification Field bits 00-07)
                    str((msg.arbitration_id & source_mask)),
                    # destination
                    # need to work out how to find the destination
                    '255',
                    # data length code
                    str(msg.dlc),
                    # data
                ]
            )
            # have to do this last join separately to avoid a double comma
            row = ''.join([row, data_string])
            logFile.write(row + '\n')
    except KeyboardInterrupt:
        logFile.close()
        notifier.stop()
        can0.shutdown()
