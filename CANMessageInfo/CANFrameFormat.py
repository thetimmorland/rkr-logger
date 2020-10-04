#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:58:05 2020

@author: bill
"""

# NMEA2000 message frame
# BIT    CAN     ISO 11783                       NEMA 2000
#   1    SOF     SOF                             SOF
#   2    ID 28   Priority 3                      PTY 03
#   3    ID 27   Priority 2                      PTY 02
#   4    ID 26   Priority 1                      PTY 01
#   5    ID 25   Reserved Bit                    PGN 18
#   6    ID 24   Data Page                       PGN 17
#        (sets an auxiliary page of parameter groups)       
#   7    ID 23   PDU Format Bit 8                PGN 16
#   8    ID 22   PDU Format Bit 7                PGN 15
#   9    ID 21   PDU Format Bit 6                PGN 14
#  10    ID 20   PDU Format Bit 5                PGN 13
#  11    ID 19   PDU Format Bit 4                PGN 12
#  12    ID 18   PDU Format Bit 3                PGN 11
#  13    SRR     Subtitute Remote Request        SRR
#  14    IDE     Identifier Extension Bit        1
#        (expect this always to be 1 for NMEA2000)
#  15    ID 17   PDU Format Bit 2                PGN 10
#  16    ID 16   PDU Format Bit 1                PGN 09
#  17    ID 15   PDU Specific Bit 8              PGN 08
#  18    ID 14   PDU Specific Bit 7              PGN 07
#  19    ID 13   PDU Specific Bit 6              PGN 06
#  20    ID 12   PDU Specific Bit 5              PGN 05
#  21    ID 11   PDU Specific Bit 4              PGN 04
#  22    ID 10   PDU Specific Bit 3              PGN 03
#  23    ID 09   PDU Specific Bit 2              PGN 02
#  24    ID 08   PDU Specific Bit 1              PGN 01
#  25    ID 07   Source Address Bit 8            SRC 08
#  26    ID 06   Source Address Bit 7            SRC 07
#  27    ID 05   Source Address Bit 6            SRC 06
#  28    ID 04   Source Address Bit 5            SRC 05
#  29    ID 03   Source Address Bit 4            SRC 04
#  30    ID 02   Source Address Bit 3            SRC 03
#  31    ID 01   Source Address Bit 2            SRC 02
#  32    ID 00   Source Address Bit 1            SRC 01
#  33    RTR     Remote Transmission Request Bit RTR
#        (1 if frame is a request for data)
#        (when logging we should discard all reequest where RTR = 1)
#  34    R 1     CAN Reserved Bit 1
#  35    R 2     CAN Reserved Bit 2
#  36    DLC 01  Data Length Code Bit 1
#  37    DLC 02  Data Length Code Bit 2
#  38    DLC 03  Data Length Code Bit 3
#  39    DLC 04  Data Length Code Bit 4



