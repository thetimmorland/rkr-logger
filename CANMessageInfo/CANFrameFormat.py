#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:58:05 2020

@author: bill
"""

# NMEA2000 message frame
# BIT    CAN     ISO 11783
#   1    SOF     SOF
#   2    ID 28   Priority 3
#   3    ID 27   Priority 2
#   4    ID 26   Priority 1
#   5    ID 25   Reserved Bit
#   6    ID 24   Data Page (what does this mean?)
#   7    ID 23   PDU Format Bit 8
#   8    ID 22   PDU Format Bit 7
#   9    ID 21   PDU Format Bit 6
#  10    ID 20   PDU Format Bit 5
#  11    ID 19   PDU Format Bit 4
#  12    ID 18   PDU Format Bit 3
#  13    SRR     Subtitute Remote Request
#  14    IDE     Identifier Extension Bit 
#        (expect this always to be 1 for NMEA2000)
#  15    ID 17   PDU Format Bit 2
#  16    ID 16   PDU Format Bit 1
#  17    ID 15   PDU Specific Bit 8
#  18    ID 14   PDU Specific Bit 7
#  19    ID 13   PDU Specific Bit 6
#  20    ID 12   PDU Specific Bit 5
#  21    ID 11   PDU Specific Bit 4
#  22    ID 10   PDU Specific Bit 3
#  23    ID 09   PDU Specific Bit 2
#  24    ID 08   PDU Specific Bit 1
#  25    ID 07   Source Address Bit 8
#  26    ID 06   Source Address Bit 7
#  27    ID 05   Source Address Bit 6
#  28    ID 04   Source Address Bit 5
#  29    ID 03   Source Address Bit 4
#  30    ID 02   Source Address Bit 3
#  31    ID 01   Source Address Bit 2
#  32    ID 00   Source Address Bit 1
#  33    RTR     Remote Transmission Request Bit 
#        (1 if frame is a request for data)
#        (when logging we should discard all reequest where RTR = 1)
#  34    R 1     CAN Reserved Bit 1
#  35    R 2     CAN Reserved Bit 2
#  36    DLC 01  Data Length Code Bit 1
#  37    DLC 02  Data Length Code Bit 2
#  38    DLC 03  Data Length Code Bit 3
#  39    DLC 04  Data Length Code Bit 4



