#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 15:55:05 2020

@author: bill

This module contains the implementation of :class:`nmea200.Frame`.

"""

import can
import time

class Frame(can.Message):
    
    def __init__(self, timestamp=0.0, arbitration_id=0, is_extended_id=True,
                 is_remote_frame=False, is_error_frame=False, channel=None,
                 dlc=None, data=None,
                 is_fd=False, bitrate_switch=False, error_state_indicator=False,
                 check=False):
        can.Message.__init__(self, timestamp=timestamp, 
                             arbitration_id=arbitration_id,
                             is_extended_id = is_extended_id,
                             is_remote_frame=is_remote_frame, 
                             is_error_frame=is_error_frame, channel=channel,
                             dlc=dlc, data=data, is_fd=is_fd,
                             bitrate_switch=bitrate_switch,
                             error_state_indicator=error_state_indicator,
                             check=check)
                             
    
    def __str__(self):
        # Timestamp
        timestamp_string = time.ctime(self.timestamp)
        # Priority
        priority = (self.arbitration_id & int('0b11100000000000000000000000000', 2)) >> 26
        priority_string = str(priority)
        # PGN
        PGN = (self.arbitration_id &      int('0b00000111111111111111100000000', 2)) >> 8
        PGN_string = str(PGN)
        # Source Address
        # data
        return timestamp_string + ', ' + priority_string + ', ' PGN_string

    
# PGN 127245 Rudder
arb_id = int ('0b111001111100010000110100000000', 2)    
msg = Frame(timestamp=time.time(), arbitration_id=arb_id)
print(msg)

